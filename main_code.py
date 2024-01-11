from bs4 import BeautifulSoup
import requests 
import sqlite3
import os

# ファイルパス
path = '/Users/miuramai/last_mission.py/ds-pg-pj'

# DBファイル名
db_name = 'temperature_data.sqlite'

# ディレクトリが存在しない場合は作成
os.makedirs(path, exist_ok=True)

# DBファイルへの完全なパス
db_path = os.path.join(path, db_name)

# DBに接続する（指定したDBファイルが存在しない場合は、新規に作成される）
con = sqlite3.connect(db_path)

# ここでデータベースの操作を行う（例：テーブル作成、データの挿入など）

# DBへの接続を閉じる
con.close()
