from datetime import datetime, timedelta
import math
import time
import winsound
from colorama import Fore, Back, Style
from fyers_apiv3 import fyersModel
import pandas as pd

class utility:
    def readFromFileAsString(filename):
        text_file = open(filename, "r")    
        data = text_file.read()    
        text_file.close() 
        return data
    def writeToFile(filename,mode,content):
        txtfile = open(filename,mode)
        txtfile.write(content)
        txtfile.close()        
    def waitTillMarketOpenForFiveMinCandles(wait):
        print(datetime.now().strftime('%H:%M:%S'))
        if wait.lower() == 'true':
            # find is market time or sleep before or after market time
            timeBeforeMarketOpen =0
            if datetime.now().strftime('%H:%M:%S')<'09:10:00' :#or datetime.now().strftime('%H:%M:%S')>'15:30:00':
                # start time
                start_time = datetime.now().strftime('%H:%M:%S')
                end_time = '09:10:00'
                # convert time string to datetime
                t1 = datetime.strptime(start_time, "%H:%M:%S")
                t2 = datetime.strptime(end_time, "%H:%M:%S")
                delta = t2 - t1
                timeBeforeMarketOpen = delta.total_seconds()
            while (datetime.now().strftime('%H:%M:%S')<'09:10:00'):
                time.sleep(timeBeforeMarketOpen)
            print(datetime.now().strftime('%H:%M:%S'))
            while int(datetime.now().strftime('%M'))%5!=0:
                time.sleep(1)
            print(datetime.now().strftime('%H:%M:%S'))
            while int(datetime.now().strftime('%S'))%1>5 and int(datetime.now().strftime('%S'))%1<15:
                time.sleep(1)
            print(datetime.now().strftime('%H:%M:%S'))
    def getPositions(client_id,access_token):
        fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="C:\delete")
        return fyers.positions()
    
    def getQuotes(client_id,access_token,symbol):
        fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="C:\delete")
        data = {
            "symbols":symbol
        }
        response = fyers.quotes(data=data)
        return response
    
    def getData(client_id,access_token,symbol="NSE:NIFTYBANK-INDEX",numberOfDays =1,resolution="5"):
        vardata = datetime.now() - timedelta(days=numberOfDays)
        instraDayStartDay = vardata.strftime("%Y-%m-%d")
        instraDayEndtDay =datetime.now().strftime("%Y-%m-%d")
        fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="C:\delete")
        data = {
            "symbol":symbol,
            "resolution":resolution,
            "date_format":"1",
            "range_from":str(instraDayStartDay),
            "range_to":str(instraDayEndtDay),
            "cont_flag":"1"
        }
        response = fyers.history(data=data)
        return response
    
    def getOHLC(candles):
        # candles = response["candles"]
        candleTime=[]
        open=[]
        high=[]
        low=[]
        close=[]
        for candle in candles:
            candleTime.append(candle[0])
            open.append(candle[1])
            high.append(candle[2])
            low.append(candle[3])
            close.append(candle[4])
        if len(open)==len(close)==len(high)==len(low):
            return open,high,low,close,candleTime
    
    def getDataFrame(candles):
        df = pd.DataFrame(candles, columns =['time', 'open','high','low','close','volume']) 
        return df
    def print(color,period,symbol,message):
        # print(Fore.RED + 'some red text')
        # # print("")
        # print(Fore.RED+' ')
        print(color+'-->'+str(period)+"mins: "+symbol+" "+message)
        # print(message)
        # print(Style.RESET_ALL)
        utility.makeSound()
        
    def printred(period,symbol,message):
        # print(Fore.RED + 'some red text')
        # # print("")
        # print(Fore.RED+' ')
        # print('-->'+str(period)+"mins: "+symbol+" "+message)
        print(Fore.RED+  message)
        # print(Style.RESET_ALL)
        # print(Style.RESET_ALL)
        # utility.makeSound()
    
    def printgreen(period,symbol,message):
        # print(Fore.GREEN+' ')
        # print('-->'+str(period)+"mins: "+symbol+" "+message)
        print(Fore.GREEN+ message)
        # print(Style.RESET_ALL)
        
    def makeSound():
        frequency = 2000
        duration = 50
        winsound.Beep(frequency, duration)
    
    def mtn(x):
        months = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr':4,
            'may':5,
            'jun':6,
            'jul':7,
            'aug':8,
            'sep':9,
            'oct':"O",
            'nov':"N",
            'dec':"D"
            }
        a = x.strip()[:3].lower()
        try:
            ez = months[a]
            # print (ez)
            return ez
        except:
            raise ValueError('Not a month')
    def IsBullishCandle(open,high,low,close):
        if open > close:
            return False
        try:
            oc_hl_ratio_pctg=(math.fabs(open-close)*100/math.fabs(high-low))
        except Exception  as err:
            print(f"Unexpected {err=}, {type(err)=}")
        return (oc_hl_ratio_pctg>50)
    
    def IsBearishCandle(open,high,low,close):
        if open < close:
            return False
        try:
            oc_hl_ratio_pctg=(math.fabs(open-close)*100/math.fabs(high-low))
        except Exception  as err:
            print(f"Unexpected {err=}, {type(err)=}")
        return (oc_hl_ratio_pctg>50)
        