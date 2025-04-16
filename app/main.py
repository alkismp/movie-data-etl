
from src.config import CONFIG
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.extract import fetch_movie_data

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "movie_data": None})


async def search(request: Request, title: str = Form(...)):
    movie_data = fetch_movie_data(title)
    return templates.TemplateResponse("index.html", {"request": request, "movie_data": movie_data, "searched_title": title})
