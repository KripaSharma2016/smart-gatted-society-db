
import sys
sys.path.append('/Users/kripa.sharma/Desktop/my-local-git-repo/smart-gatted-society-db')
from src.repository.sg_repo import SecurityGuardRepo



class SecurityGuardService:
    def __init__(self):
        pass

    def signUp(self, infoDict):
        # create object of repo
        sg = SecurityGuardRepo()
        rsp = sg.signUp(infoDict)

        return rsp

    def login(self):
        pass

    def resetPassword(self):
        pass

    def forgotPassword(self):
        pass

    def logOut(self):
        pass