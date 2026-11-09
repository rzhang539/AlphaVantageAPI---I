import json
import os
from pprint import pprint
from ingest import fetch_stock_data
from models import clean_stock_data
from database import create_save_database, get_data_db

stock_ticker = input("Enter stock sticker: ")
cache_file = f"{stock_ticker}_raw.json"

if os.path.exists(cache_file):
    with open(cache_file, "r") as f:
        reJSON = json.load(f)
    print("loaded locally")
else:
    reJSON = fetch_stock_data(stock_ticker)
    with open(cache_file, "w") as f:
        json.dump(reJSON, f, indent=4)
    print("fetched from AlphaVantage")

clean_data, bad_data = clean_stock_data(reJSON)

print(len(clean_data))
print(len(bad_data))
print(bad_data)

print(type(clean_data))

for item in clean_data[:5]:
    print(item)
    print(type(item))

create_save_database(stock_ticker, clean_data)

reverted_list = get_data_db(stock_ticker)
print(len(reverted_list))

for item in reverted_list[:5]:
    print(item)