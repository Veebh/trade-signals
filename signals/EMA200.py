from colorama import Fore
import numpy

import talib

from utility import utility


class EMA200:
    def check(symbol,period,open,high,low,close,df):
        # print("200DMA start: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])        
        # open,high,low,close = utility.getOHLC(response["candles"])
        ema200=talib.EMA(
               numpy.array(close), timeperiod = 200).tolist()
        emaLength = len(ema200)-1
        latestClose = close[emaLength-1]
        previousClose = close[emaLength-2]
        if latestClose > ema200[emaLength-1] and previousClose < ema200[emaLength-2]:
            utility.print(Fore.GREEN,period,symbol,"Latest close is above 200 EMA")
        if latestClose < ema200[emaLength-1] and previousClose > ema200[emaLength-2]:
            utility.print(Fore.RED,period,symbol,"Latest close is below 200 EMA")