import requests

from config.keys import settings

def add_stock(session_id, symbol, qty, price, exchange, notes):
    payload = {
        "session_id": session_id,
        "stock_symbol": symbol.upper(),
        "quantity": qty,
        "buy_price": price,
        "exchange": exchange,
        "notes": notes
    }
    res = requests.post(f"{settings.FASTAPI_URL}/portfolio", json=payload)
    return res.status_code == 200

def get_portfolio(session_id):
    try:
        res = requests.get(f"{settings.FASTAPI_URL}/portfolio/{session_id}")
        return res.json() if res.status_code == 200 else []
    except Exception:
        return []
