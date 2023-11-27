from DatabaseConnect import DatabaseConnect
import mysql.connector

class InsertToUser:

    def insertUser(self, username, password):
        databaseConnect = DatabaseConnect()
        
        cursor = databaseConnect.getEtracker_db()
        # insert code with params: username and password
        sql = "INSERT INTO etracker_user (user_username, user_password) VALUES ('"+username+"', '"+password+"')" #execute any sql script
        cursor.execute(sql)
        databaseConnect.commit_db()
        print(cursor.rowcount, "record inserted.")
        # queryResult = command.fetchall() #fetch all rows from cursorWorld executed script
        # for row in queryResult:
        #     print(row)
        # print("Hello :"+username)