from pydantic import BaseModel

class Input_body(BaseModel):
    textBody: str

class Classification(BaseModel):
    label: str
    score: float

class Output_body(BaseModel):
    probability: list[Classification]