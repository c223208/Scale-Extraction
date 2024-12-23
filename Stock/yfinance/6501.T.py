import pandas as pd
import yfinance as yf

# 銘柄コード (例: 6501.T)
ticker = '6501.T'

# 取得する期間を設定
start_date = '2017-01-04'
end_date = '2019-03-29'

# データを取得
stock_data = yf.download(ticker, start=start_date, end=end_date)

# 必要なカラム（DateとClose）を抽出
stock_data = stock_data[['Close']].reset_index()

# CSVファイルとして保存
csv_filename = 'close_6501_20170104_20190329.csv'
stock_data.to_csv(csv_filename, index=False)

print(f"CSVファイルを作成しました: {csv_filename}")
