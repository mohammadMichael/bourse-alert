def apply_filter(item):
    return {
        "symbol": item["symbol"],
        "score": item["pl"] / 100
    }
