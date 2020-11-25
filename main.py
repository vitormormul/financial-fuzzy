import pandas as pd
from fuzzy_logic import run_fuzzy

df = pd.read_csv('data.csv', sep=';')

tickers = []
investments = []
prices = []

for ticker in df.ticker.values:
  pl = df.loc[df.ticker == ticker].pl.values[0]
  pvp = df.loc[df.ticker == ticker].pvpa.values[0]
  div_yield = df.loc[df.ticker == ticker]['yield'].values[0]
  roe = df.loc[df.ticker == ticker].roe.values[0]

  investment, price = run_fuzzy(pl, pvp, div_yield, roe)
  tickers.append(ticker)
  investments.append(investment)
  prices.append(price)

data = {'Ticker': tickers, 'Investimento': investments, 'Preço': prices}
dfr = pd.DataFrame(data=data)
print(dfr)