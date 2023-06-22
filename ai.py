from datetime import date
import openai
from api.config import api_key_OPENAI

openai.api_key = api_key_OPENAI


today = date.today()
def generate_stock_prediction(ticker):
    response = openai.Completion.create(
        prompt=f"Is {ticker} a good buy for {today}", 
        model="gpt-3.5-turbo", 
        max_tokens=1000, 
        temperature=1,
        n=1,stop=['---'])
    for result in response:
        print(result.text)
    