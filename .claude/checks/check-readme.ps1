<#
.SYNOPSIS
    Guarda executável de drift do README canônico.

.DESCRIPTION
    O `README.md` da raiz é o contrato entre o framework e quem o adota: o espelho das
    implementações, escrito para que se possa argumentar sobre as práticas (o que é / por quê /
    onde o gerente intervém) sem abrir skill, agente e hook um a um. Um espelho sem guarda nasce
    fiel e envelhece mentindo — com autoridade, porque é o único arquivo lido. Este script falha
    (exit != 0) quando o README diverge do disco/doutrina em qualquer uma das 5 checagens mecânicas
    abaixo; zero julgamento de conteúdo, só forma e paridade de números.

    As seções são localizadas pelo TÍTULO, não pelo número — o número muda a cada reescrita do
    esqueleto do espelho e não é contrato.

    1. Todo agente `.claude/agents/*.md` aparece na tabela de Agentes da seção "Anatomia do kit"
       do README, e vice-versa.
    2. Toda skill `.claude/skills/*/SKILL.md` aparece na tabela de Skills da mesma seção, e
       vice-versa.
    3. A versão citada no README (cabeçalho + linha "Versão vigente do framework:") é igual a
       `VERSION` e a `.claude/KIT_VERSION`, e os quatro coincidem entre si.
    4. O número de guardrails da tabela da seção "Os guardrails" do README é igual ao número de
       itens da lista numerada de `GOVERNANCA.md` §7 ("## 7. Guardrails dos agentes" até "### 7.1").
    5. Toda seção `## ` do README tem a linha `> Fonte da verdade:` e o arquivo citado nela existe.

.PARAMETER Root
    Raiz do repositório a checar (onde `README.md`, `VERSION` e `GOVERNANCA.md` vivem). Default:
    resolvida a partir do caminho deste script (.claude/checks/../.. = raiz do repo). Parametrizável
    para permitir provar o guarda contra uma fixture sintética fora do repo real (ex.: scratchpad),
    sem nunca escrever no repo real — mesmo desenho de `-KitRoot` (`kit_check.ps1`) e `--root`
    (`dead_code.py`, `ratchet_piso.py`).
#>
[CmdletBinding()]
param(
    [string]$Root
)

$ErrorActionPreference = 'Stop'

if (-not $Root) {
    # .claude/checks/check-readme.ps1 -> .claude -> raiz do repo
    $Root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
}
$Root = (Resolve-Path -LiteralPath $Root).Path

$errors = [System.Collections.Generic.List[string]]::new()

$readmePath = Join-Path $Root 'README.md'
if (-not (Test-Path -LiteralPath $readmePath)) {
    Write-Host "check-readme: FALHOU - README.md não encontrado em: $readmePath"
    exit 1
}
$lines = @(Get-Content -LiteralPath $readmePath)

# --- Seções: índices dos headings "## N. " ---------------------------------
$headingIdx = [System.Collections.Generic.List[int]]::new()
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^## (\d+)\. ') { $headingIdx.Add($i) }
}

function Get-SectionLines {
    # [AllowEmptyString()] é necessário porque $Lines contém linhas em branco do README
    # (elemento "" no array) — sem ele, o binder de parâmetro Mandatory rejeita o array
    # inteiro (mesmo padrão já resolvido em kit_check.ps1 Set-MarkedRegion -NewBody).
    param(
        [Parameter(Mandatory)][AllowEmptyString()][string[]]$Lines,
        [Parameter(Mandatory)][System.Collections.Generic.List[int]]$HeadingIdx,
        [Parameter(Mandatory)][int]$Index
    )
    $start = $HeadingIdx[$Index]
    $end = if ($Index + 1 -lt $HeadingIdx.Count) { $HeadingIdx[$Index + 1] - 1 } else { $Lines.Count - 1 }
    return $Lines[$start..$end]
}

