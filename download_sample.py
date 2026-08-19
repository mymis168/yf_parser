import yfinance as yf
from pprint import pp, pprint


data = yf.download(["NVDA","AMD"], start="2026-03-01", end="2026-08-01", interval="1wk")
pprint(type(data))
pprint(data['Close']['NVDA'])  # 顯示收盤