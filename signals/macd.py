from colorama import Fore
import numpy
import talib


class macd:
    
    def check(symbol,period,open,high,low,close,df):
        # open,high,low,close = utility.getOHLC(response["candles"])
        macd, signal, hist = talib.MACD(
               numpy.array(close), fastperiod=12, slowperiod=26, signalperiod=9)
        arrayLength = len(hist)-1
        if hist[arrayLength-1] >0 and hist[arrayLength-2] <0:
            print(str(period)+"mins: "+symbol+" buy on macd")
        if hist[arrayLength-1] <0 and hist[arrayLength-2] >0:
            print(str(period)+"mins: "+symbol+" sell on macd")