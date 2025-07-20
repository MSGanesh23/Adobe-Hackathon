import fitz  

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)

    headings = []
    font_stats = {} 

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                line_text = ""
                for span in line["spans"]:
                    size = round(span["size"], 1)
                    font_stats[size] = font_stats.get(size, 0) + 1
                    line_text += span["text"].strip()

                if line_text:
                    headings.append({
                        "text": line_text,
                        "size": size,
                        "page": page_num
                    })

    
    size_freq = sorted(font_stats.items(), key=lambda x: -x[0])
    top_sizes = [s[0] for s in size_freq[:3]] 

    
    outline = []
    for h in headings:
        if h["size"] == top_sizes[0]:
            level = "H1"
        elif len(top_sizes) > 1 and h["size"] == top_sizes[1]:
            level = "H2"
        elif len(top_sizes) > 2 and h["size"] == top_sizes[2]:
            level = "H3"
        else:
            continue  

        outline.append({
            "level": level,
            "text": h["text"],
            "page": h["page"]
        })

    
    title = doc.metadata.get("title") or ""
    if not title:
        for h in outline:
            if h["level"] == "H1":
                title = h["text"]
                break
    if not title:
        title = pdf_path.stem

    return {
        "title": title,
        "outline": outline
    }
