import ta
import yfinance as yf
from pprint import pp, pprint

#ta 產出指標前需要準備 OCHLV 資料
symbol = "2330.TW"  # 台積電股票代碼
ticker = yf.Ticker(symbol)  

data = ticker.history(start="2026-03-01", end="2026-05-01", interval="1d")
#pprint(data)  # 顯示前幾筆資料

#指標定義在 SMAIndicator 類別中，使用時需要傳入收盤價資料以及計算的天數
sma_obj = ta.trend.SMAIndicator(close=data['Close'], window=5)
print(type(sma_obj))
# print(sma_obj)       列印 sma_indicator 物件的資訊(只會顯示他的 object id)

#呼叫 sma_indicator 才是真正計算五日均值的工作
data['SMA5'] = sma_obj.sma_indicator()
print(f"五日趨勢: {data['SMA5']}")

