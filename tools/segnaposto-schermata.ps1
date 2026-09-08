param(
    [string]$Titolo,
    [string]$Testata,
    [string[]]$Tabs,
    [string]$Out
)

Add-Type -AssemblyName System.Drawing

$CanvasW = 1200
$CanvasH = 760
$bmp = New-Object System.Drawing.Bitmap($CanvasW, $CanvasH)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = 'AntiAlias'
$g.TextRenderingHint = 'ClearTypeGridFit'

$white   = [System.Drawing.Color]::FromArgb(255, 255, 255)
$indigo  = [System.Drawing.Color]::FromArgb(63, 78, 173)
$boxFill = [System.Drawing.Color]::FromArgb(244, 245, 247)
$boxEdge = [System.Drawing.Color]::FromArgb(176, 183, 190)
$ink     = [System.Drawing.Color]::FromArgb(60, 66, 74)
$faint   = [System.Drawing.Color]::FromArgb(150, 157, 165)

$g.Clear($white)

$brFill = New-Object System.Drawing.SolidBrush($boxFill)
$brInk  = New-Object System.Drawing.SolidBrush($ink)
$brF    = New-Object System.Drawing.SolidBrush($faint)
$brW    = New-Object System.Drawing.SolidBrush($white)
$brInd  = New-Object System.Drawing.SolidBrush($indigo)
$pen    = New-Object System.Drawing.Pen($boxEdge, 1)

$fTitle = New-Object System.Drawing.Font('Segoe UI', 10)
$fBox   = New-Object System.Drawing.Font('Segoe UI', 9)
$fTab   = New-Object System.Drawing.Font('Segoe UI', 8)

$g.FillRectangle($brInd, 0, 0, $CanvasW, 46)
$g.DrawString($Titolo, $fTitle, $brW, 16, 14)

function Box($bx, $by, $bw, $bh, $label) {
    $g.FillRectangle($brFill, $bx, $by, $bw, $bh)
    $g.DrawRectangle($pen, $bx, $by, $bw, $bh)
    if ($label) { $g.DrawString($label, $fBox, $brInk, ($bx + 12), ($by + 10)) }
}

Box 16 58 1168 44 'Barra dei comandi'
Box 16 114 1168 62 $Testata

# linguette, su piu' righe se non entrano
$tabX = 16
$tabY = 188
foreach ($t in $Tabs) {
    $tabW = [int]$g.MeasureString($t, $fTab).Width + 14
    if (($tabX + $tabW) -gt 1184) { $tabX = 16; $tabY += 26 }
    $g.FillRectangle($brFill, $tabX, $tabY, $tabW, 24)
    $g.DrawRectangle($pen, $tabX, $tabY, $tabW, 24)
    $g.DrawString($t, $fTab, $brInk, ($tabX + 7), ($tabY + 5))
    $tabX += $tabW + 2
}

$bodyY = $tabY + 24
$bodyH = 744 - $bodyY
Box 16 $bodyY 1168 $bodyH $null
$msg = 'SEGNAPOSTO - sostituire con lo screenshot reale'
$sz = $g.MeasureString($msg, $fBox)
$g.DrawString($msg, $fBox, $brF, (($CanvasW - $sz.Width) / 2), ($bodyY + ($bodyH - $sz.Height) / 2))

# System.Drawing risolve i percorsi relativi sulla cartella del processo, non su
# quella di PowerShell: senza questo l'immagine finisce altrove o il Save fallisce.
$dest = [System.IO.Path]::GetFullPath((Join-Path (Get-Location).Path $Out))
$cartella = Split-Path $dest -Parent
if (-not (Test-Path $cartella)) { New-Item -ItemType Directory -Force $cartella | Out-Null }

try {
    $bmp.Save($dest, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Output "scritto $dest"
}
finally {
    $g.Dispose()
    $bmp.Dispose()
}
