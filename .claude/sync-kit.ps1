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
        "skills/guardrails-check", "agents/pantonic-executor". A bare name
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

.PARAMETER Check
    Compare only; makes no changes. Lists the managed artifacts that
    diverge from the kit and exits 1 if any do, 0 if the tree is clean.
#>
[CmdletBinding()]
param(
    [switch]$Check
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
        return $excluded
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
    return $excluded
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
# Summary
# ---------------------------------------------------------------------------

if ($Check) {
    if ($diverging.Count -gt 0) {
        Write-Host "sync-kit -Check: $($diverging.Count) managed artifact(s) diverge from the kit:"
        foreach ($d in $diverging) { Write-Host "  - $d" }
        exit 1
    }
    Write-Host "sync-kit -Check: clean, $copied managed artifact(s) match the kit ($skipped excluded)."
    exit 0
}

Write-Host "sync-kit: $copied copied, $skipped skipped by exclusion."
