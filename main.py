import models
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
#* Documentation can be found at localhost:8000/docs

app = FastAPI()
#* The above FastAPI application 'app' above is run bay running 'uvicorn <pythonFileAppIsIn>:<applicationName> --reload'
#* In this case, we would run 'uvicorn main:app --reload'.
#* We run this app by creating a shell script called 'run' and posting the above code in it.
#* We make the 'run' shell script an executable by typing 'chmod +x run' in the terminal.
#* We then run the 'run' shell script by typing './run' in the terminal
#* In the example below, can find output at 'localhost:8000/'

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def dashboard(request: Request):
    """
    Displays the stock screener dashboard / homepage.

    Returns:
        [type]: [description]
    """
    #return {"Dashboard": "Home Page"}
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "somevar": 2
    })

@app.post("/stock")
def create_stock():
    """
    Creates a stock and stores it in the database.

    Returns:
        [type]: [description]
    """
    return {
            "code": "success",
            "message": "stock created"
            }