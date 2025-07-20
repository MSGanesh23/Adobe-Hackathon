

from sentence_transformers import SentenceTransformer, util
import statistics as _st


_MINILM = SentenceTransformer("all-MiniLM-L6-v2")


_KEYWORDS = [
    "abstract", "introduction", "background", "method", "methods",
    "related work", "results", "discussion", "conclusion", "references",
    "acknowledgments", "summary",
]
_KEY_EMB = _MINILM.encode(_KEYWORDS, convert_to_tensor=True)


def _layout_filter(span, median_size):
    
    short = len(span["text"].split()) <= 12
    big   = span["size"] >= median_size * 1.15
    bold  = span["bold"]
    return short and (big or bold)


def _semantic_score(text):
    
    emb = _MINILM.encode(text, convert_to_tensor=True)
    return float(util.cos_sim(emb, _KEY_EMB).max())


def detect_headings(pages, min_semantic=0.35):
    
    candidates = []

    for spans in pages:
        if not spans:
            continue
        median_size = _st.median(s["size"] for s in spans)
        for span in spans:
            if not _layout_filter(span, median_size):
                continue
            score = _semantic_score(span["text"])
            if score >= min_semantic:
                candidates.append({**span, "semantic_score": score})

    return candidates
