from colorama import Fore
import numpy
import talib
from utility import utility


class EMA9_26:
    def check(symbol,period,open,high,low,close,df):
        # open,high,low,close = utility.getOHLC(response["candles"])
        ema9=talib.EMA(numpy.array(close), timeperiod = 9).tolist()
        ema26=talib.EMA(numpy.array(close), timeperiod = 26).tolist()
        lenema9 = len(ema9) -1
        lenema26 = len(ema26) -1
        if ema9[lenema9-1]>=ema26[lenema26-1] and ema9[lenema9-2]<=ema26[lenema26-2]:
            utility.print(Fore.GREEN,period,symbol,"ema9 crosses above ema26")
        if ema9[lenema9-1]<=ema26[lenema26-1] and ema9[lenema9-2]>=ema26[lenema26-2]:
            utility.print(Fore.RED,period,symbol,"ema9 falls below ema26")