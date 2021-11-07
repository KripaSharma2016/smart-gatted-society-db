
import sys
sys.path.append('/Users/kripa.sharma/Desktop/my-local-git-repo/smart-gatted-society-db')
from utils.database_connection import *


class SecurityGuardRepo:
    def __init__(self):
        pass

    def signUp(self, infoDict):
        print(">>>. it repo >>>>>")
        print(infoDict)
        # unpack all values and run insert query and return if success else error
        return {"msg": "successfully registered!"}

    def login(self):
        pass

    def resetPassword(self):
        pass

    def forgotPassword(self):
        pass

    def logOut(self):
        pass