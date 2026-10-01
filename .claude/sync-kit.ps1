<#
.SYNOPSIS
    Materializes the Pantonic agentic kit (skills + agents) from the vendored
    kit/ subtree into the flat .claude/ namespace of the consuming project.

.DESCRIPTION
    In the hub (PantonicApp) this file is versioned at .claude/sync-kit.ps1.
    `git subtree split --prefix=.claude` publishes it to the root of the
    `kit` branch, and a consumer's `git subtree add --prefix=.claude/kit
    <hub-url> kit --squash` lands it at <child>/.claude/kit/sync-kit.ps1 —
    the location this script actually runs from. It resolves its own kit
    root and the destination .claude/ purely from $PSScriptRoot (no
    hardcoded absolute path), so the same file works unmodified in any
    consumer repo.

    Copies:
      kit/skills/<name>/   -> .claude/skills/<name>/   (full directory mirror)
      kit/agents/<name>.md -> .claude/agents/<name>.md
      kit/tools/**, kit/checks/** -> .claude/tools/**, .claude/checks/**
                                     (per file; __pycache__ ignored)
      kit/projecoes.json, kit/KIT_VERSION -> .claude/

    Then projects the kit hooks: `python .claude/tools/materializar.py apply
    --alvo projeto` writes projecoes.json into .claude/settings.json, keeping
    permissions and non-kit hooks (-Check runs `drift` instead). Without
    python on PATH it only warns.

    Doctrine documents (GOVERNANCA.md, ARQUITETURA_PANTONICA.md,
    docs/RUBRICA_DE_REVISAO.md) live outside the `.claude/` prefix and do not
    travel with the subtree.

    Exclusions: <child>/.claude/kit-exclude.txt, one entry per line.
      - Blank lines and lines whose first non-blank character is '#' are
        ignored.
      - Inline comments are supported: everything from the first '#' on a
        line is discarded before the entry is used, so
        "skills/guardrails-check   # local override" is read as
        "skills/guardrails-check". A continuation line that is only a
        comment (e.g. an indented "# ..." line explaining the entry above)
        collapses to empty and is skipped the same way.
      - Normative entry format is "<namespace>/<name>", e.g.
        "skills/guardrails-check", "agents/pantonic-executor",
        "tools/backlog.py", "projecoes.json". A bare name
        ("guardrails-check") is also accepted for compatibility and matches
        either namespace, but namespaced entries are preferred — a bare
        name is ambiguous between skills/ and agents/.

    An excluded artifact is skipped entirely: the local override under
    .claude/ survives the sync untouched. Any local artifact under
    .claude/skills or .claude/agents whose name does not come from the kit
    is never touched. Inside a managed (non-excluded) skill directory the
    mirror is total: a file removed from the kit disappears from the
    consumer on the next sync.

    Running the script twice in a row with no kit changes produces no
    further writes (idempotent).

    Sync stamp: on every effective (non -Check) run, once the copy pass
    completes, the script writes <kitRoot>/SYNC_STATE — version=<KIT_VERSION
    content, or "unknown" if absent>, synced_at=<UTC ISO 8601>,
    mode=subtree|copia (subtree when an origin commit was resolved, copia
    otherwise). -Check never writes it: both -Check exit paths return before
    this point.

    Origin signature verification: before any copy or comparison, the
    script resolves the "origin commit" — the last commit in this repo
    that touched the kit path ($PSScriptRoot) — and runs
    `git verify-commit` against it. An unverifiable origin (no signing
    key configured, no matching commit, git missing, or this directory
    not being a git repo) is treated as "not signed": by default this
    only prints a WARN line and the sync proceeds; with -RequireSignature
    it aborts instead. This check is read-only, so it also runs under
    -Check.

.PARAMETER Check
    Compare only; makes no changes. Lists the managed artifacts that
    diverge from the kit and exits 1 if any do, 0 if the tree is clean.
    Signature verification (see above) still runs, since -Check is
    read-only.

.PARAMETER RequireSignature
    Makes origin signature verification blocking: if the origin commit
    is missing or not signature-verified, the script aborts with an
    actionable message and a non-zero exit code instead of only warning.
#>
[CmdletBinding()]
param(
    [switch]$Check,
    [switch]$RequireSignature
)

$ErrorActionPreference = 'Stop'

$kitRoot    = $PSScriptRoot
$claudeRoot = Split-Path -Path $kitRoot -Parent

# ---------------------------------------------------------------------------
# Exclusion list
# ---------------------------------------------------------------------------

function Get-ExcludedKeys {
    param([string]$ExcludeFile)

    $excluded = New-Object System.Collections.Generic.HashSet[string]
    if (-not (Test-Path -LiteralPath $ExcludeFile -PathType Leaf)) {
        return ,$excluded
    }

    foreach ($rawLine in Get-Content -LiteralPath $ExcludeFile) {
        $line = $rawLine
        $hashIndex = $line.IndexOf('#')
        if ($hashIndex -ge 0) {
            $line = $line.Substring(0, $hashIndex)
        }
        $line = $line.Trim()
        if ($line.Length -eq 0) {
            continue
        }
        [void]$excluded.Add($line)
    }
    return ,$excluded
}

function Test-Excluded {
    param(
        [System.Collections.Generic.HashSet[string]]$Excluded,
        [string]$Namespace,
        [string]$Name
    )
    return $Excluded.Contains("$Namespace/$Name") -or $Excluded.Contains($Name)
}

$excludeFile  = Join-Path $claudeRoot 'kit-exclude.txt'
$excludedKeys = Get-ExcludedKeys -ExcludeFile $excludeFile

# ---------------------------------------------------------------------------
# Origin signature verification (runs before any copy/write, and under
# -Check too since it is read-only)
# ---------------------------------------------------------------------------

function Invoke-GitCommand {
    param(
        [string]$RepoDir,
        [string[]]$Arguments
    )

    $output   = $null
    $exitCode = 1
    try {
        $output = & git -C $RepoDir @Arguments 2>&1
        $exitCode = $LASTEXITCODE
    } catch {
        $output   = $null
        $exitCode = 1
    }
    return [PSCustomObject]@{ Output = $output; ExitCode = $exitCode }
}

function Get-KitOriginCommit {
    param([string]$KitRoot)

    $result = Invoke-GitCommand -RepoDir $KitRoot -Arguments @('log', '-1', '--format=%H', '--', '.')
    if ($result.ExitCode -eq 0 -and $result.Output) {
        $first = $result.Output | Select-Object -First 1
        $sha = "$first".Trim()
        if ($sha.Length -gt 0) {
            return $sha
        }
    }
    return $null
}

function Test-KitSignatureVerified {
    param(
        [string]$KitRoot,
        [string]$Sha
    )

    if (-not $Sha) {
        return $false
    }
    $result = Invoke-GitCommand -RepoDir $KitRoot -Arguments @('verify-commit', $Sha)
    return ($result.ExitCode -eq 0)
}

$originSha         = Get-KitOriginCommit -KitRoot $kitRoot
$signatureVerified = Test-KitSignatureVerified -KitRoot $kitRoot -Sha $originSha

if (-not $signatureVerified) {
    $shaLabel = if ($originSha) { $originSha } else { '<unresolved: no commit found for this kit path, git missing, or not a git repo>' }
    if ($RequireSignature) {
        Write-Host "sync-kit: ABORT - origin commit $shaLabel is not signature-verified. Configure commit signing (git config user.signingkey <key-id> && git config commit.gpgsign true, then re-commit) or omit -RequireSignature to proceed with a warning." -ForegroundColor Red
        exit 1
    }
    Write-Host "WARN: sync-kit - origin commit $shaLabel is not signature-verified (git verify-commit failed or unavailable). Proceeding without signature verification. Re-run with -RequireSignature to enforce."
}

# ---------------------------------------------------------------------------
# Directory mirror helpers (used for skills/<name>/)
# ---------------------------------------------------------------------------

function Get-RelativeFileMap {
    param([string]$Root)

    $map = @{}
    if (-not (Test-Path -LiteralPath $Root -PathType Container)) {
        return $map
    }
    $rootFull = (Resolve-Path -LiteralPath $Root).Path
    Get-ChildItem -LiteralPath $Root -Recurse -File | ForEach-Object {
        $rel = $_.FullName.Substring($rootFull.Length).TrimStart('\', '/')
        $map[$rel] = $_.FullName
    }
    return $map
}

function Compare-Directory {
    param([string]$SourceDir, [string]$DestDir)

    $srcMap = Get-RelativeFileMap -Root $SourceDir
    $dstMap = Get-RelativeFileMap -Root $DestDir

    $diffs = New-Object System.Collections.Generic.List[string]

    foreach ($rel in $srcMap.Keys) {
        if (-not $dstMap.ContainsKey($rel)) {
            $diffs.Add("missing: $rel")
            continue
        }
        $srcHash = (Get-FileHash -LiteralPath $srcMap[$rel] -Algorithm SHA256).Hash
        $dstHash = (Get-FileHash -LiteralPath $dstMap[$rel] -Algorithm SHA256).Hash
        if ($srcHash -ne $dstHash) {
            $diffs.Add("changed: $rel")
        }
    }
    foreach ($rel in $dstMap.Keys) {
        if (-not $srcMap.ContainsKey($rel)) {
            $diffs.Add("extra: $rel")
        }
    }
    return $diffs
}

function Sync-Directory {
    param([string]$SourceDir, [string]$DestDir)

    $srcMap = Get-RelativeFileMap -Root $SourceDir
    $dstMap = Get-RelativeFileMap -Root $DestDir

    foreach ($rel in $srcMap.Keys) {
        $srcPath    = $srcMap[$rel]
        $dstPath    = Join-Path $DestDir $rel
        $dstDirPart = Split-Path $dstPath -Parent
        if (-not (Test-Path -LiteralPath $dstDirPart)) {
            New-Item -ItemType Directory -Path $dstDirPart -Force | Out-Null
        }
        $needsCopy = $true
        if (Test-Path -LiteralPath $dstPath) {
            $srcHash   = (Get-FileHash -LiteralPath $srcPath -Algorithm SHA256).Hash
            $dstHash   = (Get-FileHash -LiteralPath $dstPath -Algorithm SHA256).Hash
            $needsCopy = ($srcHash -ne $dstHash)
        }
        if ($needsCopy) {
            Copy-Item -LiteralPath $srcPath -Destination $dstPath -Force
        }
    }

    foreach ($rel in $dstMap.Keys) {
        if (-not $srcMap.ContainsKey($rel)) {
            Remove-Item -LiteralPath $dstMap[$rel] -Force
        }
    }

    # Prune now-empty directories left behind by removals.
    if (Test-Path -LiteralPath $DestDir) {
        Get-ChildItem -LiteralPath $DestDir -Recurse -Directory |
            Sort-Object { $_.FullName.Length } -Descending |
            ForEach-Object {
                if (-not (Get-ChildItem -LiteralPath $_.FullName -Force)) {
                    Remove-Item -LiteralPath $_.FullName -Force
                }
            }
    }
}

function Test-FileChanged {
    param([string]$SourceFile, [string]$DestFile)

    if (-not (Test-Path -LiteralPath $DestFile)) {
        return $true
    }
    $srcHash = (Get-FileHash -LiteralPath $SourceFile -Algorithm SHA256).Hash
    $dstHash = (Get-FileHash -LiteralPath $DestFile -Algorithm SHA256).Hash
    return ($srcHash -ne $dstHash)
}

# ---------------------------------------------------------------------------
# Enumerate managed artifacts
# ---------------------------------------------------------------------------

$skillsSrc = Join-Path $kitRoot 'skills'
$agentsSrc = Join-Path $kitRoot 'agents'
$skillsDst = Join-Path $claudeRoot 'skills'
$agentsDst = Join-Path $claudeRoot 'agents'

$skillNames = @()
if (Test-Path -LiteralPath $skillsSrc -PathType Container) {
    $skillNames = Get-ChildItem -LiteralPath $skillsSrc -Directory | Select-Object -ExpandProperty Name
}

$agentNames = @()
if (Test-Path -LiteralPath $agentsSrc -PathType Container) {
    $agentNames = Get-ChildItem -LiteralPath $agentsSrc -Filter '*.md' -File |
        ForEach-Object { $_.BaseName }
}

$copied    = 0
$skipped   = 0
$diverging = New-Object System.Collections.Generic.List[string]

foreach ($name in $skillNames) {
    if (Test-Excluded -Excluded $excludedKeys -Namespace 'skills' -Name $name) {
        $skipped++
        continue
    }
    $src = Join-Path $skillsSrc $name
    $dst = Join-Path $skillsDst $name
    if ($Check) {
        $diffs = Compare-Directory -SourceDir $src -DestDir $dst
        if ($diffs.Count -gt 0) {
            $diverging.Add("skills/$name")
        }
    } else {
        Sync-Directory -SourceDir $src -DestDir $dst
    }
    $copied++
}

foreach ($name in $agentNames) {
    if (Test-Excluded -Excluded $excludedKeys -Namespace 'agents' -Name $name) {
        $skipped++
        continue
    }
    $src = Join-Path $agentsSrc "$name.md"
    $dst = Join-Path $agentsDst "$name.md"
    if ($Check) {
        if (Test-FileChanged -SourceFile $src -DestFile $dst) {
            $diverging.Add("agents/$name")
        }
    } else {
        $dstDirPart = Split-Path $dst -Parent
        if (-not (Test-Path -LiteralPath $dstDirPart)) {
            New-Item -ItemType Directory -Path $dstDirPart -Force | Out-Null
        }
        if (Test-FileChanged -SourceFile $src -DestFile $dst) {
            Copy-Item -LiteralPath $src -Destination $dst -Force
        }
    }
    $copied++
}

# ---------------------------------------------------------------------------
# Runtime support files: tools/, checks/, projecoes.json, KIT_VERSION.
# Skills and agents call `.claude/tools/*.py` and `.claude/checks/*` by path,
# so these land at the same relative location they have in the hub. Managed
# per file (key "<namespace>/<relative path>", or the bare file name for the
# two root files): a consumer-local file whose name does not come from the
# kit is never touched, and a file removed from the kit is left in place.
# ---------------------------------------------------------------------------

$supportFiles = New-Object System.Collections.Generic.List[object]
foreach ($ns in @('tools', 'checks')) {
    $nsSrc = Join-Path $kitRoot $ns
    if (-not (Test-Path -LiteralPath $nsSrc -PathType Container)) { continue }
    Get-ChildItem -LiteralPath $nsSrc -Recurse -File |
        Where-Object { $_.FullName -notmatch '[\\/]__pycache__[\\/]' } |
        ForEach-Object {
            $rel = $_.FullName.Substring($nsSrc.Length).TrimStart('\', '/')
            $supportFiles.Add([PSCustomObject]@{
                Namespace = $ns
                Name      = $_.Name
                Key       = "$ns/$($rel -replace '\\', '/')"
                Source    = $_.FullName
                Dest      = Join-Path (Join-Path $claudeRoot $ns) $rel
            })
        }
}
foreach ($rootFile in @('projecoes.json', 'KIT_VERSION')) {
    $rootSrc = Join-Path $kitRoot $rootFile
    if (Test-Path -LiteralPath $rootSrc -PathType Leaf) {
        $supportFiles.Add([PSCustomObject]@{
            Namespace = ''
            Name      = $rootFile
            Key       = $rootFile
            Source    = $rootSrc
            Dest      = Join-Path $claudeRoot $rootFile
        })
    }
}

foreach ($f in $supportFiles) {
    if ($excludedKeys.Contains($f.Key) -or
        (Test-Excluded -Excluded $excludedKeys -Namespace $f.Namespace -Name $f.Name)) {
        $skipped++
        continue
    }
    if ($Check) {
        if (Test-FileChanged -SourceFile $f.Source -DestFile $f.Dest) {
            $diverging.Add($f.Key)
        }
    } else {
        $dstDirPart = Split-Path $f.Dest -Parent
        if (-not (Test-Path -LiteralPath $dstDirPart)) {
            New-Item -ItemType Directory -Path $dstDirPart -Force | Out-Null
        }
        if (Test-FileChanged -SourceFile $f.Source -DestFile $f.Dest) {
            Copy-Item -LiteralPath $f.Source -Destination $f.Dest -Force
        }
    }
    $copied++
}

# ---------------------------------------------------------------------------
# Hook projection: the materialized copy of materializar.py (under
# <claudeRoot>/tools, not the one under kit/) projects projecoes.json into
# <claudeRoot>/settings.json, so hook commands point at .claude/tools/ —
# the same path the skills use. -Check runs the read-only `drift` instead.
# ---------------------------------------------------------------------------

function Invoke-Materializar {
    param([string]$Command)

    $script = Join-Path (Join-Path $claudeRoot 'tools') 'materializar.py'
    if (-not (Test-Path -LiteralPath $script -PathType Leaf)) {
        Write-Host "WARN: $script ausente - hooks do kit nao projetados em settings.json."
        return $true
    }
    $python = Get-Command python -ErrorAction SilentlyContinue
    if (-not $python) {
        Write-Host "WARN: python fora do PATH - rode 'python .claude/tools/materializar.py $Command --alvo projeto'."
        return $true
    }
    & $python.Source $script $Command --alvo projeto --kit-root $claudeRoot | Write-Host
    return ($LASTEXITCODE -eq 0)
}

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

if ($Check) {
    if (-not (Invoke-Materializar -Command 'drift')) {
        $diverging.Add('settings.json (hooks do kit)')
    }
    if ($diverging.Count -gt 0) {
        Write-Host "sync-kit -Check: $($diverging.Count) managed artifact(s) diverge from the kit:"
        foreach ($d in $diverging) { Write-Host "  - $d" }
        exit 1
    }
    Write-Host "sync-kit -Check: clean, $copied managed artifact(s) match the kit ($skipped excluded)."
    exit 0
}

Write-Host "sync-kit: $copied copied, $skipped skipped by exclusion."

if (-not (Invoke-Materializar -Command 'apply')) {
    Write-Error "sync-kit: materializar apply falhou - settings.json nao reflete projecoes.json."
    exit 1
}

# ---------------------------------------------------------------------------
# Sync stamp (only reached on an effective sync: both -Check branches above
# exit before this point, so this write never happens under -Check)
# ---------------------------------------------------------------------------

$versionFile = Join-Path $kitRoot 'KIT_VERSION'
$version = 'unknown'
if (Test-Path -LiteralPath $versionFile -PathType Leaf) {
    $versionContent = (Get-Content -LiteralPath $versionFile -Raw).Trim()
    if ($versionContent.Length -gt 0) {
        $version = $versionContent
    }
}

$syncedAt = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
$mode     = if ($originSha) { 'subtree' } else { 'copia' }

$syncStatePath  = Join-Path $kitRoot 'SYNC_STATE'
$syncStateLines = @(
    "version=$version"
    "synced_at=$syncedAt"
    "mode=$mode"
)
Set-Content -LiteralPath $syncStatePath -Value $syncStateLines -Encoding utf8NoBOM
