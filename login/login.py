
from fyerutilities import fyerutilities
from login.AccessToken import AccessToken
from utility import utility


class login:

    def SetupLogin():
        access_token = AccessToken.Get()
        return access_token