# This is a simple Python script template
from DatabaseConnection import Query
from Country import Country
from InsertToUser import InsertToUser

def main():
    # queryAll = Query()
    # # raw data from database
    # print(queryAll.getQuery())

    # parse into class
    # countries = []
    # for row in queryAll.getQuery():
    #     countries.append(Country(row[0], row[1], row[2]))

    # for eachCountry in countries:
    #     print(eachCountry.getName())

    user = InsertToUser()
    user.insertUser("adi-pogi", "jai-cute")
    

if __name__ == "__main__":
    main()
