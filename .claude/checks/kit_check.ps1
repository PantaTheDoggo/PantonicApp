<#
.SYNOPSIS
    Validador estrutural do kit agêntico Pantonic* (.claude/).

.DESCRIPTION
    V2K-T1/V2K-T2 (docs/plans/P-0729-v2-melhoria-candidatos.md §3, candidato C-01).
    Falha (exit != 0) quando um artefato de extensão do kit está estruturalmente
    inválido, ou quando o `.claude/README.md` versionado diverge do regenerado a
    partir do disco. NÃO interpreta semântica de doutrina — só forma sintática do
    frontmatter YAML, paridade de versão e deriva do índice (ver risco registrado
    na ficha C-01 / BM-14§D9: validar semântica de doutrina é fora de escopo deste
    script; padrão de referência BM-15§D9/BM-07§D8, não BM-14§D9).

.PARAMETER Mode
    'validate' — checagem estrutural (V2K-T1). 'generate' — regenera as tabelas de
    agentes/skills do `.claude/README.md` entre marcadores de região a partir do
    frontmatter em disco. 'check-drift' — regenera em memória e falha se divergir
    do arquivo versionado (não escreve).

.PARAMETER KitRoot
    Raiz do kit (equivalente a .claude/) a validar. Default: resolvida a partir
    do caminho deste script (.claude/checks/.. = .claude/). Parametrizável para
    permitir testar contra uma cópia sintética fora do kit real (ex.: scratchpad),
    sem nunca escrever dentro do .claude/ real.
#>
[CmdletBinding()]
param(
    [ValidateSet('validate', 'generate', 'check-drift', 'consumers')]
    [string]$Mode = 'validate',

    [string]$KitRoot
)

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [Text.Encoding]::UTF8

if (-not $KitRoot) {
    # .claude/checks/kit_check.ps1 -> .claude/
    $KitRoot = Split-Path -Parent $PSScriptRoot
}
$KitRoot = (Resolve-Path -LiteralPath $KitRoot).Path

function Get-AgentsTableMarkdown {
    # Gera as linhas da tabela "Agentes" a partir de .claude/agents/*.md
    # (frontmatter: name/model/description). Ordem determinística (Sort-Object
    # Name) — é o que faz -Mode check-drift significar algo.
    param([Parameter(Mandatory)][string]$KitRoot)
    $agentsDir = Join-Path $KitRoot 'agents'
    $files = @(Get-ChildItem -LiteralPath $agentsDir -Filter '*.md' -File -ErrorAction SilentlyContinue) | Sort-Object Name
    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add('| Agente | Modelo | Papel |')
    $lines.Add('|---|---|---|')
    foreach ($f in $files) {
        $fm = Get-Frontmatter -Path $f.FullName
        $name = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
        $fmName = if ($fm) { Get-FieldValue -FrontmatterLines $fm -Field 'name' } else { $null }
        if (-not [string]::IsNullOrWhiteSpace($fmName)) { $name = $fmName }
        $model = if ($fm) { Get-FieldValue -FrontmatterLines $fm -Field 'model' } else { $null }
        $modelDisplay = if ([string]::IsNullOrWhiteSpace($model)) { '' } else { (Get-Culture).TextInfo.ToTitleCase($model) }
        $description = if ($fm) { Get-FieldValue -FrontmatterLines $fm -Field 'description' } else { '' }
        $lines.Add("| ``$name`` | $modelDisplay | $description |")
    }
    return $lines
}

function Get-SkillsTableMarkdown {
    # Gera as linhas da tabela "Skills" a partir de .claude/skills/*/SKILL.md
    # (frontmatter: description). Ordem determinística (Sort-Object Name).
    param([Parameter(Mandatory)][string]$KitRoot)
    $skillsDir = Join-Path $KitRoot 'skills'
    $dirs = @(Get-ChildItem -LiteralPath $skillsDir -Directory -ErrorAction SilentlyContinue) | Sort-Object Name
    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add('| Skill | Quando usar |')
    $lines.Add('|---|---|')
    foreach ($d in $dirs) {
        $skillMd = Join-Path $d.FullName 'SKILL.md'
        $description = ''
        if (Test-Path -LiteralPath $skillMd) {
            $fm = Get-Frontmatter -Path $skillMd
            if ($fm) { $description = Get-FieldValue -FrontmatterLines $fm -Field 'description' }
        }
        $lines.Add("| ``$($d.Name)`` | $description |")
    }
    return $lines
}

