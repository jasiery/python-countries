import mysql.connector

class DatabaseConnect():
    
    def __init__(self):
        self.etracker_db_cursor = cursor

    def getEtracker_db(self):
        return self.etracker_db_cursor
    

    def commit_db(self):
        world.commit()

world = mysql.connector.connect(
    host= "localhost", #mysql server host
    user= "root", #mysql server user
    password= "1101", #mysql server password
    database= "world" #database name
) 
cursor = world.cursor() #cursor object for the selected database