# --- 1/2. Agentes e Skills: localizar a seção "Anatomia do kit" pelo TÍTULO -
$secKitIdx = -1
for ($i = 0; $i -lt $headingIdx.Count; $i++) {
    if ($lines[$headingIdx[$i]] -match '^## \d+\. Anatomia do kit') { $secKitIdx = $i; break }
}
if ($secKitIdx -lt 0) {
    $errors.Add("Seção 'Anatomia do kit' não encontrada no README (heading '## <N>. Anatomia do kit').")
}
else {
    $secKit = Get-SectionLines -Lines $lines -HeadingIdx $headingIdx -Index $secKitIdx

    $agentesHdr = -1
    $skillsHdr = -1
    for ($i = 0; $i -lt $secKit.Count; $i++) {
        if ($secKit[$i].Trim() -eq '**Agentes**' -and $agentesHdr -lt 0) { $agentesHdr = $i }
        if ($secKit[$i].Trim() -eq '**Skills**' -and $skillsHdr -lt 0) { $skillsHdr = $i }
    }
    if ($agentesHdr -lt 0 -or $skillsHdr -lt 0 -or $skillsHdr -le $agentesHdr) {
        $errors.Add("Marcadores '**Agentes**'/'**Skills**' ausentes ou fora de ordem na seção 'Anatomia do kit'.")
    }
    else {
        $agentRows = $secKit[($agentesHdr + 1)..($skillsHdr - 1)]
        $skillRows = $secKit[($skillsHdr + 1)..($secKit.Count - 1)]

        $readmeAgents = [System.Collections.Generic.List[string]]::new()
        foreach ($row in $agentRows) {
            if ($row -match '^\|\s*`([^`]+)`\s*\|') { $readmeAgents.Add($Matches[1]) }
        }
        $readmeSkills = [System.Collections.Generic.List[string]]::new()
        foreach ($row in $skillRows) {
            if ($row -match '^\|\s*`([^`]+)`\s*\|') { $readmeSkills.Add($Matches[1]) }
        }

        $diskAgents = @(Get-ChildItem -LiteralPath (Join-Path $Root '.claude/agents') -Filter '*.md' -File -ErrorAction SilentlyContinue) |
            ForEach-Object { [System.IO.Path]::GetFileNameWithoutExtension($_.Name) } | Sort-Object
        $diskSkills = @(Get-ChildItem -LiteralPath (Join-Path $Root '.claude/skills') -Directory -ErrorAction SilentlyContinue) |
            Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') } |
            ForEach-Object { $_.Name } | Sort-Object

        $onlyInReadmeAgents = @($readmeAgents | Where-Object { $_ -notin $diskAgents })
        $onlyOnDiskAgents = @($diskAgents | Where-Object { $_ -notin $readmeAgents })
        foreach ($a in $onlyInReadmeAgents) { $errors.Add("Agente na tabela de 'Anatomia do kit' sem arquivo correspondente em .claude/agents/: '$a'") }
        foreach ($a in $onlyOnDiskAgents) { $errors.Add("Agente '$a' (.claude/agents/$a.md) não aparece na tabela de Agentes de 'Anatomia do kit'.") }

        $onlyInReadmeSkills = @($readmeSkills | Where-Object { $_ -notin $diskSkills })
        $onlyOnDiskSkills = @($diskSkills | Where-Object { $_ -notin $readmeSkills })
        foreach ($s in $onlyInReadmeSkills) { $errors.Add("Skill na tabela de 'Anatomia do kit' sem SKILL.md correspondente em .claude/skills/: '$s'") }
        foreach ($s in $onlyOnDiskSkills) { $errors.Add("Skill '$s' (.claude/skills/$s/SKILL.md) não aparece na tabela de Skills de 'Anatomia do kit'.") }
    }
}

# --- 3. Versão: README (cabeçalho + linha vigente) == VERSION == KIT_VERSION
$versionFile = Join-Path $Root 'VERSION'
$kitVersionFile = Join-Path $Root '.claude/KIT_VERSION'
$versions = @{}
if (Test-Path -LiteralPath $versionFile) { $versions['VERSION'] = (Get-Content -LiteralPath $versionFile -Raw).Trim() }
else { $errors.Add("Arquivo VERSION não encontrado em: $versionFile") }
if (Test-Path -LiteralPath $kitVersionFile) { $versions['.claude/KIT_VERSION'] = (Get-Content -LiteralPath $kitVersionFile -Raw).Trim() }
else { $errors.Add("Arquivo .claude/KIT_VERSION não encontrado em: $kitVersionFile") }

$readmeHeaderVersion = $null
$readmeBodyVersion = $null
foreach ($line in $lines) {
    if ($null -eq $readmeHeaderVersion -and $line -match '\*\*Versão do framework:\*\*\s*`([^`]+)`') {
        $readmeHeaderVersion = $Matches[1]
    }
    if ($null -eq $readmeBodyVersion -and $line -match 'Versão vigente do framework:\s*`([^`]+)`') {
        $readmeBodyVersion = $Matches[1]
    }
}
if ($null -eq $readmeHeaderVersion) { $errors.Add("Linha '**Versão do framework:**' não encontrada no cabeçalho do README.") }
else { $versions['README.md (cabeçalho)'] = $readmeHeaderVersion }
if ($null -eq $readmeBodyVersion) { $errors.Add("Linha 'Versão vigente do framework:' não encontrada no corpo do README (seção de distribuição e versão).") }
else { $versions['README.md (corpo)'] = $readmeBodyVersion }

