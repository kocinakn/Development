from datetime import datetime
import pandas as pd

def get_cx_prices(cx: list):
    t = datetime.now()
    fr = None
    for crypto in cx:
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={crypto}USDT'
        data = pd.read_json(url, 'index')
        df = data.T
        if fr is None:
            fr = df
        else:
            fr = fr.append(df)
    print(t)
    print(fr.reset_index(drop=True))


if __name__ == '__main__':
    cx = ['BTC', 'ETH', 'LTC', 'ADA', 'XRP', 'BCH']
    df = get_cx_prices(cx)