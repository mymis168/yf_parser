import yfinance as yf
from pprint import pprint

ticker_symbol = "2330.TW"  # 台積電股票代碼
ticker_symbol_nvidia = "TSLA"  # NVIDIA股票代碼

print("台積電基本資訊")
taiwan_semi = yf.Ticker(ticker_symbol_nvidia)
#pprint(taiwan_semi.info) 

pprint(taiwan_semi.fast_info)
print(f"台積電目前價格: {taiwan_semi.fast_info['lastPrice']}")
print(f"台積電目今日開盤價格: {taiwan_semi.fast_info['open']}")
print(f"台積電昨日收盤價格: {taiwan_semi.fast_info['previousClose']}")
print(f"台積電今日最高價格: {taiwan_semi.fast_info['dayHigh']}")
print(f"台積電今日最低價格: {taiwan_semi.fast_info.get('dayLow', '無')}")