

import fitz  


def parse_pdf(path):
    
    doc = fitz.open(path)
    pages = []

    for pno in range(len(doc)):
        page = doc.load_page(pno)
        spans = []

        
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue
                    font_name = span.get("font", "")
                    spans.append(
                        {
                            "text": text,
                            "size": span.get("size", 0),
                            "bold": "Bold" in font_name,
                            "italic": ("Italic" in font_name) or ("Oblique" in font_name),
                            "x0": span["bbox"][0],
                            "y0": span["bbox"][1],
                            "page": pno + 1,
                        }
                    )
        pages.append(spans)

    doc.close()
    return pages
