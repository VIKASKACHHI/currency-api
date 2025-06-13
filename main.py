from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Currency API is running ✅"}
@app.get("/convert")
def convert(from_currency: str, to_currency: str, amount: float):
    # conversion logic
    return {"result": ...}


# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

# Static currency rates from 1 USD
exchange_rates = {
    "USD": 1.0,
    "INR": 83.23,
    "EUR": 0.92,
    "GBP": 0.78,
    "JPY": 156.7,
    "AED": 3.67,
    "CNY": 7.25
}

@app.get("/convert")
def convert_currency(
    from_currency: str = Query(...),
    to_currency: str = Query(...),
    amount: float = Query(...)
):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return {"success": False, "error": "Unsupported currency"}

    # Convert from `from_currency` to USD, then to `to_currency`
    usd_amount = amount / exchange_rates[from_currency]
    converted_amount = usd_amount * exchange_rates[to_currency]

    return {
        "success": True,
        "from": from_currency,
        "to": to_currency,
        "rate": round(exchange_rates[to_currency] / exchange_rates[from_currency], 4),
        "converted": round(converted_amount, 2)
    }
