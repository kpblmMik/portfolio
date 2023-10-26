from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

name = "Mikhail Sarnov"
skills = ["Python", "git", "Linux", "html css js", "aws cli", "clouformation"]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": name, "skills": skills})
