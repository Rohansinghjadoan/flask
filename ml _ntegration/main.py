from fastapi import FastAPI
from schemas import InputSchema,OutputSchema
from predict import make_prediction,make_batch_predictions
from typing import List

app=FastAPI()


@app.get('/')
def index():
    return {'message':'Welcome to the House Price Prediction API'}

@app.post('/predict',response_model=OutputSchema)
def predict_price(data:InputSchema):
    predicted_price=make_prediction(data.model_dump()) ## model_dump() converts pydantic model to dictionary
    return OutputSchema(predicted_price=round(predicted_price,2))


@app.post('/batch_predict',response_model=list[OutputSchema])
def batch_predict(data:List[InputSchema]):
    pass
    