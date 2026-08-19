import yfinance as yf
from pprint import pp, pprint
import matplotlib.pyplot as plt


# pandas DataFrame 下載台積電股票歷史股價數據 的功能

data = yf.download(["2330.TW"], start="2026-03-01", end="2026-05-01", interval="1d")
# 顯示 統計數據中的 移動平均線(股票常用 5日、10日、20日、60日、120日、240日) 以及 最高價、最低價、收盤價
pprint(data['Close']['2330.TW'])  # 顯示收盤
# 五日均值
data['MA5'] = data['Close']['2330.TW'].rolling(window=5).mean()
pprint(f"5-day Moving Average: {data['Close']['2330.TW'].rolling(window=5).mean().iloc[-1]:.2%}")
# 十日均值
data['MA10'] = data['Close']['2330.TW'].rolling(window=10).mean()
pprint(f"10-day Moving Average: {data['Close']['2330.TW'].rolling(window=10).mean().iloc[-1]:.2%}")
# 二十日均值
data['MA20'] = data['Close']['2330.TW'].rolling(window=20).mean()
pprint(f"20-day Moving Average: {data['Close']['2330.TW'].rolling(window=20).mean().iloc[-1]}")

#繪製 5日、10日、20日均線圖表
data[['Close','MA5','MA10','MA20']].plot(figsize=(12, 6))
plt.title('台積電 5日、10日、20日均線圖表')
plt.ylabel('價格') # 設定 y軸資料名稱
plt.show()   # 將圖表顯示出來




#每日報酬率

data['Daily Return'] = data['Close']['2330.TW'].pct_change()
pprint(f"Daily Returns:\n{data['Daily Return'].head()}")

#計算年化報酬率
annual_return = data['Daily Return'].mean() * 252  # 假設一年有252個交易日
pprint(f"Annualized Return: {annual_return:.2%}")

#計算macd指標
exp1 = data['Close']['2330.TW'].ewm(span=12, adjust=False).mean()
exp2 = data['Close']['2330.TW'].ewm(span=26, adjust=False).mean()
data['MACD'] = exp1 - exp2  


#計算rsi指標
delta = data['Close']['2330.TW'].diff() 
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
data['RSI'] = 100 - (100 / (1 + rs))