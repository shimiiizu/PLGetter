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