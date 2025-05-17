
import webbrowser
from fyers_apiv3 import fyersModel

from configuration import configuration
from fyerutilities import fyerutilities
from login.RefreshToken import RefreshToken
from utility import utility


class AccessToken:
    
    def Get():
        if not fyerutilities.isFileOld(configuration.access_tokenFile,0):
            return utility.readFromFileAsString(configuration.access_tokenFile)
        if not fyerutilities.isFileOld(configuration.refresh_tokenFile,14):
            return RefreshToken.Get()
        return AccessToken.CreateNewToken()
    
    def CreateNewToken():
        session = fyersModel.SessionModel(
            client_id=configuration.client_id,
            secret_key=configuration.secret_key,
            redirect_uri=configuration.redirect_uri, 
            response_type="code")
        response = session.generate_authcode()
        print(response)
        url = response
        webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
        val = webbrowser.get('chrome').open(url)
        auth_code = input("enter authcode: ")
        
        session = fyersModel.SessionModel(
            client_id=configuration.client_id,
            secret_key=configuration.secret_key,
            redirect_uri=configuration.redirect_uri, 
            response_type="code", 
            grant_type="authorization_code"
        )
        session.set_token(auth_code)
        response = session.generate_token()
        access_token=response["access_token"]
        utility.writeToFile(configuration.access_tokenFile,"w",access_token)
        utility.writeToFile(configuration.refresh_tokenFile,"w",response["refresh_token"])
        return access_token