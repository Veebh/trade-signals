from colorama import Fore
from customsignals.TechnicalSignals import TechnicalSignals
from utility import utility


class supertrend:
    
    def check(symbol,period,open,high,low,close,df):
        # df = utility.getDataFrame(response["candles"])
        superTrendVals = TechnicalSignals.supertrend(df,3,10)
        superTrendValues = superTrendVals.to_numpy()
        length = len(superTrendVals)-1
        if int(close[len(close)-1])<=10:
            return superTrendValues
        if superTrendValues[length-1][1] != superTrendValues[length-2][1]:
            if superTrendValues[length-1][1] == "up":
                utility.print(Fore.GREEN,period,symbol," super trend value changed..i.e: "+str(superTrendValues[length-1][1]))
            if superTrendValues[length-1][1] == "down":
                    utility.print(Fore.RED,period,symbol," super trend value changed..i.e: "+str(superTrendValues[length-1][1]))
        return superTrendValues
            # utility.makeSound()