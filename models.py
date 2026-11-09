from pydantic import BaseModel, ValidationError
from datetime import date 

class weekly_close(BaseModel):
    date: date
    price: float

def clean_stock_data(raw_data: dict) -> list[weekly_close]:
    weekly_series = raw_data.get("Weekly Time Series", {})
    clean_data = []
    bad_data = []
    
    for week, price_info in weekly_series.items():
        try:
            weekly_data = weekly_close(
                date=week,
                price=float(price_info['4. close'])
            )
            clean_data.append(weekly_data)
        except ValidationError as e:
            current_data = {
                'date': week,
                'price': price_info,
                'msg': e
            }
            bad_data.append(current_data)

    return clean_data, bad_data