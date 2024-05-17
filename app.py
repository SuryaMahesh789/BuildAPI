from fastapi import FastAPI 

app=FastAPI()

@app.get("/predict")
def predict_model(age:int,sex:str):
    if age<18 and (sex=='F' or sex=='f'):
        return {'Can Vote':'No','Gender':'Female','reason':'Age Limit'}
    elif age<18 and (sex=='M' or sex=='m'):
        return {'Can Vote':'No','Gender':'Male','reason':'Age Limit'}
    else:
        return {'Can Vote':'Yes'}