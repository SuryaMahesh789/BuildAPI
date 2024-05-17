from fastapi import FastAPI 

from pydantic import BaseModel

class Input(BaseModel):
    age:int
    sex:str
    
app=FastAPI()

@app.put("/predict")
def predict_model(d:Input):
    if d.age<18 and (d.sex=='F' or d.sex=='f'):
        return {'Can Vote':'No','Gender':'Female','reason':'Age Limit'}
    elif d.age<18 and (d.sex=='M' or d.sex=='m'):
        return {'Can Vote':'No','Gender':'Male','reason':'Age Limit'}
    else:
        return {'Can Vote':'Yes'}