import requests

def get_market_data():
    url = "https://old.tsetmc.com/tsev2/data/MarketWatchPlus.aspx"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    text = r.text

    results = []

    # دیتا به صورت ; جداست
    rows = text.split(";")

    for row in rows:
        parts = row.split("@")

        try:
            if len(parts) < 10:
                continue

            symbol = parts[0]

            results.append({
                "symbol": symbol,
                "cs": 1,
                "tvol": float(parts[3] or 0),
                "pl": float(parts[2] or 0),
                "tmax": float(parts[6] or 0),
                "tmin": float(parts[7] or 0),
                "qd1": float(parts[8] or 0),
                "qo1": float(parts[9] or 0),
            })

        except:
            continue

    return results
