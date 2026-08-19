import yfinance as yf
from pprint import pp, pprint


ticker_symbol = "2330.TW"  # 台積電股票代碼
ticker = yf.Ticker(ticker_symbol)
#pprint(ticker.history(period="3mo" , interval="1wk")) 
pprint(ticker.history(start="2026-07-01", end="2026-07-31")) # 顯示台積電的歷史股價數據