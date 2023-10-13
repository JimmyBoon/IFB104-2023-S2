from sqlite3 import *
from os import path
from re import fullmatch

#Creating a database:
db_name = "my_database.db"

def create_database(db_name):
    if bool(fullmatch("[A-Za-z0-9_]+\.db", db_name)) == False:
        print("What are you doing? We need a file name ending in db")
        return

    if path.exists(db_name):
        print("Database is already created...have a nice day")
        return

    try:
        connection = connect(database=db_name)
        db = connection.cursor()

        db.execute("CREATE TABLE Movies(MovieId INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT, MovieTitle TEXT, MovieYear INT);")

        connection.commit()
    except Exception as error:
        print("Something went wrong creating the DB")
        print(error)
    
    finally:
        print("Cleaning up")
        db.close()
        connection.close()


create_database(db_name)
