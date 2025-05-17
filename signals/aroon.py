from colorama import Fore
import talib
from utility import utility


class aroon:
    
    def check(symbol,period,open,high,low,close,df):
        # df = utility.getDataFrame(response["candles"])
        ar_down,ar_up  = talib.AROON(df.high.values, df.low.values, 14)
        length = len(ar_up)-1
        if length != len(ar_down)-1:
            print("error in calculating aroon values")
            return
        if ar_up[length-1] > ar_down[length-1] and ar_up[length-2] < ar_down[length-2]:
            utility.print(Fore.GREEN,period,symbol,"aroon up broke above.")
        if ar_up[length-1] < ar_down[length-1] and ar_up[length-2] > ar_down[length-2]:
            utility.print(Fore.RED,period,symbol,"aroon down broke above.")
        if ar_up[length-1] > 80 and ar_up[length-2]<=80:
            utility.print(Fore.GREEN,period,symbol,"aroon up is "+str(ar_up[length-1]))
        if ar_down[length-1] > 80 and ar_down[length-2]<=80:
            utility.print(Fore.GREEN,period,symbol,"aroon down is "+str(ar_down[length-1]))