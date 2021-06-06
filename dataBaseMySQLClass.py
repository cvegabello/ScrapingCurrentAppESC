import pymysql
from pymysql import Error

class DataBase:
    def __init__(self) -> None:
        try:
            self.connection = pymysql.connect(
                host = '10.5.165.52',
                port = 3306,
                user= 'opsNY',
                password= '',
                db= 'boardinfony'
            )
            self.cursor = self.connection.cursor()
            print("connection successful")
        except Error as ex:
            print("Connection error:", ex)
    
    def select_returnOneRecord(self, sqlStr):
        try:
            self.cursor.execute(sqlStr)
            record = self.cursor.fetchone()
            return record

        except Exception as e:
            raise

    def queryNoRecords(self, sqlStr):
        try:
            self.cursor.execute(sqlStr)
            self.connection.commit()
        except Exception as e:
            raise

    def execStoreProcNoRecords(self, spStr, Arg):
        try:
            self.cursor.callproc(spStr,Arg)
            self.connection.commit()
            
        except Exception as e:
            raise


    def close(self):
        self.connection.close()
        
