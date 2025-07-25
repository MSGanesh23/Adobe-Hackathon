

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def refine_sections(sections):
    
    results = []
    for section in sections:
        text = section["text"]
        if len(text.split()) < 50:
            summary = text  
        else:
            summary = summarizer(text, max_length=200, min_length=60, do_sample=False)[0]["summary_text"]

        results.append({
            "document": section["document"],
            "page_number": section["page_number"],
            "refined_text": summary.strip()
        })
    return results
