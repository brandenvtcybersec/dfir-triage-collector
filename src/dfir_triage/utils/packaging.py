from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


def zip_dir(src_dir: Path, out_zip: Path) -> None:
    with ZipFile(out_zip, "w", compression=ZIP_DEFLATED) as z:
        for p in src_dir.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(src_dir))
