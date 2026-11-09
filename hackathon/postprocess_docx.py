"""Post-process REPORT.docx: drop the template's "With / Apart Research" line and
shrink the event line and the title footnote. Usage: python3 postprocess_docx.py REPORT.docx"""
import re, shutil, sys, zipfile

path = sys.argv[1]
src = zipfile.ZipFile(path)
out = zipfile.ZipFile(path + ".tmp", "w", zipfile.ZIP_DEFLATED)
for item in src.infolist():
    data = src.read(item.filename)
    if item.filename == "word/document.xml":
        d = data.decode("utf-8")
        i = d.find(">With<")
        if i != -1:
            start = max(d.rfind("<w:p>", 0, i), d.rfind("<w:p ", 0, i))
            end = d.find("</w:p>", i) + len("</w:p>")
            para = d[start:end]
            assert "Apart Research" in para and para.count("<w:p ") + para.count("<w:p>") == 1
            d = d[:start] + d[end:]
        j = d.find("Apart Research Swarm Alignment Hackathon")
        if j != -1:
            start = max(d.rfind("<w:p>", 0, j), d.rfind("<w:p ", 0, j))
            end = d.find("</w:p>", j) + len("</w:p>")
            para = re.sub(r"(<w:r>\s*<w:rPr>)", r'\1<w:sz w:val="17"/><w:szCs w:val="17"/>', d[start:end])
            d = d[:start] + para + d[end:]
        data = d.encode("utf-8")
    elif item.filename == "word/footnotes.xml":
        f = data.decode("utf-8")
        f = f.replace('<w:sz w:val="20"/>', '<w:sz w:val="16"/>').replace('<w:szCs w:val="20"/>', '<w:szCs w:val="16"/>')
        data = f.encode("utf-8")
    out.writestr(item, data)
out.close(); src.close()
shutil.move(path + ".tmp", path)
