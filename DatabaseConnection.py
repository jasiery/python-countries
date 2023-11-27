import mysql.connector

class Query():

    def __init__(self):
        self.query = queryResult

    def getQuery(self):
        return self.query

world = mysql.connector.connect(
    host= "localhost", #mysql server host
    user= "root", #mysql server user
    password= "1101", #mysql server password
    database= "world" #database name
)

cursorWorld = world.cursor() #cursor object for the selected database
cursorWorld.execute("SELECT Code, Name, Continent FROM country") #execute any sql script
queryResult = cursorWorld.fetchall() #fetch all rows from cursorWorld executed script

sql = "INSERT INTO etracker_user (user_username, user_password) VALUES ('adi', 'adi password')"
cursorWorld.execute(sql)
world.commit()
