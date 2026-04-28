from fastapi import FastAPI
from app.schemas import InputData
from app.model import predict
from Recommendation_logic.recommend import get_recommendations

app = FastAPI(
    title="EV Intelligence System",
    description="Driving Behavior Classification API",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "EV Intelligence System API is running"}

@app.post("/predict")
def get_prediction(data: InputData):
    input_dict = data.dict()

    prediction, confidence = predict(input_dict)

    recommendation = get_recommendations(prediction, input_dict)

    return {
        "prediction": prediction,
        "confidence": confidence,
        "recommendations": recommendation
    }