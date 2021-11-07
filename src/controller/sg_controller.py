
import sys
sys.path.append('/Users/kripa.sharma/Desktop/my-local-git-repo/smart-gatted-society-db')
from src.service.sg_service import SecurityGuardService



class SecurityGuardController:
    def __init__(self):
        pass

    def signUp(self, infoDict):
        # create object of service layer
        sg = SecurityGuardService()
        resp = sg.signUp(infoDict)
        return resp

    def login(self):
        pass

    def resetPassword(self):
        pass

    def forgotPassword(self):
        pass

    def logOut(self):
        pass