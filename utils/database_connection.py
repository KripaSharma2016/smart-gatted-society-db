#it will provide database connection.

import psycopg2
import sys
sys.path.append('../')
from getlogs.logger import logs
from configs.config_loader import ConfigLoader

class MainDataBase:
    def __init__(self):
        self.conn = None
        self.cur = None

    def createConnection(self):
        """ i will create connection with postgresql database."""
        errorMsg = ""
        logs.info("create connection started")
        config = ConfigLoader()
        host, port, dbname, user, pwd = config.getKeys()
        try:
            self.conn = psycopg2.connect(
                        host=host,
                        port=port,
                        dbname=dbname,
                        user=user,
                        password=pwd,
                    )
        except Exception as ex:
            errorMsg = "Not able to connect to db"
            logs.error(errorMsg)
            return errorMsg
        else:
            logs.info("connection establish successfully")
        self.cur = self.conn.cursor()

        return errorMsg

    def insertQuery(self, sqlQuery):
        """ It will execute queries... """
        errorMsg = ""
        logs.info("insert query started")
        if self.cur != None:
            try:
                self.cur.execute(sqlQuery)
            except Exception as ex:
                errorMsg = "Error while executing query" + str(ex)
                logs.error(errorMsg)
                return errorMsg
            else:
                logs.info("Query successfully executed!")
                return errorMsg
        else:
            logs.info("Cursor have no connection!")
            return errorMsg

    def fetchQuery(self, sqlQuery):
        """ It will execute queries... """
        if self.cur != None:
            try:
                self.cur.execute(sqlQuery)
                result = self.cur.fetchone()
            except Exception as ex:
                print("Error while executing query", str(ex))
                return None
            else:
                print("Query successfully executed!")
                return result
        else:
            print("Cursor have no connection!")
            return None

    def commitQuery(self):
        self.conn.commit()

    def closeConnection(self):
        self.cur.close()
        self.conn.close()


"""if __name__ == "__main__":
    mydb = MainDataBase()
    #sql1 = "CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);"
    mydb.createConnection()
    #data = mydb.executeQuery(sql1)
    print(data)
    sql2 = "INSERT INTO test (num, data) VALUES (100, 'abcd')"
    data = mydb.executeQuery(sql2)
    print(data)
    mydb.commitQuery()
    mydb.closeConnection()
    mydb.createConnection()
    sql3 = "SELECT * FROM test;"
    data = mydb.fetchQuery(sql3)
    print(data)"""