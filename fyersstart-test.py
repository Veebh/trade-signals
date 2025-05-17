from timeloop import Timeloop
from datetime import timedelta
from configuration import configuration
from fyerutilities import fyerutilities
from login.login import login
from symbols import symbols
from utility import utility

analysistime=15

access_token = login.SetupLogin()

tl = Timeloop()
@tl.job(interval=timedelta(seconds=analysistime))
def job_every_5mins():
    fyerutilities.runTechnicalAnalysis(configuration.client_id,access_token,symbols.banknifty,5)
    fyerutilities.runTechnicalAnalysis(configuration.client_id,access_token,symbols.nifty,5)
    fyerutilities.runTechnicalAnalysis(configuration.client_id,access_token,symbols.finnifty,5)

# @tl.job(interval=timedelta(seconds=analysistime))
# def job_every_5mins():
#     fyerutilities.positiondata(configuration.client_id,access_token)

tl.start()
end=input()