function Set-MarkedRegion {
    # Substitui o conteúdo ENTRE os marcadores por $NewBody; os marcadores em si
    # e tudo fora deles (prosa autoral) são preservados intactos. Falha
    # (throw) se um marcador estiver ausente ou desbalanceado — isso é o que
    # torna -Mode generate seguro contra README sem os marcadores esperados.
    param(
        [Parameter(Mandatory)][AllowEmptyString()][string[]]$Content,
        [Parameter(Mandatory)][string]$BeginMarker,
        [Parameter(Mandatory)][string]$EndMarker,
        [Parameter(Mandatory)][AllowEmptyCollection()][AllowEmptyString()][string[]]$NewBody
    )
    $beginIdx = -1
    $endIdx = -1
    for ($i = 0; $i -lt $Content.Count; $i++) {
        if ($beginIdx -lt 0 -and $Content[$i].Trim() -eq $BeginMarker) { $beginIdx = $i }
        elseif ($Content[$i].Trim() -eq $EndMarker) { $endIdx = $i }
    }
    if ($beginIdx -lt 0) { throw "Marcador de início ausente: '$BeginMarker'" }
    if ($endIdx -lt 0) { throw "Marcador de fim ausente: '$EndMarker'" }
    if ($endIdx -le $beginIdx) { throw "Marcadores desbalanceados ('$BeginMarker' ... '$EndMarker')" }
    $result = [System.Collections.Generic.List[string]]::new()
    $result.AddRange([string[]]$Content[0..$beginIdx])
    $result.AddRange([string[]]$NewBody)
    $result.AddRange([string[]]$Content[$endIdx..($Content.Count - 1)])
    return $result.ToArray()
}

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

