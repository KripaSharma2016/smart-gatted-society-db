# it will test database_connection file
# TDD : (Test Data Driven approach)

import unittest
from database_connection import *

class TestMainDataBase(unittest.TestCase):

    def test_create_connection_is_working(self):
        #create object of class
        mydb = MainDataBase()
        expectedResult = ""
        response = mydb.createConnection()
        self.assertEqual(expectedResult, response)
        mydb.closeConnection()

    """def test_create_connection_is_not_working(self):
            #create object of class
            mydb = MainDataBase()
            expectedResult = "Not able to connect to db"
            response = mydb.createConnection()
            self.assertEqual(expectedResult, response)
            mydb.closeConnection() """


if __name__ == '__main__':
    unittest.main()
