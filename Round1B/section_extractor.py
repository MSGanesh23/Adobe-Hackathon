import fitz  
from typing import List, Dict
import os


def extract_text_sections(pdf_path: str) -> List[Dict]:
    
    doc = fitz.open(pdf_path)
    sections = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text().strip()

        if text:
            sections.append({
                "document": os.path.basename(pdf_path),
                "page_number": page_num + 1,
                "section_text": text
            })

    doc.close()
    return sections


def extract_sections_from_multiple_pdfs(pdf_paths: List[str]) -> List[Dict]:
    
    all_sections = []

    for path in pdf_paths:
        print(f"[INFO] Extracting from: {path}")
        sections = extract_text_sections(path)
        all_sections.extend(sections)

    print(f"[INFO] Total sections extracted: {len(all_sections)}")
    return all_sections
