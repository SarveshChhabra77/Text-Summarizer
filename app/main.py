from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.pipeline.prediction_pipeline import PredictionPipeline
from app.schema import SummarizeRequest, SummarizeResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Absolute paths so Render's working directory doesn't matter
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title='Text Summarization API',
    version='0.0.1'
)
templates = Jinja2Templates(directory=str(BASE_DIR / 'templates'))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / 'static')), name="static")

pipeline = PredictionPipeline()

# Increment this string whenever CSS/JS changes to bust browser & CDN cache
STATIC_VERSION = "4"


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "v": STATIC_VERSION}
    )


@app.post('/summarize', response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    summary = pipeline.run(request.text)
    return SummarizeResponse(summary=summary)