if ($versions.Count -gt 1) {
    $distinctValues = @($versions.Values | Select-Object -Unique)
    if ($distinctValues.Count -gt 1) {
        $detail = ($versions.GetEnumerator() | ForEach-Object { "$($_.Key)='$($_.Value)'" }) -join ', '
        $errors.Add("Divergência de versão entre as fontes: $detail")
    }
}

# --- 4. Guardrails: seção "Os guardrails" ('| N |') == GOVERNANCA.md §7 -----
$secGuardIdx = -1
for ($i = 0; $i -lt $headingIdx.Count; $i++) {
    if ($lines[$headingIdx[$i]] -match '^## \d+\. Os guardrails') { $secGuardIdx = $i; break }
}
if ($secGuardIdx -lt 0) {
    $errors.Add("Seção 'Os guardrails' não encontrada no README (heading '## <N>. Os guardrails').")
    $readmeGuardrailCount = $null
}
else {
    $secGuard = Get-SectionLines -Lines $lines -HeadingIdx $headingIdx -Index $secGuardIdx
    $readmeGuardrailCount = @($secGuard | Where-Object { $_ -match '^\|\s*\d+\s*\|' }).Count
}

$governancaPath = Join-Path $Root 'GOVERNANCA.md'
$governancaGuardrailCount = $null
if (-not (Test-Path -LiteralPath $governancaPath)) {
    $errors.Add("GOVERNANCA.md não encontrado em: $governancaPath")
}
else {
    $govLines = @(Get-Content -LiteralPath $governancaPath)
    $gStart = -1
    $gEnd = -1
    for ($i = 0; $i -lt $govLines.Count; $i++) {
        if ($gStart -lt 0 -and $govLines[$i] -match '^## 7\. Guardrails dos agentes') { $gStart = $i }
        elseif ($gStart -ge 0 -and $govLines[$i] -match '^### 7\.1') { $gEnd = $i; break }
    }
    if ($gStart -lt 0) {
        $errors.Add("Seção '## 7. Guardrails dos agentes' não encontrada em GOVERNANCA.md.")
    }
    elseif ($gEnd -lt 0) {
        $errors.Add("Marcador de fim '### 7.1' não encontrado após '## 7. Guardrails dos agentes' em GOVERNANCA.md.")
    }
    else {
        $govBody = $govLines[$gStart..($gEnd - 1)]
        $governancaGuardrailCount = @($govBody | Where-Object { $_ -match '^\d+\. \*\*' }).Count
    }
}

if ($null -ne $readmeGuardrailCount -and $null -ne $governancaGuardrailCount -and $readmeGuardrailCount -ne $governancaGuardrailCount) {
    $errors.Add("Divergência no número de guardrails: a seção 'Os guardrails' do README tem $readmeGuardrailCount linha(s) vs GOVERNANCA.md §7 com $governancaGuardrailCount item(ns).")
}

# --- 5. Toda seção '## ' tem 'Fonte da verdade' apontando para arquivo real
for ($i = 0; $i -lt $headingIdx.Count; $i++) {
    $title = $lines[$headingIdx[$i]]
    $body = (Get-SectionLines -Lines $lines -HeadingIdx $headingIdx -Index $i) | Select-Object -Skip 1
    $sourcePath = $null
    foreach ($line in $body) {
        if ($line -match '^> Fonte da verdade:\s*`([^`]+)`') { $sourcePath = $Matches[1]; break }
    }
    if ($null -eq $sourcePath) {
        $errors.Add("Seção '$title' sem linha '> Fonte da verdade:'.")
        continue
    }
    $sourceFull = Join-Path $Root $sourcePath
    if (-not (Test-Path -LiteralPath $sourceFull)) {
        $errors.Add("Seção '$title': fonte da verdade aponta para arquivo inexistente: '$sourcePath'")
    }
}

# --- Veredito ----------------------------------------------------------------
if ($errors.Count -gt 0) {
    Write-Host "check-readme: FALHOU ($($errors.Count) problema(s))"
    foreach ($e in $errors) {
        Write-Host "  - $e"
    }
    exit 1
}

$agentCount = if ($diskAgents) { $diskAgents.Count } else { 0 }
$skillCount = if ($diskSkills) { $diskSkills.Count } else { 0 }
Write-Host "check-readme: OK - $agentCount agente(s), $skillCount skill(s), $readmeGuardrailCount guardrail(s), versão '$($versions['VERSION'])', $($headingIdx.Count) seção(ões) com Fonte da verdade válida."
exit 0
