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
