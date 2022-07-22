import imp
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from binance.cm_futures import CMFutures
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#from config import api_key, secret
#from uitils import *

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
dir = directory=str(Path(BASE_DIR, 'static'))
#templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'static')))


app = FastAPI(
    title = "FastApi",
    description = "Binance Futures",
    version = "0.0.0 / test",
)       

#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/binance/test/connection/{key}/{secret}')
def auth_get_all_blog_users(key: str, secret: str):
    cm_futures_client = CMFutures(key=key, secret=secret)
    return cm_futures_client.account()


# @app.get('/binance/candle')
# async def binance_candle(request: Request):
#     client = RequestClient(api_key=api_key, secret=secret)
#     candels = client.get_candlestick_data(symbol="BTCUSDT", interval="1m", limit=10)
#     return candels

# @app.get('/binance/account')
# async def binance_account(request: Request):
#     client = RequestClient(api_key=api_key, secret=secret)
#     result = client.get_account_information()
#     return Get_Capital(result, "USDT")




if __name__ == "__main__":
    uvicorn.run("main:app", host = "localhost", port = 3001, log_level="info", reload=True)