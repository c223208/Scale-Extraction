import time
import requests
from bs4 import BeautifulSoup

# Yahoo FinanceのURL
url = "https://finance.yahoo.co.jp/quote/6501.T/history?from=20170104&to=20190329&timeFrame=d&page=1"

# ページをリクエストして取得
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# テーブルを見つける
table = soup.find('table', {'class': 'tblHistory'})

# 行を抽出する
rows = table.find_all('tr')

# 各行からデータを抽出
data = []
for row in rows[1:]:  # 最初の行はヘッダーなのでスキップ
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]  # テキストを取得
    data.append(cols)

# データを表示
for row in data:
    print(row)



## Google Sheets
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Google Sheets API認証
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'  # ここに認証ファイルのパスを記入

# スプレッドシートIDと範囲
SPREADSHEET_ID = '16MAxgubd_XxbdR1C4ouFv3NhCIVREcFPko0IFRjEzqg'
RANGE_NAME = 'Sheet1!A1'

# サービスを構築
credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)

# データを書き込む
values = [
    # スクレイピングで取得したデータをここに追加
    ['2021-01-01', '1500', '1550', '1490', '1530', '5000'],
    # 他の行...
]
body = {
    'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
    valueInputOption='RAW', body=body).execute()

print(f"{result.get('updatedCells')} cells updated.")



## ページ遷移
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Selenium WebDriverのセットアップ
driver = webdriver.Chrome(executable_path='path/to/chromedriver')  # ChromeDriverのパスを指定

# 最初のページにアクセス
driver.get('https://finance.yahoo.co.jp/quote/6501.T/history?from=20170104&to=20190329&timeFrame=d&page=1')

while True:
    # ページのデータをスクレイピングする（同じBeautifulSoupを使って）
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', {'class': 'tblHistory'})
    rows = table.find_all('tr')
    
    # データの抽出
    data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
    
    # Google Sheetsにデータを書き込む（前述のコードを呼び出す）
    # ここで、dataをGoogle Sheetsに書き込む処理を行う
    
    # 次のページへ進む
    try:
        next_button = driver.find_element(By.XPATH, '//a[@class="next"]')  # "次へ"ボタンのXPath
        next_button.click()
        time.sleep(3)  # ページが読み込まれるまで待つ
    except Exception as e:
        print("次のページがありません。終了します。")
        break  # 次のページがない場合、終了
