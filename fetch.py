import requests
import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from api.config import api_key_alpaca, secret_key
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

headers = {
    'APCA-API-KEY-ID': api_key_alpaca,
    'APCA-API-SECRET-KEY': secret_key
}

base_url = 'https://api.alpaca.markets'

trading_client = TradingClient(api_key_alpaca, secret_key, paper=True)
client = StockHistoricalDataClient(api_key_alpaca, secret_key)
api_t = tradeapi.REST(api_key_alpaca, secret_key, base_url, api_version='v2')

'''Related Functions from different api that get realtime stock updates'''
def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&interval=1min&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    print(ticker_symbol, ":", price)
    return price

def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&interval=1min&apikey={api}"
    response = requests.get(url).json()
    datetime_ = response['datetime']
    print(datetime_)
    return datetime_

# get stock information based on entered ticker
def get_stock_info(ticker_symbol, time_in_force, limit):
    barset = api_t.get_bars(ticker_symbol, time_in_force, limit)
    
    # Extract the latest bar data for the stock
    latest_bars = barset[ticker_symbol]
    latest_bar = latest_bars[-1]
    
    return latest_bar

def get_account():
    account = trading_client.get_account()
    response = requests.get(f'{base_url}/v2/account', headers=headers)
    
    if response.status_code == 200:
        account_info = response.json()
        account_name = account_info['name']
        print(f"Account Name: {account_name}")
    else:
        print(f"Request failed with status code {response.status_code}")
    
    # Check if our account is restricted from trading.
    if account.trading_blocked:
        print('Account is currently restricted from trading.')
    print('${} is available as buying power'.format(account.buying_power))

# buy stock according user set parameters
def buy_stock(ticker_symbol, quantity, order, in_force):
    # Setting parameters for our buy order
    market_order_data = MarketOrderRequest(
    symbol=ticker_symbol,
    qty=quantity,
    side=order,
    time_in_force=in_force
    )
    #submits the buy order and prints the order ticker
    market_order = trading_client.submit_order(market_order_data)
    
    for property_name, value in market_order:
        print(f"\"{property_name}\": {value}")

# get historical data for ticker over specified period        
def get_historical_data(ticker, year, month, day):
    day = int(day)
    day2 = day - day + 1
    request = StockBarsRequest(
        symbol_or_symbols = [ticker],
        timeframe=TimeFrame.Day,
        start=datetime(int(year), int(month), day2),
        end=datetime(int(year), int(month), day)
    )
    bars = client.get_stock_bars(request)
    bars.df
    with open("data.txt", "w") as stockData:
            stockData.write(str(bars.df))

# get account info
def get_account_info():
    account = trading_client.get_account()
    for property_name, value in account:
        print(f"\"{property_name}\": {value}")
    


# def get_stock_quote(ticker_symbol, api):
#     url = f"https://api.twelvedata.com/statistics?symbol={ticker_symbol}&interval=1min&apikey={api}"
#     response = requests.get(url).json()
#     print(response)
#     return response

# name = get_stock_quote(ticker, api_key)['name']
# stock_price = get_stock_price(ticker, api_key)

