import yfinance as yf
from pprint import pprint


tickers_list = "AAPL MSFT GOOG TSLA SPCX NVDA INTC AMD 2330.TW 2454.TW"
tickers = yf.Tickers(tickers_list)

#取出每一檔個股 顯示開收盤最高低價格
for ticker in tickers.tickers.values():
    print(f"{ticker.ticker} 基本資訊")    
    print(f"{ticker.ticker} 目前價格: {ticker.fast_info['lastPrice']}")
    print(f"{ticker.ticker} 昨日收盤價格: {ticker.fast_info['previousClose']}")
    print(f"{ticker.ticker} 今日開盤價格: {ticker.fast_info['open']}")    
    print(f"{ticker.ticker} 今日最高價格: {ticker.fast_info['dayHigh']}")
    print(f"{ticker.ticker} 今日最低價格: {ticker.fast_info.get('dayLow', '無')}")
    print("=====================================")