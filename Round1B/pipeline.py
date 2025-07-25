import json
from section_extractor import extract_sections_from_multiple_pdfs
from section_ranker import rank_sections
from subsection_analyzer import analyze_subsections


def run_pipeline(persona, task, pdf_paths):
    
    all_sections = extract_sections_from_multiple_pdfs(pdf_paths)

    
    ranked_sections = rank_sections(all_sections, persona, task)

    
    analyzed_subsections = analyze_subsections(ranked_sections, persona, task)

    
    result = {
        "metadata": {
            "persona": persona,
            "job_to_be_done": task,
            "input_documents": pdf_paths,
        },
        "extracted_sections": ranked_sections,
        "subsection_analysis": analyzed_subsections,
    }

    return result
