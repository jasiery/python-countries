from DatabaseConnect import DatabaseConnect
import mysql.connector

class InsertToUser:

    def insertUser(self, username, password):
        databaseConnect = DatabaseConnect()
        
        command = databaseConnect.getEtracker_db()
        # insert code with params: username and password
        sql = "INSERT INTO etracker_user (user_username, user_password) VALUES ('"+username+"', '"+password+"')" #execute any sql script
        command.execute(sql)
        databaseConnect.commit_db()
        # queryResult = command.fetchall() #fetch all rows from cursorWorld executed script
        # for row in queryResult:
        #     print(row)
        print("Hello :"+username)