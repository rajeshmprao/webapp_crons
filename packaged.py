from webapp_db.connections import cursor_conn
import os

host = os.environ["DB_HOST"]
user = os.environ["DB_USER"]
passwd = os.environ["DB_PASS"]

cursor, conn = cursor_conn(user, passwd, host)
