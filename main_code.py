from bs4 import BeautifulSoup
import requests 
import sqlite3
import os

# ファイルパス
path = '/Users/miuramai/last_mission.py/ds-pg-pj/'

# DBファイル名
db_name = 'temperature_data.sqlite'

# ディレクトリが存在しない場合は作成
os.makedirs(path, exist_ok=True)

# DBファイルへの完全なパス
db_path = os.path.join(path, db_name)

# DBに接続する（指定したDBファイルが存在しない場合は、新規に作成される）
con = sqlite3.connect(db_path)

# DBへの接続を閉じる
con.close()

#-------------------------------------------------------#
# DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 実行したいSQLを用意する
# テーブルを作成するSQL
# CREATE TABLE テーブル名（カラム名 型，...）;
sql_create_table_temperature_data_table = 'CREATE TABLE temperature_data_table(temperature_ave real, humidity_ave real, sunshine_hours real);'

# 4．SQLを実行する
cur.execute(sql_create_table_temperature_data_table)

# 6．DBへの接続を閉じる
con.close()

#-------------------------------------------------------#
import requests
from bs4 import BeautifulSoup
import sqlite3
import time

# データベースへの接続
conn = sqlite3.connect('temperature_data.sqlite')  # データベースのファイル名を適切に指定してください
cur = conn.cursor()

# スクレイピング対象のURLを構築
base_url = f"https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=45&block_no=47682&year=2023&month=12&day=17&view="

# HTTPリクエストを送信してウェブページのHTMLを取得
response = requests.get(base_url)

# レスポンスが正常であるかを確認
if response.status_code == 200:
    # BeautifulSoupを使ってHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # テーブルの行を取得
    rows = soup.find_all('tr')

    for row in rows:
        # 'td'タグを持つ要素を取得
        columns = row.find_all('td')

        # 列が十分にあるかを確認してから取得
        if len(columns) > 16:
            data_0_0_value = float(columns[6].text)
            data_0_1_value = float(columns[9].text)
            data_0_2_value = float(columns[16].text)

            # 各データをデータベースに挿入
            sql_insert_data = "INSERT INTO temperature_data_table(temperature_ave, humidity_ave, sunshine_hours) VALUES (?, ?, ?);"
            cur.execute(sql_insert_data, (data_0_0_value, data_0_1_value, data_0_2_value))

            # 1秒スリープ
            time.sleep(1)

    # トランザクションのコミット
    conn.commit()

else:
    # エラーが発生した場合はエラーステータスコードを表示
    print(f"Error: {response.status_code}")

# データベース接続をクローズ
conn.close()

#-------------------------------------------------------#

# DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 新しいテーブルを作成するSQL
sql_create_table_local_data = 'CREATE TABLE local_data(number_of_steps INTEGER);'
cur.execute(sql_create_table_local_data)



# 6．DBへの接続を閉じる
con.close()

#-------------------------------------------------------#

# 1．DBに接続する
con = sqlite3.connect(path + db_name)

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．データを挿入するSQL
sql_insert_local_data = "INSERT INTO local_data(number_of_steps) VALUES (?);"

# 4．データをリストで用意する
new_column_data_str = "13607,25,3974,3731,18778,672,6941,7373,5225,4855,4714,4454,3116,6313,8614,4908,5996,4177,3302,1926,5681,9078,3709,5576,8181,4084,15737,5043,2075,6495,5448"
new_column_data_list = [int(x) for x in new_column_data_str.split(',')]

# 5．31行のデータを一気に挿入
for data in new_column_data_list:
    cur.execute(sql_insert_local_data, (data,))

# 6．コミット処理（データ操作を反映させる）
con.commit()

# 7．DBへの接続を閉じる
con.close()
