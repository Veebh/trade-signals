import talib
from utility import utility

class DMI:
    def check(symbol,period,open,high,low,close,df):
        # df = utility.getDataFrame(response["candles"])
        adx = talib.ADX(df.high,df.low,df.close,timeperiod=14)
        lengthadx =len(adx)-1
        adxvalue=adx[lengthadx-1]        
        oldAdxvalue=adx[lengthadx-2]        
        minus_di  = talib.MINUS_DI(df.high,df.low,df.close,timeperiod=14)
        plus_di  = talib.PLUS_DI(df.high,df.low,df.close,timeperiod=14)
        if adxvalue > 22 and oldAdxvalue< 22:
            print(str(period)+"mins: "+symbol+" adx trading above 25: "+str(adxvalue))
            utility.makeSound()
        lengthplus_di = len(plus_di)-1#ignore latest value
        lengthminus_di = len(minus_di)-1#ignore latest value
        if lengthplus_di == lengthminus_di:
            if plus_di[lengthplus_di-1] > minus_di[lengthminus_di-1] and plus_di[lengthplus_di-2] < minus_di[lengthminus_di-2]:
                print(str(period)+"mins: "+symbol+" plus_di is broken up")
                utility.makeSound()                
            if plus_di[lengthplus_di-1] < minus_di[lengthminus_di-1] and plus_di[lengthplus_di-2] > minus_di[lengthminus_di-2]:
                print(str(period)+"mins: "+symbol+" minus_di is broken up")
                utility.makeSound()                
                