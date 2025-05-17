import sys
from login.login import login
from timeloop import Timeloop
from datetime import timedelta
from configuration import configuration
from fyerutilities import fyerutilities
from symbols import symbols
from utility import utility



access_token = login.SetupLogin()

tl = Timeloop()
@tl.job(interval=timedelta(seconds=300))
def job_every_5mins():
    sys.stdout.write(".")
    sys.stdout.flush()
    fyerutilities.runTechnicalAnalysis(configuration.client_id,access_token,symbols.banknifty,5)
    fyerutilities.runTechnicalAnalysis(configuration.client_id,access_token,symbols.nifty,5)
    fyerutilities.runTechnicalAnalysis(configuration.client_id,access_token,symbols.finnifty,5)
    
@tl.job(interval=timedelta(seconds=900))
def job_every_15mins():
    sys.stdout.write(".")
    sys.stdout.flush()
    fyerutilities.runTechnicalAnalysis(configuration.client_id,access_token,symbols.banknifty,15)
    fyerutilities.runTechnicalAnalysis(configuration.client_id,access_token,symbols.banknifty,15)
    fyerutilities.runTechnicalAnalysis(configuration.client_id,access_token,symbols.finnifty,15)
    

tl.start()
end=input()
