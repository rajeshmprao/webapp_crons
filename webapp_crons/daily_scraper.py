from .fno_scraper import fno_scraper
from datetime import datetime

def daily_scraper(security, date = None):
    if security == 'fno':
        if date == None:
            date = datetime.today()
        fno_scraper(date)
