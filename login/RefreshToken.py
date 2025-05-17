



import requests
from configuration import configuration
from utility import utility


class RefreshToken:
    def Get():
        refresh_token= utility.readFromFileAsString(configuration.refresh_tokenFile)
        url = configuration.tokenUrl
        myobj = {
        "grant_type": "refresh_token",
        "appIdHash": configuration.appIdHash,
        "refresh_token": refresh_token,
        "pin": configuration.pin
        }
        response = requests.post(url, json = myobj)
        access_token=response.json()["access_token"]
        utility.writeToFile(configuration.access_tokenFile,"w",access_token)
        return access_token