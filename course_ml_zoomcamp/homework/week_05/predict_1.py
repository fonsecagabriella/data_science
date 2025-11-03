import pickle
from typing import Any, Dict, List

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="lead-score-service")

# -------- Load artifacts --------
with open("pipeline_v1.bin", "rb") as f_in:
    dv, model = pickle.load(f_in)   # dv is a DictVectorizer (fit), model is trained

# -------- Core scoring helper --------
def lead_score_from_dict(payload: Dict[str, Any]) -> float:
    """
    Accepts a free-form dict of lead attributes.
    Unknown keys are ignored by DictVectorizer; missing keys become zeros.
    Returns a probability-like score in [0, 1].
    """
    X = dv.transform([payload])  # DictVectorizer expects a list of dicts

    if hasattr(model, "predict_proba"):
        score = float(model.predict_proba(X)[0, 1])
    elif hasattr(model, "decision_function"):
        raw = float(model.decision_function(X)[0])
        score = 1.0 / (1.0 + np.exp(-raw))  # map margin → [0,1]
    else:
        # Some regressors output a number; clip to [0, 1] to act as a score
        score = float(model.predict(X)[0])
        score = float(np.clip(score, 0.0, 1.0))

    return score

# -------- Response model --------
class PredictResponse(BaseModel):
    lead_score: float
    qualified: bool

# -------- Endpoints --------
@app.post("/predict", response_model=PredictResponse)
def predict(lead: Dict[str, Any]) -> PredictResponse:
    """
    Send any JSON dict. Example:
    {
      "gender": "female",
      "partner": "yes",
      "contract": "month-to-month",
      "tenure": 5,
      "monthlycharges": 70.2
    }
    """
    score = lead_score_from_dict(lead)
    return PredictResponse(lead_score=score, qualified=(score >= 0.5))

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
    uvicorn.run(app, host="0.0.0.0", port=9696)
