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

def prepare_data(d):
    for k, v in d.items():
        v['mid_price'] = (v.ask0 + v.bid0)/2
        v['spread'] = v.ask0 - v.bid0
        v['rolling_mean_spread'] = v.spread.rolling('5s').mean()
    return d


if __name__ == '__main__':
    cx = ['BTC', 'ETH', 'LTC', 'ADA', 'XRP', 'BCH']
    get_cx_prices(cx)