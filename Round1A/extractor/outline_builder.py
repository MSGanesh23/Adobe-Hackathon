
from pathlib import Path
from .parse_pdf import parse_pdf
from .heading_detector import detect_headings
from .level_infer import infer_levels


def _guess_title(pages):
    
    first_page_spans = pages[0] if pages else []
    if not first_page_spans:
        return ""

    largest = max(first_page_spans, key=lambda s: s["size"])
    return largest["text"].strip()


def extract_outline(pdf_path: Path):
    
    pages = parse_pdf(pdf_path)
    raw_heads = detect_headings(pages)
    heads = infer_levels(raw_heads)

    outline = [
        {"level": h["level"], "text": h["text"], "page": h["page"]}
        for h in sorted(heads, key=lambda x: (x["page"], x["y0"]))
    ]

    return {
        "title": _guess_title(pages),
        "outline": outline,
    }
