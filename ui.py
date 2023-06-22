import typer
import fetch
from api.config import api_key_stock
from alpaca.trading.enums import OrderSide, TimeInForce

app = typer.Typer(add_completion=False)

@app.command()
def Check(
    ticker: str = typer.Option(
        "AAPL",
        "--ticker",
        "-t",
        help="Check the current market price of a stock"    
    )
):
    fetch.get_stock_price(ticker, api_key_stock)
    fetch.get_stock_quote(ticker,api_key_stock)
    

@app.command()
def Trade(
    ticker: str = typer.Option(
        "AAPL",
        "--ticker",
        "-t",
        help="Selects the stock you want"
    ),
    quantity: str = typer.Option(
        "1",
        "--quantity",
        "-q",
        help="Specifies the amount of shares purchased"    
    ),
    slide: str = typer.Option(
        "BUY",
        "--slide",
        "-s", "-b",
        help="Enter either BUY or SELL"
    ),
    Time_In_Force: str = typer.Option(
        "GTC",
        "--Time-In-Force",
        "-f",
        help="Selects when you want to keep order open to"
    )
):
    #Convert string to class
    ticker = ticker.upper()
    
    if slide.upper() == "BUY":
        slide = OrderSide.BUY
    if slide.upper() == "SELL":
        slide = OrderSide.SELL
        
    if Time_In_Force.upper() == "GTC":
        Time_In_Force = TimeInForce.GTC
    if Time_In_Force.upper() == "CLS":
        Time_In_Force = TimeInForce.CLS
    if Time_In_Force.upper() == "DAY":
        Time_In_Force = TimeInForce.DAY
    if Time_In_Force.upper() == "OPG":
        Time_In_Force = TimeInForce.OPG
    
    
    #fetch order ticker and buy/sell info    
    fetch.buy_stock(ticker, quantity, slide, Time_In_Force)

@app.command()
def Account(
    name: str = typer.Option(
        'John',
        '--name',
        '-n',
        help="Enter your name"
    )
):
    fetch.get_account(name)


    
if __name__ == "__main__":
    app()
    
    