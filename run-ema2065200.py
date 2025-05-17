
import os
import sys
print(sys.path)
from fyerutilities import fyerutilities
from login.login import login




access_token = login.SetupLogin()

import csv
import requests

CSV_URL = 'https://public.fyers.in/sym_details/BSE_CM.csv'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    data =[]
    
    for row in my_list:
        try:
            # vals = row.split(',')
            stockSymbol = row[9]
            # print(row)
            val = fyerutilities.getStockData(row,access_token,stockSymbol,360,"D")
            if len(val)>0:
                data.append(val)
                if len(data)>10:
                    f = open("C:\PersonalFolder\data.csv", "a")
                    writer = csv.writer(f)
                    writer.writerows(data)
                    f.close()
                    data=[]
        except:
            b=10

