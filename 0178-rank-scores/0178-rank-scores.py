import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)
    
    # optional: sort by score descending
    scores = scores.sort_values(by="score", ascending=False)
    
    return scores[["score", "rank"]]