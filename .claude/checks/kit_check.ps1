<#
.SYNOPSIS
    Validador estrutural do kit agêntico Pantonic* (.claude/).

.DESCRIPTION
    V2K-T1 (docs/plans/P-0729-v2-melhoria-candidatos.md §3 T1, candidato C-01).
    Falha (exit != 0) quando um artefato de extensão do kit está estruturalmente
    inválido. NÃO interpreta semântica de doutrina — só forma sintática do
    frontmatter YAML e paridade de versão (ver risco registrado na ficha C-01 /
    BM-14§D9: validar semântica de doutrina é fora de escopo deste script).

    Modos previstos: -generate e -check-drift são reservados para V2K-T2 e ainda
    não implementados; o parâmetro já aceita os três valores para não exigir
    mudança de assinatura depois.

.PARAMETER Mode
    'validate' (único implementado nesta tarefa), 'generate' ou 'check-drift'
    (reservados, V2K-T2).

.PARAMETER KitRoot
    Raiz do kit (equivalente a .claude/) a validar. Default: resolvida a partir
    do caminho deste script (.claude/checks/.. = .claude/). Parametrizável para
    permitir testar contra uma cópia sintética fora do kit real (ex.: scratchpad),
    sem nunca escrever dentro do .claude/ real.
#>
[CmdletBinding()]
param(
    [ValidateSet('validate', 'generate', 'check-drift')]
    [string]$Mode = 'validate',

    [string]$KitRoot
)

$ErrorActionPreference = 'Stop'

if (-not $KitRoot) {
    # .claude/checks/kit_check.ps1 -> .claude/
    $KitRoot = Split-Path -Parent $PSScriptRoot
}
$KitRoot = (Resolve-Path -LiteralPath $KitRoot).Path

if ($Mode -ne 'validate') {
    Write-Host "kit_check: modo '$Mode' reservado para V2K-T2 — ainda não implementado nesta tarefa (V2K-T1)."
    exit 1
}

$errors = [System.Collections.Generic.List[string]]::new()

function Get-Frontmatter {
    param([Parameter(Mandatory)][string]$Path)
    $lines = Get-Content -LiteralPath $Path
    if ($lines.Count -lt 2 -or $lines[0].Trim() -ne '---') {
        return $null
    }
    $endIdx = -1
    for ($i = 1; $i -lt $lines.Count; $i++) {
        if ($lines[$i].Trim() -eq '---') { $endIdx = $i; break }
    }
    if ($endIdx -lt 1) { return $null }
    return $lines[1..($endIdx - 1)]
}

function Get-FieldValue {
    param([Parameter(Mandatory)][AllowEmptyCollection()][string[]]$FrontmatterLines, [Parameter(Mandatory)][string]$Field)
    foreach ($line in $FrontmatterLines) {
        if ($line -match "^\s*${Field}\s*:\s*(.*)$") {
            return $Matches[1].Trim()
        }
    }
    return $null
}

# --- 1. Agentes: .claude/agents/*.md -------------------------------------
# Campos exigidos derivados do estado vigente (2026-07-29): todos os 9 agentes
# medidos têm name+description. 'tools' é OPCIONAL porque pantonic-executor.md
# não tem essa linha e o kit atual precisa continuar válido; quando presente,
# só validamos sintaxe (lista separada por vírgula, ou '*'). 'model' também
# fica opcional pelo mesmo motivo — a regra desta tarefa é name+description.
$agentsDir = Join-Path $KitRoot 'agents'
$agentFiles = @(Get-ChildItem -LiteralPath $agentsDir -Filter '*.md' -File -ErrorAction SilentlyContinue)
foreach ($f in $agentFiles) {
    $fm = Get-Frontmatter -Path $f.FullName
    if ($null -eq $fm) {
        $errors.Add("Agente sem frontmatter YAML ('---'...'---'): $($f.FullName)")
        continue
    }
    $name = Get-FieldValue -FrontmatterLines $fm -Field 'name'
    $description = Get-FieldValue -FrontmatterLines $fm -Field 'description'
    if ([string]::IsNullOrWhiteSpace($name)) {
        $errors.Add("Agente sem campo 'name' no frontmatter: $($f.FullName)")
    }
    if ([string]::IsNullOrWhiteSpace($description)) {
        $errors.Add("Agente sem campo 'description' no frontmatter: $($f.FullName)")
    }
    $tools = Get-FieldValue -FrontmatterLines $fm -Field 'tools'
    if (-not [string]::IsNullOrWhiteSpace($tools)) {
        if ($tools -ne '*' -and $tools -notmatch '^[A-Za-z0-9_]+(\s*,\s*[A-Za-z0-9_]+)*$') {
            $errors.Add("Agente com campo 'tools' sintaticamente inválido ('$tools'): $($f.FullName)")
        }
    }
}

# --- 2. Skills: .claude/skills/*/SKILL.md --------------------------------
$skillsDir = Join-Path $KitRoot 'skills'
$skillDirs = @(Get-ChildItem -LiteralPath $skillsDir -Directory -ErrorAction SilentlyContinue)
foreach ($d in $skillDirs) {
    $skillMd = Join-Path $d.FullName 'SKILL.md'
    if (-not (Test-Path -LiteralPath $skillMd)) {
        $errors.Add("Skill sem SKILL.md: $($d.FullName)")
        continue
    }
    $fm = Get-Frontmatter -Path $skillMd
    if ($null -eq $fm) {
        $errors.Add("Skill sem frontmatter YAML ('---'...'---'): $skillMd")
        continue
    }
    $name = Get-FieldValue -FrontmatterLines $fm -Field 'name'
    $description = Get-FieldValue -FrontmatterLines $fm -Field 'description'
    if ([string]::IsNullOrWhiteSpace($name)) {
        $errors.Add("Skill sem campo 'name' no frontmatter: $skillMd")
    }
    elseif ($name -ne $d.Name) {
        $errors.Add("Skill com 'name' ('$name') diferente do nome do diretório ('$($d.Name)'): $skillMd")
    }
    if ([string]::IsNullOrWhiteSpace($description)) {
        $errors.Add("Skill sem campo 'description' no frontmatter: $skillMd")
    }
}

# --- 3. Paridade de versão: VERSION (raiz) == .claude/KIT_VERSION --------
$repoRoot = Split-Path -Parent $KitRoot
$versionFile = Join-Path $repoRoot 'VERSION'
$kitVersionFile = Join-Path $KitRoot 'KIT_VERSION'
$versionSummary = $null
if (-not (Test-Path -LiteralPath $versionFile)) {
    $errors.Add("Arquivo VERSION não encontrado em: $versionFile")
}
elseif (-not (Test-Path -LiteralPath $kitVersionFile)) {
    $errors.Add("Arquivo KIT_VERSION não encontrado em: $kitVersionFile")
}
else {
    $v1 = (Get-Content -LiteralPath $versionFile -Raw).Trim()
    $v2 = (Get-Content -LiteralPath $kitVersionFile -Raw).Trim()
    if ($v1 -ne $v2) {
        $errors.Add("Divergência de versão: VERSION='$v1' vs KIT_VERSION='$v2'")
    }
    else {
        $versionSummary = $v1
    }
}

if ($errors.Count -gt 0) {
    Write-Host "kit_check: FALHOU ($($errors.Count) problema(s))"
    foreach ($e in $errors) {
        Write-Host "  - $e"
    }
    exit 1
}

Write-Host "kit_check: OK - $($agentFiles.Count) agente(s) e $($skillDirs.Count) skill(s) validados; VERSION == KIT_VERSION ('$versionSummary')."
exit 0
