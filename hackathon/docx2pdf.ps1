# Convert a Word file to PDF with the installed Word application and print the page of each heading.
param([string]$In,[string]$Out)
$ErrorActionPreference = "Stop"
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
  $doc = $word.Documents.Open($In, $false, $true)
  $doc.ExportAsFixedFormat($Out, 17)
  Write-Output ("total_pages=" + $doc.ComputeStatistics(2))
  foreach ($p in $doc.Paragraphs) {
    $name = [string]$p.Style.NameLocal
    if ($name -like "Heading*") {
      $t = $p.Range.Text.Trim()
      if ($t.Length -gt 60) { $t = $t.Substring(0, 60) }
      Write-Output ("page " + $p.Range.Information(3) + " y=" + [int]$p.Range.Information(6) + "pt: " + $t)
    }
  }
  $doc.Close($false)
} finally { $word.Quit() }
