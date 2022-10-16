from fastapi import FastAPI
from reply_insta_classifier.data_models import Input_body, Output_body
from reply_insta_classifier.dummy_model import Dummy_text_classifier


dummy_model = Dummy_text_classifier()
app = FastAPI()


@app.post("/insta/classification")
async def get_prediction(input_body: Input_body):
    out = Output_body(probability = dummy_model.classify_text(input_body.textBody))
    return out.dict()