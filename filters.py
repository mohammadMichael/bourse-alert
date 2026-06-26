def apply_filter(item):
    cs = item["cs"]
    tvol = item["tvol"]
    pl = item["pl"]
    tmax = item["tmax"]
    tmin = item["tmin"]
    qd1 = item["qd1"]
    qo1 = item["qo1"]

    if cs != 1:
        return None

    if tvol == 0:
        return None

    if pl == tmax:
        score = 3 + (qd1 / tvol)
        return {"symbol": item["symbol"], "score": round(score, 2)}

    elif pl == tmin:
        score = -3 - (qo1 / tvol)
        return {"symbol": item["symbol"], "score": round(score, 2)}

    else:
        return {"symbol": item["symbol"], "score": round(pl / 100, 2)}
