from colorama import Fore
import numpy
import talib

from utility import utility


class ema926cci:
    def check(symbol,period,open,high,low,close,df):
        ema9=talib.EMA(numpy.array(close), timeperiod = 9).tolist()
        ema26=talib.EMA(numpy.array(close), timeperiod = 26).tolist()
        cci = talib.CCI(df.high, df.low,df.close, timeperiod=20)
        lenema9 = len(ema9) 
        lenema26=len(ema26)
        #if cci is down below 80 and 926 +ve, consolidation over on breakout reversal
        if ema9[lenema9-1]>=ema26[lenema26-1] and ema9[lenema9-2]<=ema26[lenema26-2] and cci[len(cci)-1]>(-80) and cci[len(cci)-2]<(-80):
            utility.print(Fore.GREEN,period,symbol,"cci is down below 80 and 926 +ve, consolidation over on breakout reversal.")
        #if cci is above 80 and 926 -ve, consolidation over on breakdown reversal
        if ema9[lenema9-1]<=ema26[lenema26-1] and ema9[lenema9-2]>=ema26[lenema26-2] and cci[len(cci)-1]>80 and cci[len(cci)-2]<80:
            utility.print(Fore.RED,period,symbol,"cci is above 80 and 926 -ve, consolidation over on breakdown reversal")