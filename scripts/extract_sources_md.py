from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw"
OUT_DIR = ROOT / "sources_md"


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "document"


def clean_text(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    cleaned: list[str] = []
    blank = False
    for line in lines:
        stripped = " ".join(line.split())
        if not stripped:
            if not blank:
                cleaned.append("")
            blank = True
            continue
        cleaned.append(stripped)
        blank = False
    return "\n".join(cleaned).strip()


def infer_title(text: str, source_path: Path) -> str:
    for line in text.splitlines():
        candidate = " ".join(line.split()).strip()
        if len(candidate) >= 12:
            return candidate
    return source_path.stem.replace("-", " ").title()


def build_markdown(source_path: Path) -> str:
    reader = PdfReader(str(source_path))
    pages: list[str] = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    raw_text = "\n\n".join(pages)
    cleaned = clean_text(raw_text)
    title = infer_title(cleaned, source_path)
    doc_type = source_path.parent.name.rstrip("s")
    rel_source = source_path.relative_to(ROOT)
    return (
        f"# {title}\n\n"
        f"- Source file: `{rel_source}`\n"
        f"- Document type: `{doc_type}`\n\n"
        "## Extracted Text\n\n"
        f"{cleaned}\n"
    )


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    for pdf_path in sorted(RAW_DIR.rglob("*.pdf")):
        category_dir = OUT_DIR / pdf_path.parent.name
        category_dir.mkdir(parents=True, exist_ok=True)
        output_path = category_dir / f"{slugify(pdf_path.stem)}.md"
        output_path.write_text(build_markdown(pdf_path), encoding="utf-8")
        print(f"Wrote {output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
