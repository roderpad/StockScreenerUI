import models
import yfinance
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Stock
#* Documentation can be found at localhost:8000/docs

app = FastAPI()
#* The above FastAPI application 'app' above is run bay running 'uvicorn <pythonFileAppIsIn>:<applicationName> --reload'
#* In this case, we would run 'uvicorn main:app --reload'.
#* Here, we run this app by creating a shell script called 'run' and posting 'uvicorn main:app --reload' in it.
#* We then make the 'run' shell script an executable by typing 'chmod +x run' in the bash terminal.
#* We then run the 'run' shell script by typing './run' in the terminal
#* In the example below, can find output at 'localhost:8000/'

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

class StockRequest(BaseModel):
    symbol: str
    
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def dashboard(request: Request, forward_pe = None, dividend_yield = None, ma50 = None, ma200 = None, db: Session = Depends(get_db)):
    """
    Displays the stock screener dashboard / homepage.

    Returns:
        [type]: [description]
    """
    #return {"Dashboard": "Home Page"}
    
    stocks = db.query(Stock)
    if forward_pe:
        stocks = stocks.filter(Stock.forward_pe < forward_pe)
    if dividend_yield:
        stocks = stocks.filter(Stock.dividend_yield > dividend_yield)
    if ma50:
        stocks = stocks.filter(Stock.price > Stock.ma50)
    if ma200:
        stocks = stocks.filter(Stock.price > Stock.ma200)
    #print(stocks)
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "stocks": stocks,
        "dividend_yield": dividend_yield,
        "forward_pe": forward_pe,
        "ma50": ma50,
        "ma200": ma200
    })

def fetch_stock_data(id: int):
    db = SessionLocal()
    stock = db.query(Stock).filter(Stock.id == id).first()
    
    yahoo_data = yfinance.Ticker(stock.symbol)
    
    stock.ma200 = yahoo_data.info['twoHundredDayAverage']
    stock.ma50 = yahoo_data.info['fiftyDayAverage']
    stock.price = yahoo_data.info['previousClose']
    stock.forward_pe = yahoo_data.info['forwardPE']
    stock.forward_eps = yahoo_data.info['forwardEps']
    if yahoo_data.info['dividendYield'] is not None:
        stock.dividend_yield = yahoo_data.info['dividendYield'] * 100 #* In percent
    else:
        stock.dividend_yield = yahoo_data.info['dividendYield']
    
    db.add(stock)
    db.commit()

@app.post("/stock")
async def create_stock(stock_request: StockRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Creates a stock and stores it in the database.

    Returns:
        [type]: [description]
    """
    stock = Stock()
    stock.symbol = stock_request.symbol
    
    db.add(stock)
    db.commit()
    
    background_tasks.add_task(fetch_stock_data, stock.id)
    db.refresh(stock)
    
    return {
            "code": "success",
            "message": "stock created"
            }