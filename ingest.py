import requests
import os
import sys
from dotenv import load_dotenv 

load_dotenv()
API_Key = os.getenv("ALPHA_VANTAGE_API_KEY")

def fetch_stock_data(symbol: str):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_Key}'

    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.RequestException as e:
        sys.exit(f"Network connection failed: {e}")

    if "Error Message" in data:
        sys.exit("API error, invalid stock ticker")

    if "Note" in data:
        sys.exit(f"API Limit Reached: {data['Note']}")

    return data 
