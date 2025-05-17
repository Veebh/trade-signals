from datetime import datetime
import pandas as pd
from utility import utility

class BullishEngulfing:
    
    def Run(client_id,access_token,symbol,period):
        response=utility.getData(client_id,access_token,symbol,period)
        open,high,low,close = utility.getOHLC(response["candles"])
        length = len(open)
        for number in range(length):
            BullishEngulfing.IdentifyPattern(symbol, period, open, high, low, close, number)

    def IdentifyPattern(symbol, period, open, high, low, close, number):
        bullish = utility.IsBullishCandle(open[number],high[number],low[number],close[number])
        boring = utility.IsBullishCandle(open[number-1],high[number-1],low[number-1],close[number-1])
        bearish = utility.IsBearishCandle(open[number-2],high[number-2],low[number-2],close[number-2])
        if bullish and boring and bearish:
            print(symbol +" BullishEngulfing: "+period)
            
    def check(symbol,period,open,high,low,close,candleTime,df):
        # open,high,low,close = utility.getOHLC(response["candles"])
        length = len(open)
        for number in range(length):
            BullishEngulfing.IsTweezerTops(symbol, period, open, high, low, close,candleTime, number)
    
    def IsTweezerTops(symbol, period, open, high, low, close,candleTime, number):
        # latest candle
        latestCandleIsBearish = utility.IsBearishCandle(open[number],high[number],low[number],close[number])
        # previous candle
        previousCandleIsBullish = utility.IsBullishCandle(open[number-1],high[number-1],low[number-1],close[number-1])
        if latestCandleIsBearish and previousCandleIsBullish:
            if open[number-1] > close[number]:
                print(symbol +" Tweezer Tops identified: "+str(period) +"  "+str(datetime.fromtimestamp(candleTime[number]).strftime("%A, %B %d, %Y %I:%M:%S")))