if ($Mode -eq 'validate') {

$errors = [System.Collections.Generic.List[string]]::new()

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

# --- 2b. Frontmatter é YAML válido --------------------------------------
# TK-77a (`docs/DIARIO_DE_OBRAS.md` `### TK-77a`) — o frontmatter de agente ou skill que o YAML
# estrito (`yaml.safe_load`) recusa também é motivo de falha aqui, mesma classe nas duas
# famílias (o leitor de frontmatter acima, `Get-Frontmatter`, é um só para as duas).
$frontmatterYamlScript = Join-Path $KitRoot 'checks/frontmatter_yaml.py'
$frontmatterYamlTargets = [System.Collections.Generic.List[string]]::new()
foreach ($f in $agentFiles) { $frontmatterYamlTargets.Add($f.FullName) }
foreach ($d in $skillDirs) {
    $skillMd = Join-Path $d.FullName 'SKILL.md'
    if (Test-Path -LiteralPath $skillMd) { $frontmatterYamlTargets.Add($skillMd) }
}
$frontmatterYamlOutput = @(& python $frontmatterYamlScript @frontmatterYamlTargets 2>&1)
$frontmatterYamlExit = $LASTEXITCODE
if ($frontmatterYamlExit -eq 1) {
    foreach ($line in $frontmatterYamlOutput) {
        $errors.Add("frontmatter YAML: $line")
    }
}
elseif ($frontmatterYamlExit -ne 0) {
    $errors.Add("frontmatter YAML: saida nao interpretavel (exit $frontmatterYamlExit): $($frontmatterYamlOutput -join ' | ')")
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

# --- 4. Materialização: canônico (projecoes.json) -> settings.json alvo --
# RPC-T3 (docs/plans/P-0735-residencia-e-ponto-de-carga.md §T3). A régua deixa
# de depender de disciplina: cobra que o canônico declarado em projecoes.json
# seja válido para os dois alvos (leitura pura, segura em qualquer máquina —
# 'check' não olha o disco do alvo, só a forma do manifesto).
$materializarScript = Join-Path $KitRoot 'tools/materializar.py'
$materializarCheckOutput = @(& python $materializarScript check --alvo todos --kit-root $KitRoot 2>&1)
$materializarCheckExit = $LASTEXITCODE
if ($materializarCheckExit -eq 1) {
    foreach ($line in $materializarCheckOutput) {
        if ($line -match '^materializar: FALHOU - ') { continue }
        $errors.Add("materializar check: $line")
    }
}
elseif ($materializarCheckExit -ne 0) {
    $errors.Add("materializar check: saida nao interpretavel (exit $materializarCheckExit): $($materializarCheckOutput -join ' | ')")
}

$canonicalEntryCount = 0
$projecoesPath = Join-Path $KitRoot 'projecoes.json'
if (Test-Path -LiteralPath $projecoesPath) {
    $projecoes = Get-Content -LiteralPath $projecoesPath -Raw | ConvertFrom-Json
    foreach ($alvoProp in $projecoes.alvos.PSObject.Properties) {
        $alvo = $alvoProp.Value
        if ($alvo.chaves -and $alvo.chaves.hooks) {
            foreach ($eventProp in $alvo.chaves.hooks.PSObject.Properties) {
                $canonicalEntryCount += @($eventProp.Value).Count
            }
        }
        if ($alvo.arquivos) {
            $canonicalEntryCount += @($alvo.arquivos).Count
        }
    }
}

if ($errors.Count -gt 0) {
    Write-Host "kit_check: FALHOU ($($errors.Count) problema(s))"
    foreach ($e in $errors) {
        Write-Host "  - $e"
    }
    exit 1
}

Write-Host "kit_check: OK - $($agentFiles.Count) agente(s), $($skillDirs.Count) skill(s) e $canonicalEntryCount entrada(s) canonica(s) validados; VERSION == KIT_VERSION ('$versionSummary')."
exit 0

}
elseif ($Mode -eq 'generate') {
    $readmePath = Join-Path $KitRoot 'README.md'
    if (-not (Test-Path -LiteralPath $readmePath)) {
        Write-Host "kit_check: generate FALHOU - README.md não encontrado em: $readmePath"
        exit 1
    }
    $content = @(Get-Content -LiteralPath $readmePath)
    $agentsBody = Get-AgentsTableMarkdown -KitRoot $KitRoot
    $skillsBody = Get-SkillsTableMarkdown -KitRoot $KitRoot
    try {
        $content = Set-MarkedRegion -Content $content -BeginMarker '<!-- kit:agents:begin -->' -EndMarker '<!-- kit:agents:end -->' -NewBody $agentsBody
        $content = Set-MarkedRegion -Content $content -BeginMarker '<!-- kit:skills:begin -->' -EndMarker '<!-- kit:skills:end -->' -NewBody $skillsBody
    }
    catch {
        Write-Host "kit_check: generate FALHOU - $($_.Exception.Message)"
        exit 1
    }
    Set-Content -LiteralPath $readmePath -Value $content -Encoding utf8NoBOM
    Write-Host "kit_check: generate OK - README.md regenerado: $($agentsBody.Count - 2) agente(s), $($skillsBody.Count - 2) skill(s)."
    exit 0
}
elseif ($Mode -eq 'check-drift') {
    $driftErrors = [System.Collections.Generic.List[string]]::new()
    # Linhas de detalhe só para exibição — não entram na contagem de problemas
    # (EBK-T5, docs/plans/P-0751-esgotar-backlog.md): uma divergência de README
    # com N linhas diferentes conta 1 problema, não N+1.
    $driftDetailLines = [System.Collections.Generic.List[string]]::new()
    $readmePath = Join-Path $KitRoot 'README.md'
    if (-not (Test-Path -LiteralPath $readmePath)) {
        Write-Host "kit_check: check-drift FALHOU - README.md não encontrado em: $readmePath"
        exit 1
    }
    $current = @(Get-Content -LiteralPath $readmePath)
    $agentsBody = Get-AgentsTableMarkdown -KitRoot $KitRoot
    $skillsBody = Get-SkillsTableMarkdown -KitRoot $KitRoot
    try {
        $regenerated = Set-MarkedRegion -Content $current -BeginMarker '<!-- kit:agents:begin -->' -EndMarker '<!-- kit:agents:end -->' -NewBody $agentsBody
        $regenerated = Set-MarkedRegion -Content $regenerated -BeginMarker '<!-- kit:skills:begin -->' -EndMarker '<!-- kit:skills:end -->' -NewBody $skillsBody
    }
    catch {
        Write-Host "kit_check: check-drift FALHOU - $($_.Exception.Message)"
        exit 1
    }
    $diff = Compare-Object -ReferenceObject $current -DifferenceObject $regenerated
    if ($diff) {
        $driftErrors.Add("README.md diverge do regenerado ($($diff.Count) linha(s) diferente(s)):")
        foreach ($d in $diff) {
            $side = if ($d.SideIndicator -eq '<=') { 'versionado' } else { 'regenerado' }
            $driftDetailLines.Add("    [$side] $($d.InputObject)")
        }
    }

    # --- Materialização (RPC-T3): destino do alvo 'projeto' == canônico -----
    # Alvo 'usuario' fica fora (DL-4): cobrar a projeção da máquina de quem
    # executa quebraria consumidor que não optou por ela.
    $materializarScript = Join-Path $KitRoot 'tools/materializar.py'
    $materializarDriftOutput = @(& python $materializarScript drift --alvo projeto --kit-root $KitRoot 2>&1)
    $materializarDriftExit = $LASTEXITCODE
    if ($materializarDriftExit -eq 1) {
        foreach ($line in $materializarDriftOutput) {
            if ($line -match '^materializar: FALHOU - ') { continue }
            $driftErrors.Add("materializar drift: $line")
        }
    }
    elseif ($materializarDriftExit -ne 0) {
        $driftErrors.Add("materializar drift: saida nao interpretavel (exit $materializarDriftExit): $($materializarDriftOutput -join ' | ')")
    }

    if ($driftErrors.Count -gt 0) {
        Write-Host "kit_check: check-drift FALHOU ($($driftErrors.Count) problema(s)):"
        for ($i = 0; $i -lt $driftErrors.Count; $i++) {
            Write-Host "  - $($driftErrors[$i])"
            if ($i -eq 0 -and $driftDetailLines.Count -gt 0) {
                foreach ($d in $driftDetailLines) {
                    Write-Host $d
                }
            }
        }
        exit 1
    }
    Write-Host "kit_check: check-drift OK - .claude/README.md == regenerado ($($agentsBody.Count - 2) agente(s), $($skillsBody.Count - 2) skill(s)); materializacao do alvo 'projeto' == canonico."
    exit 0
}
elseif ($Mode -eq 'consumers') {
    # V2K-T12b (docs/plans/P-0729-v2-melhoria-candidatos.md §T12, C-09, metade
    # consumidora). Deriva por máquina as 3 colunas de docs/CONSUMIDORES.md a
    # partir do carimbo SYNC_STATE (V2K-T12a) que cada consumidor grava em
    # .claude/kit/ a cada sync efetivo. Coluna 'Consumidor' é a única entrada
    # mantida à mão; caminho sem carimbo (inclusive inexistente) preserva a
    # linha semeada intacta — nunca apaga nem inventa versão.
    $repoRoot = Split-Path -Parent $KitRoot
    $consumidoresPath = Join-Path $repoRoot 'docs/CONSUMIDORES.md'
    if (-not (Test-Path -LiteralPath $consumidoresPath)) {
        Write-Host "kit_check: consumers FALHOU - docs/CONSUMIDORES.md não encontrado em: $consumidoresPath"
        exit 1
    }
    $lines = @(Get-Content -LiteralPath $consumidoresPath)
    $headerIdx = -1
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i].Trim() -eq '| Consumidor | Versão instalada | Último sync | Modo |') { $headerIdx = $i; break }
    }
    if ($headerIdx -lt 0) {
        Write-Host "kit_check: consumers FALHOU - cabeçalho da tabela não encontrado em: $consumidoresPath"
        exit 1
    }
    $dataStart = $headerIdx + 2
    $dataEnd = $dataStart
    while ($dataEnd -lt $lines.Count -and $lines[$dataEnd].TrimStart().StartsWith('|')) {
        $dataEnd++
    }
    $updated = 0
    $seeded = 0
    $newLines = [System.Collections.Generic.List[string]]::new()
    $newLines.AddRange([string[]]$lines[0..($dataStart - 1)])
    for ($i = $dataStart; $i -lt $dataEnd; $i++) {
        $row = $lines[$i]
        $cols = $row.Split('|')
        $consumidorPath = $cols[1].Trim()
        $syncStatePath = Join-Path $consumidorPath '.claude/kit/SYNC_STATE'
        if (Test-Path -LiteralPath $syncStatePath) {
            $kv = @{}
            foreach ($l in @(Get-Content -LiteralPath $syncStatePath)) {
                if ($l -match '^\s*([A-Za-z_]+)\s*=\s*(.*)$') { $kv[$Matches[1]] = $Matches[2].Trim() }
            }
            $version = if ($kv.ContainsKey('version')) { $kv['version'] } else { 'unknown' }
            $syncedAt = if ($kv.ContainsKey('synced_at')) { $kv['synced_at'] } else { 'unknown' }
            $syncMode = if ($kv.ContainsKey('mode')) { $kv['mode'] } else { 'unknown' }
            $newLines.Add("| $consumidorPath | $version | $syncedAt | $syncMode |")
            $updated++
        }
        else {
            $newLines.Add($row)
            $seeded++
        }
    }
    if ($dataEnd -lt $lines.Count) {
        $newLines.AddRange([string[]]$lines[$dataEnd..($lines.Count - 1)])
    }
    if ($updated -gt 0) {
        Set-Content -LiteralPath $consumidoresPath -Value $newLines.ToArray() -Encoding utf8NoBOM
    }
    Write-Host "kit_check: consumers OK - $updated atualizado(s) por carimbo, $seeded permanece(m) semeado(s)."
    exit 0
}
