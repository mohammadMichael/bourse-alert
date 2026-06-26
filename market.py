import requests

def get_market_data():
    url = "https://cdn.tsetmc.com/api/ClosingPrice/GetMarketWatch?market=0"

    response = requests.get(url)
    data = response.json()

    results = []

    for item in data.get("marketWatch", []):
        try:
            results.append({
                "symbol": item.get("lVal18AFC"),   # نام سهم
                "cs": 1,
                "tvol": item.get("qTotTran5J"),    # حجم
                "pl": item.get("pClosing"),        # قیمت پایانی
                "tmax": item.get("priceMax"),      # سقف
                "tmin": item.get("priceMin"),      # کف
                "qd1": item.get("zTotTran"),       # خریدار
                "qo1": item.get("count"),          # فروشنده
            })
        except:
            continue

    return results
