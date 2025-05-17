from colorama import Fore
import talib
from utility import utility


class cci:
    def check(symbol,period,open,high,low,close,df):
        # df = utility.getDataFrame(response["candles"])
        
        cci = talib.CCI(df.high, df.low,df.close, timeperiod=20)
        length = len(cci)-1
        if cci[length-1]>80 and cci[length-2]<80:
            utility.print(Fore.YELLOW,period,symbol,"CCI at breakout range, watch other indicator to find trade "+str(cci[length-1]))
        if cci[length-1]>(-80) and cci[length-2]<(-80):
            utility.print(Fore.YELLOW,period,symbol,"CCI at breakout range, watch other indicator to find trade "+str(cci[length-1]))       