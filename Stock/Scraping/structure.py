import requests
from bs4 import BeautifulSoup

# Yahoo FinanceのURL
url = "https://finance.yahoo.co.jp/quote/6501.T/history?from=20170104&to=20190329&timeFrame=d&page=1"

# ページをリクエストして取得
response = requests.get(url)

# HTMLをBeautifulSoupで解析
soup = BeautifulSoup(response.content, 'html.parser')

# テーブルの構造を確認
table = soup.find('table', {'class': 'tblHistory'})

if table:
    # テーブルが見つかった場合、各行を出力
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if cols:  # 行にデータがある場合のみ表示
            cols = [ele.text.strip() for ele in cols]
            print(cols)
else:
    print("テーブルが見つかりませんでした。")
