# -*- coding: utf-8 -*-
__author__ = "Rajesh Rao"
__copyright__ = "meh"
__status__ = "Development"

def get_url_from_date(url_type, date_object):
    if url_type == 'fno':
        base_url = "https://www.nseindia.com/content/historical/DERIVATIVES/"
        year = date_object.year

        url = base_url + str(year) + "/"

        month_name = (date_object.strftime("%b")).upper()
        date = (date_object.strftime("%d"))
        year = (date_object.strftime("%Y"))

        url = url + str(month_name) + "/fo" + date + month_name + year
        final_url = url + "bhav.csv.zip"

        zip_name = "fo" + date + month_name + year + "bhav.csv"

        return zip_name, final_url
        