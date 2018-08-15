import os
import csv
import datetime
import pandas as pd
import pymysql
import time


from webapp_db.connections import cursor_conn
from webapp_db.get import fno_symbol
from webapp_db.insert import futures_eod_data, options_eod_data

from .get_url_from_date import get_url_from_date
from .download_bhavcopy import download_bhavcopy


db_host = os.environ["DB_HOST"]
db_usename = os.environ['DB_USER']
db_password = os.environ['DB_PASS']

futures_to_insert = []
options_to_insert = []
def fno_scraper(datetime_object):

    cursor, _ = cursor_conn(db_usename, db_password, db_host )
    
    try:
        zipname, url = get_url_from_date('fno', datetime_object)
        downloaded_zip = download_bhavcopy(url)
        if downloaded_zip is True:
            print("Got FNO Bhavcopy for " +
                  (datetime_object.strftime("%d-%b-%Y")))
            fno_symbol_dict = fno_symbol(cursor)
            process_fno_bhav(
                zipname, fno_symbol_dict, datetime_object.date(),
                cursor)

        else:
            print("FNO Bhavcopy does not exist for " +
                  (datetime_object.strftime("%d-%b-%Y")))
    except Exception as e:
        raise
        print(e)
    return


def process_fno_bhav(zipfile, fno_symbol_dict, date, cursor):
    zipfile = "csv_files/" + zipfile
    print("processing FNO csv for " + str(zipfile))
    file_reader = csv.DictReader(open(zipfile))
    print(fno_symbol_dict)
    for row in file_reader:
        if int(row["OPEN_INT"]) != 0 and exists_in_db(row, fno_symbol_dict):
            try:
                instrument = row['INSTRUMENT']
                symbol = row['SYMBOL']
                expriy_date_object = date_object = datetime.datetime.strptime(
                    row['EXPIRY_DT'], '%d-%b-%Y').date()

                # Strike Price is 0 by default
                strike_price = row['STRIKE_PR']
                option_type = row['OPTION_TYP']
                open_value = row['OPEN']
                high_value = row['HIGH']
                low_value = row['LOW']
                close_value = row['CLOSE']
                settle_value = row['SETTLE_PR']
                contracts = row['CONTRACTS']
                val_inlakh = row['VAL_INLAKH']
                open_int = row['OPEN_INT']
                change_in_oi = row['CHG_IN_OI']
                date_object = datetime.datetime.strptime(
                    row['TIMESTAMP'], '%d-%b-%Y').date()

                # option_type is 0 by default
                # Set option_type to 'NONE' for futures
                if option_type == 'XX':
                    option_type = 'NONE'
                    futures_to_insert.extend([symbol,
                                        instrument,
                                        date_object,
                                        expriy_date_object,
                                        option_type,
                                        open_value,
                                        high_value,
                                        low_value,
                                        close_value,
                                        settle_value,
                                        open_int,
                                        change_in_oi])
                else:
                    options_to_insert.extend([symbol,
                                        instrument,
                                        date_object,
                                        strike_price,
                                        expriy_date_object,
                                        option_type,
                                        open_value,
                                        high_value,
                                        low_value,
                                        close_value,
                                        settle_value,
                                        open_int,
                                        change_in_oi])
            except Exception as e:
                raise
                if e.args[0] == 1062:
                    continue

                # Else continue
                else:
                    print(e)
        else:
            pass
    futures_eod_data(cursor, futures_to_insert)
    options_eod_data(cursor, options_to_insert)
    os.remove(zipfile)
    futures_to_insert.clear()
    options_to_insert.clear()



def exists_in_db(row, fno_symbol_dict):

    if 'FUT' in row['INSTRUMENT']:
        row_record = [
            row['SYMBOL']]
            
        
        flag = 0
        for rows in fno_symbol_dict:
            if(rows['SYMBOL'] == row_record[0]):
                flag = 1
        if flag == 1:
            return True
        else: return False
    elif 'OPT' in row['INSTRUMENT']:
        row_record = [
            row['SYMBOL']]
        flag = 0
        for rows in fno_symbol_dict:
            if(rows['SYMBOL'] == row_record[0]):
                flag = 1
        if(flag == 1):
            # input(row_record)        
            return True
        else: return False
    else:
        return False
    
