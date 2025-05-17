from asyncio import sleep
import os

from colorama import Fore
from signals.supertrend import supertrend


from utility import utility


class runsupertrendstrategy:
    def run(symbol,period,open,high,low,close,df,display):
        #get latest trend change on 5mins by index.
        superTrendVals =supertrend.check(symbol,period,open,high,low,close,df)
        length = len(superTrendVals)-1
        if int(close[len(close)-1])<=10:
            return
        if str(superTrendVals[length-1][1])=="up":
            utility.printgreen(
                period,
                display,
                "%s %s\t%s- %s=%s"
                %(display, 
                  str(superTrendVals[length-1][1]),
                  str(int(superTrendVals[length-1][0])).ljust(4),
                  str(int(close[len(close)-1])).ljust(4),
                  str(int(superTrendVals[length-1][0])-int(close[len(close)-1])).ljust(4)))

        elif str(superTrendVals[length-1][1])=="down":
            val =int(superTrendVals[length-1][0])-int(close[len(close)-1])
            utility.printred(
                period,
                display,                
                "%s %s\t%s- %s=%s"
                %(display, 
                  str(superTrendVals[length-1][1]),
                  str(int(superTrendVals[length-1][0])).ljust(4),
                  str(int(close[len(close)-1])).ljust(4),
                    str(val).ljust(4)))
                #   str(7*25*val).ljust(4),
                #   str(7*25*int(superTrendVals[length-1][0])).ljust(4),
                #   str(15*25*val).ljust(4),
                #   str(15*25*int(superTrendVals[length-1][0])).ljust(4)
                #   ))
        # myobj = gTTS(text=text, lang='en', slow=False)
        # myobj.save("welcome.mp3")
        # os.system("start welcome.mp3")
        # sleep(10)
        #get near by strikes to find the change in 5mins by option chain