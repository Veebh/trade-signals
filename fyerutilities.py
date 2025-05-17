import csv
import webbrowser
import numpy
import requests
from datetime import datetime 
from fyers_api import accessToken

import os

import talib
from Patterns.BullishEngulfing import BullishEngulfing
from customsignals.run.supertrend.runsupertrendstrategy import runsupertrendstrategy
from customsignals.strategies.ema926cci import ema926cci
from configuration import configuration
from signals.ema9_26 import EMA9_26
from signals.supertrend import supertrend
from signals.macd import macd
from utility import utility

class fyerutilities:
    
    def isFileOld(filePath,dayCount):
        if os.path.exists(filePath):
            createdTime =os.path.getmtime(filePath)
            dt_m = datetime.fromtimestamp(createdTime)
            return (datetime.now().date()- dt_m.date()).days>dayCount
        else:
            return True
    
    # def positiondata(client_id,access_token):
    #     response=utility.getPositions(client_id,access_token)
    #     print(response)
    #     # fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="c:")
    #     # fyers_api.positions()
    #     print()
    def runSuperTrendStrategy(client_id,access_token,symbol,period,display):
        response=utility.getData(client_id,access_token,symbol,period)
        open,high,low,close = utility.getOHLC(response["candles"])
        df = utility.getDataFrame(response["candles"])
        runsupertrendstrategy.run(symbol,period,open,high,low,close,df,display)
        
    

    def runTechnicalAnalysis(client_id,access_token,symbol,period):
        # sys.stdout.write(".")
        # sys.stdout.flush()
        # print(str(datetime.now().strftime("%H:%M:%S,%f")))
        response=utility.getData(client_id,access_token,symbol,period)
        open,high,low,close,candleTime = utility.getOHLC(response["candles"])
        df = utility.getDataFrame(response["candles"])
        # macd.check(symbol,period,open,high,low,close,df)
        # # EMA200.check(symbol,period,open,high,low,close,df)
        # supertrend.check(symbol,period,open,high,low,close,df)
        # # DMI.check(symbol,period,open,high,low,close,df)
        # # aroon.check(symbol,period,open,high,low,close,df)
        # EMA9_26.check(symbol,period,open,high,low,close,df)
        # # cci.check(symbol,period,open,high,low,close,df)
        # ema926cci.check(symbol,period,open,high,low,close,df)
        # # print(str(datetime.now().strftime("%H:%M:%S,%f")))
        BullishEngulfing.check(symbol,period,open,high,low,close,candleTime,df)

    def getStockData(row, access_token,symbol,numberOfDays,period):
            # sys.stdout.write(".")
            # sys.stdout.flush()
            # print(str(datetime.now().strftime("%H:%M:%S,%f")))
            response=utility.getData(configuration.client_id,access_token,symbol,numberOfDays,period)
            open,high,low,close,candleTime = utility.getOHLC(response["candles"])
            # df = utility.getDataFrame(response["candles"])
            emas=talib.EMA(numpy.array(close), timeperiod = 15).tolist()
            row265 = []
            try:
                latestClose = close[len(close)-1]
                ema20Val =emas[len(emas)-20]
                ema65Val =emas[len(emas)-65]
                ema200Val =emas[len(emas)-200]
                if latestClose>ema20Val and ema20Val > ema65Val and ema65Val> ema200Val:
                    row265 = [symbol,str(round(latestClose,1)),str(round(ema20Val,1)),str(round(ema65Val,1)),str(round(ema200Val,1)),str(round((ema20Val-ema65Val+ema65Val-ema200Val)*100/latestClose,1))]
                    return row265
            except:
                a=100
                # print("An exception occurred "+str(row))
            return row265
        
