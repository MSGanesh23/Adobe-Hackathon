from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_sections(sections, persona, task, top_k=5):
    
    query = f"{persona}: {task}"

   
    query_embedding = model.encode(query, convert_to_tensor=True)
    section_embeddings = model.encode(sections, convert_to_tensor=True)

    
    similarities = util.cos_sim(query_embedding, section_embeddings)[0]

    
    sorted_indices = similarities.argsort(descending=True)

   
    top_sections = [sections[i] for i in sorted_indices[:top_k]]

    return top_sections
