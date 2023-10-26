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

@app.get("/contact", response_class=HTMLResponse)
async def contact_form(request: Request):
    return templates.TemplateResponse(
        "contact.html",
        {"request": request, "name": name, "skills": skills}
    )

@app.post("/save_contact")
async def save_contact(request: Request):
    form_data = await request.form()
    name = form_data.get("name")
    email = form_data.get("email")
    message = form_data.get("message")
    
    with open("contacts.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Message: {message}\n")

    return {"message": "Contact information saved successfully!"}