
from timeloop import Timeloop
from datetime import timedelta
from Patterns.BullishEngulfing import BullishEngulfing
from configuration import configuration
from login.login import login
from symbols import symbols


access_token = login.SetupLogin()


tl = Timeloop()
@tl.job(interval=timedelta(seconds=300))
def job_every_5mins():
    BullishEngulfing.Run(configuration.client_id,access_token,symbols.banknifty,5)
    