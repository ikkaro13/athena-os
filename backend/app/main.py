from fastapi import FastAPI
from backend.app.schemas.match import MatchRequest
from backend.app.services.prediction_service import PredictionService

app = FastAPI(
    title="Athena OS",
    description="Sports Intelligence Platform",
    version="0.1.0"
)

prediction_service = PredictionService()

@app.get("/")
def root():
    return {
        "project": "Athena OS",
        "engine": "ONLINE",
        "module": "Hermes",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Hermes",
        "version": "0.1.0"
    }

@app.post("/predict")
def predict(match: MatchRequest):

    prediction = prediction_service.predict(
    match.league,
    match.home_team,
    match.away_team
)

    return prediction


