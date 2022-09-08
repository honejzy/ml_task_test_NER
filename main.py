from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import json


app = FastAPI()
templates = Jinja2Templates(directory="templates/")

tokenizer = AutoTokenizer.from_pretrained("surdan/LaBSE_ner_nerel")
model = AutoModelForTokenClassification.from_pretrained("surdan/LaBSE_ner_nerel")
app.token_classifier = pipeline(
    "token-classification", tokenizer=tokenizer, model=model, aggregation_strategy="average"
)


@app.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request, 'input': ''})


@app.post("/")
def form_post(request: Request, data: str = Form(...)):
    result = app.token_classifier(data)
    for item in result:
        item.pop('score')
        item.pop('start')
        item.pop('end')
    return templates.TemplateResponse('index.html', context={'request': request, 'input': data, 'output': result})
