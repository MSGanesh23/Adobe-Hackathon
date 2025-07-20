
def infer_levels(candidates):
   
    if not candidates:
        return []

    
    sizes = sorted(
        {round(c["size"], 1) for c in candidates}, reverse=True
    )[:3]  

    
    size_to_level = {}
    levels = ["H1", "H2", "H3"]
    for lvl, sz in zip(levels, sizes):
        size_to_level[sz] = lvl

    
    for c in candidates:
        c["level"] = size_to_level.get(round(c["size"], 1), "H3") 

    return candidates
