from pathlib import Path
import re
from PyPDF2 import PdfMerger

def natural_key(path: Path):
    return [int(t) if t.isdigit() else t.lower()
            for t in re.split(r"(\d+)", path.stem)]

folder = Path(".")
out_file = folder / "merged.pdf"

pdfs = [
    p for p in folder.glob("*.pdf")
    if p.resolve() != out_file.resolve()
]

pdfs.sort(key=natural_key)

merger = PdfMerger()

for p in pdfs:
    merger.append(str(p))

with open(out_file, "wb") as f:
    merger.write(f)

merger.close()

print(f"Zusammengefügt: {len(pdfs)} Dateien → {out_file}")


        