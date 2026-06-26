def get_market_data():
    print("MARKET FUNCTION CALLED", flush=True)

    return [
        {
            "symbol": "TEST",
            "cs": 1,
            "tvol": 1000,
            "pl": 100,
            "tmax": 110,
            "tmin": 90,
            "qd1": 500,
            "qo1": 300,
        }
    ]
