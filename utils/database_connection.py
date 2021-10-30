#it will provide database connection.

import psycopg2

class MainDataBase:
    def __init__(self):
        self.conn = None
        self.cur = None

    def createConnection(self):
        """ i will create connection with postgresql database."""
        try:
            self.conn = psycopg2.connect(
                        host='localhost',
                        port=54320,
                        dbname='testing',
                        user='postgres',
                        password='admin',
                    )
        except Exception as ex:
            print("Not able to connect to db", ex)
        else:
            print("connection establish successfully")
        self.cur = self.conn.cursor()

    def insertQuery(self, sqlQuery):
        """ It will execute queries... """
        errorMsg = ""
        if self.cur != None:
            try:
                self.cur.execute(sqlQuery)
            except Exception as ex:
                errorMsg = "Error while executing query", str(ex)
                print(errorMsg)
                return errorMsg
            else:
                print("Query successfully executed!")
                return errorMsg
        else:
            print("Cursor have no connection!")
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


if __name__ == "__main__":
    mydb = MainDataBase()
    #sql1 = "CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);"
    mydb.createConnection()
    #data = mydb.executeQuery(sql1)
    """print(data)
    sql2 = "INSERT INTO test (num, data) VALUES (100, 'abcd')"
    data = mydb.executeQuery(sql2)
    print(data)
    mydb.commitQuery()
    mydb.closeConnection()"""
    mydb.createConnection()
    sql3 = "SELECT * FROM test;"
    data = mydb.fetchQuery(sql3)
    print(data)