import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
import joblib

app = FastAPI()

class InferenceRequest(BaseModel):
    no_of_adults: int
    no_of_children: int
    type_of_meal_plan: str
    required_car_parking_space: int
    lead_time: int

# Baixar o modelo do S3 na inicialização do app
@app.on_event("startup")
def load_model():
    try:
        s3 = boto3.client('s3')
        s3.download_file(os.getenv('S3_BUCKET_NAME'), 'model.joblib', 'model.joblib')
        global model
        model = joblib.load('model.joblib')
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar o modelo: {e}")

@app.post("/api/v1/inference")
def get_inference(request: InferenceRequest):
    try:
        data = [[request.no_of_adults, request.no_of_children, request.type_of_meal_plan, 
                 request.required_car_parking_space, request.lead_time]]
        prediction = model.predict(data)
        return {"result": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao realizar a inferência: {e}")
