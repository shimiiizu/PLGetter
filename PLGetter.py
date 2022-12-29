import matplotlib.pyplot as plt
from sqlite3.dbapi2 import Cursor
from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
import os
import sqlite3
import pandas as pd
import datetime
from datetime import date
from itertools import product


# DBの指定
DB = 'D:/XBRLDB/XBRL_DB_v02.db'

# sqlの指定
sql = 'SELECT * FROM XbrlDB'

# ダウンロード済のXbrlファイルのリストを作成
conn = sqlite3.connect(DB)
cur = conn.cursor()
df = pd.read_sql(sql, conn)

print(df.columns)

# 銘柄コードで抽出(Announcement_dateでソート)

# codeを指定
code = 6196
df_select = df[df['Code'] == code].sort_values('Announcement_date')

print(df_select['Announcement_date'])
print(df_select['Sales'])

xlist = df_select['Announcement_date'].values.tolist()
# xlist = df_select['OperatingIncome'].values.tolist()
ylist = df_select['Sales'].values.tolist()

plt.scatter(xlist, ylist)
plt.show()



