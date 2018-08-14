from .fno_scraper import fno_scraper
from datetime import datetime, timedelta

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def historic_scraper(security, from_date_object, to_date_object):
    if security == 'fno':
        for date in daterange(from_date_object, to_date_object):
            fno_scraper(date)
            print("{} done".format(date.strftime("%d/%m/%Y")))
        
