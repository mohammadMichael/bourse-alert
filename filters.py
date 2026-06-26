def apply_filter(item):
    symbol = item["symbol"]
    tvol = item["tvol"]
    pl = item["pl"]
    tmax = item["tmax"]
    tmin = item["tmin"]
    qd1 = item["qd1"]
    qo1 = item["qo1"]

    if tvol == 0:
        return None

    score = 0

    # 📈 صف خرید نزدیک سقف
    if tmax > 0 and pl >= tmax * 0.98:
        score = 3 + (qd1 / (tvol + 1))

    # 📉 صف فروش نزدیک کف
    elif tmin > 0 and pl <= tmin * 1.02:
        score = -3 - (qo1 / (tvol + 1))

    # 📊 حرکت حجمی
    elif tvol > 50000:
        score = pl / 100

    else:
        return None

    # فقط سیگنال مهم
    if abs(score) < 2:
        return None

    return {
        "symbol": symbol,
        "score": round(score, 2)
    }
