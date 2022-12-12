import pandas as pd
import numpy as np

prices = pd.read_csv('prices.csv')

tickers = list(prices['ticker'].unique())

vols = {}
for t in tickers:
    prices_t = prices[prices['ticker'] == t]
    returns_t = np.log(prices_t['price']) - np.log(prices_t['price'].shift(1))
    vols[t] = np.std(returns_t)

max(vols)
