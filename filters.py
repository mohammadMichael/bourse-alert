def apply_filter(item):
    symbol = item["symbol"]
    pl = item["pl"]

    # 🔥 تست ساده و قطعی
    score = pl / 100

    return {
        "symbol": symbol,
        "score": round(score, 2)
    }
