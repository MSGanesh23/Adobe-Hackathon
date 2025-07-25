

from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def analyze_subsections(ranked_sections, persona, task):
    
    analyzed_subsections = []

    persona_context = f"{persona}: {task}"

    for section in ranked_sections:
        section_text = section["section_text"]

        
        truncated_text = section_text[:3000]

        try:
            summary = summarizer(truncated_text, max_length=200, min_length=30, do_sample=False)[0]["summary_text"]
        except Exception as e:
            logger.warning(f"Summarization failed for section {section['document']} page {section['page_number']}: {e}")
            summary = truncated_text[:200] + "..."

        analyzed_subsections.append({
            "refined_text": summary,
            "document": section["document"],
            "page_number": section["page_number"],
            "persona_task_context": persona_context
        })

    return analyzed_subsections
