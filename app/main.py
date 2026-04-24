from fastapi import FastAPI
from app.schemas import InputData
from app.model import predict

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

    prediction = predict(input_dict)

    # simple recommendations
    if prediction == "Aggressive":
        recommendation = [
            "Reduce speed",
            "Avoid sudden acceleration"
        ]
    elif prediction == "Eco":
        recommendation = [
            "Maintain current driving pattern",
            "Efficient driving detected"
        ]
    else:
        recommendation = [
            "Maintain moderate speed",
            "Balanced driving"
        ]

    return {
        "prediction": prediction,
        "recommendations": recommendation
    }