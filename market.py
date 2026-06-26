import random

def get_market_data():
    # داده تستی (بعداً واقعی میشه)
    symbols = ["فولاد", "شپنا", "خودرو", "وبملت", "شستا"]

    data = []

    for s in symbols:
        item = {
            "symbol": s,
            "cs": 1,
            "tvol": random.randint(1000, 100000),
            "pl": random.randint(90, 110),
            "tmax": 110,
            "tmin": 90,
            "qd1": random.randint(0, 50000),
            "qo1": random.randint(0, 50000),
        }
        data.append(item)

    return data
