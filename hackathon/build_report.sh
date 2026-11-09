#!/usr/bin/env bash
# Build REPORT.docx (official Swarm Alignment template) and REPORT.pdf (Word on the Windows host).
# Usage: bash projects/critical-infrastructure-research/hackathon/build_report.sh
# Edit REPORT.md only. REPORT.numbered.md is generated. If sections/tension.md changes, run merge_tension.py first.
set -euo pipefail
REPO=/home/sammatuba/projects/ps/ai-safety
H=$REPO/projects/critical-infrastructure-research/hackathon
TEMPLATE=$REPO/sources/swarm-template/swarm-alignment-template-2026-11-09.docx
cd "$REPO"
python3 "$H/number_citations.py"
python3 tools/md2apart.py --template "$TEMPLATE" --report "$H/REPORT.numbered.md" --out "$H/REPORT.docx"
python3 "$H/postprocess_docx.py" "$H/REPORT.docx"
WIN_TMP=$(powershell.exe -NoProfile -Command 'Write-Output $env:TEMP' | tr -d '\r')
WT=$(wslpath -u "$WIN_TMP")/swarm-build
mkdir -p "$WT"
rm -f "$WT/REPORT.pdf"
cp "$H/REPORT.docx" "$H/docx2pdf.ps1" "$WT/"
timeout 180 powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$WIN_TMP\\swarm-build\\docx2pdf.ps1" \
  -In "$WIN_TMP\\swarm-build\\REPORT.docx" -Out "$WIN_TMP\\swarm-build\\REPORT.pdf" | tr -d '\r'
cp "$WT/REPORT.pdf" "$H/REPORT.pdf"
ls -la "$H/REPORT.pdf"
grep -c '\[\[RESULT' "$H/REPORT.md" | sed 's/^/lines with RESULT placeholders: /' || true
