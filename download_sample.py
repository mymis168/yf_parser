import yfinance as yf
from pprint import pp, pprint


data = yf.download("TSLA SPCX", start="2026-07-01", end="2026-08-01", interval="1wk")
pprint(data)