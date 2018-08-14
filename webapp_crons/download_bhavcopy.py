__author__ = "Rajesh Rao"
__copyright__ = "meh"
__status__ = "Development"

import requests
import zipfile
import io


def download_bhavcopy(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(path="csv_files")
            # print("Downloaded csv for date " + str(url))
            return True
        elif r.status_code == 404:
            # print("File does not exist for date")
            return False
        else:
            print(r, r.status_code)
            return False
    except Exception as e:
        print(e)
        return False