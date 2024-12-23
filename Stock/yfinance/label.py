import yfinance as yf

# 例: 6501.T の株価データを取得
stock_data = yf.download('6501.T', period='1y')

# データの確認
print(stock_data.head())  # データの最初の数行を表示

# 列名の確認
print(stock_data.columns)