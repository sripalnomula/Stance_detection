import numpy as np
import os
import pickle
from utils.fnd import pre_process
from utils.stance import stance_detection
import uvicorn
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
load_dotenv()
print(os.environ.get('HOST'))
with open(os.environ.get("TFIDF_PATH"),'rb') as f:
    tfidf = pickle.load(f)

with open(os.environ.get("SELECTOR_PATH"),'rb') as f:
    selector = pickle.load(f)

with open(os.environ.get("NB_PATH"),'rb') as f:
    nb_classifiers = pickle.load(f)

with open(os.environ.get("STANCE_PATH"),'rb') as f:
    stance_model = pickle.load(f)
with open(os.environ.get("STANCE_TFIDF_PATH"),'rb') as f:
    tfidf_vect = pickle.load(f)
app = FastAPI()
print(os.environ.get("CLIENT_URL"))
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CLIENT_URL")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/fake-news-detection")
async def fakeNewsDetection(req:Request):
    req_info = await req.json()
    X = pre_process(req_info['title'],req_info['body'],tfidf,selector)
    y = nb_classifiers.predict_proba(X)[0]
    if(y[0]>y[1]):
        return {"status":200,"message":"Provided information is falsy with {:.2f}% chance".format(y[0]*100),"class":False,"prediction_prob":y[0]}
    else:
        return {"status":200,"message":"Provided information is truthy with {:.2f}% chance".format(y[1]*100),"class":True,"prediction_prob":y[1]}

@app.post("/stance-detection")
async def stanceDetection(req:Request):
    req_info = await req.json()
    result = stance_detection(req_info["title"],req_info['body'],tfidf_vect,stance_model)
    return {"status":200,"message":"The given title {} about body/text".format(result),"stance":result}

if __name__=="__main__":
    uvicorn.run(app,host=os.environ.get('HOST'),port=int(os.environ.get('PORT')))