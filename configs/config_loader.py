# it will load json values into python objects


import json
from types import SimpleNamespace

class ConfigLoader:
    def __init__(self):
        self.config = None
        jsonData = ""
        try:
            with open('/Users/kripa.sharma/Desktop/smart-gated-society-db/configs/config.json') as fd:
                jsonData = fd.read()
        except Exception as ex:
            print("error", ex)
        else:
            self.config = json.loads(jsonData, object_hook=lambda d: SimpleNamespace(**d))

    def getKeys(self):
        key1 = self.config.postgresqldb_docker_test
        key2 = self.config.postgresqldb_docker_postgres
        return self.return_values(key2)

    def return_values(self, mainKey):
        return mainKey.host, mainKey.port, mainKey.dbname, mainKey.user, mainKey.password

