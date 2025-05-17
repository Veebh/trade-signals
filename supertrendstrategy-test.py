



import calendar
from datetime import datetime, timedelta

import numpy
from configuration import configuration
from fyerutilities import fyerutilities
from symbols import expiryWeekNumber, symbols
from utility import utility
from timeloop import Timeloop


access_token = fyerutilities.getaccess_token()
# wait = input("wait for market opening or not True/False: ")
# utility.waitTillMarketOpenForFiveMinCandles(wait)
tl = Timeloop()
@tl.job(interval=timedelta(seconds=60))
def job_every_5mins():
    
    fyerutilities.runSuperTrendStrategy(configuration.client_id,access_token,symbols.banknifty,5)
    #latest banknifty index value
    response = utility.getQuotes(configuration.client_id,access_token,symbols.banknifty)
    cmp = response["d"][0]["v"]["lp"];    
    # print(cmp)
    strikesToWatch = []
    today = datetime.now().date()
    monthName = utility.mtn(calendar.month_name[today.month])
    strike =symbols.bankniftyweeklyexpiry+str(today.strftime("%Y"))[2:]+str(monthName)+str(expiryWeekNumber.nextWeek)
    for number in range(10):
        Cestrike=strike+str(int(numpy.floor((cmp+number*100) / 100.0) * 100))+"CE"
        strikesToWatch.append(Cestrike)
    for number in range(10):
        Pestrike=strike+str(int(numpy.floor((cmp-number*100) / 100.0) * 100))+"PE"
        strikesToWatch.append(Pestrike)
    for strike in strikesToWatch:
        fyerutilities.runSuperTrendStrategy(configuration.client_id,access_token,strike,5)
        
tl.start()
end=input()
