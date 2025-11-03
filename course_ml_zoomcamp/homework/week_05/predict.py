import pickle
from typing import Any, Dict, List

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="lead-score-service")

# --------- Pydantic schema ---------
class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float


# --------- Load artifacts ---------
with open("pipeline_v1.bin", "rb") as f_in:
    dv, model = pickle.load(f_in)   # dv is DictVectorizer, model is trained classifier


# --------- Core scoring helper ---------
def lead_score_from_dict(payload: Dict[str, Any]) -> float:
    """
    Take a single lead (dict) and return the probability
    of getting a subscription (class 1).
    """
    # DictVectorizer expects a list of dicts
    X = dv.transform([payload])

    # Most scikit-learn classifiers used in the course have predict_proba
    proba = model.predict_proba(X)[0, 1]

    # Make sure it's a plain float (not numpy type) so it’s JSON-serializable
    return float(proba)


# --------- FastAPI endpoints ---------
@app.post("/predict")
def predict(lead: Lead) -> Dict[str, float]:
    """
    Predict subscription probability for a given lead.
    """
    proba = lead_score_from_dict(lead.dict())
    return {"subscription_probability": proba}


@app.get("/features")
def features() -> Dict[str, List[str]]:
    """
    Introspect the vectorizer to see what feature names it knows.
    Useful for exploring when you 'don't know the features'.
    """
    names = (
        dv.get_feature_names_out().tolist()
        if hasattr(dv, "get_feature_names_out")
        else dv.feature_names_
    )
    return {"feature_names": names}


if __name__ == "__main__":
    # Option 1: run `python predict.py`
    uvicorn.run(app, host="0.0.0.0", port=9696)
