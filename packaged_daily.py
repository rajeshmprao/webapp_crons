from webapp_db.connections import cursor_conn
from webapp_crons import daily_scraper
from datetime import datetime
import os

host = os.environ["DB_HOST"]
user = os.environ["DB_USER"]
passwd = os.environ["DB_PASS"]

date = datetime(2018, 8, 13)
daily_scraper('fno', date)