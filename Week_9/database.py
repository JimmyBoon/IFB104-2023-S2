from sqlite3 import *
from os import path

def create_title_database(db_name):
    connection = connect(database=db_name)
    db = connection.cursor()

    db.execute("CREATE TABLE Titles(TitleId INTEGER UNIQUE primary key AUTOINCREMENT, Title TEXT);")

    connection.commit()

    db.close
    connection.close()

def add_title_to_database(db_name, title):

    if not path.exists(db_name):
        print(f"Creating the database {db_name}")
        create_title_database(db_name)

    #Add things into the database
    connection = connect(database=db_name)
    db = connection.cursor()

    sql_instruction = f"INSERT INTO Titles (Title)VALUES('{title}')"

    try:
        db.execute(sql_instruction)
        connection.commit()
        db.close()
        connection.close()
    except:
        print("Something went wrong")
        db.close()
        connection.close() 

def get_titles_from_database(db_name):

    connection = connect(database=db_name)
    db = connection.cursor()

    sql_instruction = f"SELECT * FROM Titles"

    try:
        db.execute(sql_instruction)
        result = db.fetchall()
        db.close()
        connection.close()
    except:
        print("Something went wrong")
        db.close()
        connection.close() 

    return result