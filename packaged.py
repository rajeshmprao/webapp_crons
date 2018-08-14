from webapp_db.connections import cursor_conn
from webapp_crons import historic_scraper
from datetime import datetime
import os

host = os.environ["DB_HOST"]
user = os.environ["DB_USER"]
passwd = os.environ["DB_PASS"]

from_date = datetime(2016, 1, 1)
to_date = datetime(2018,8,12)
historic_scraper('fno', from_date, to_date)