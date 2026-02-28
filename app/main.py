from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.pipeline.prediction_pipeline import PredictionPipeline
from app.schema import SummarizeRequest,SummarizeResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title='Text Summarization API',
    version='0.0.1'
)
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

pipeline = PredictionPipeline()



@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/summarize',response_model=SummarizeResponse)
def summarize(request:SummarizeRequest):
    
    summary = pipeline.run(request.text)
    
    return SummarizeResponse(summary=summary)
