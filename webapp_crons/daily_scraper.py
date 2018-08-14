from .fno_scraper import fno_scraper
from datetime import datetime

def daily_scraper(security):
    if security == 'fno':
        date = datetime.today()
        fno_scraper(date)
