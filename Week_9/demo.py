from sqlite3 import *
from os import path


#Create the database
db_name = "demo.db"

def create_database(db_name):
    connection = connect(database=db_name)
    db = connection.cursor()

    db.execute("CREATE TABLE Users(UserId INTEGER UNIQUE primary key AUTOINCREMENT, UserName TEXT);")

    connection.commit()

    db.close
    connection.close()

def add_user_to_database(some_user):

    if not path.exists(db_name):
        print(f"Creating the database {db_name}")
        create_database(db_name)

    #Add things into the database
    connection = connect(database=db_name)
    db = connection.cursor()

    sql_instruction = f"INSERT INTO Users (UserName)VALUES('{some_user}')"

    try:
        db.execute(sql_instruction)
        connection.commit()
        db.close()
        connection.close()
    except:
        print("Something went wrong")
        db.close()
        connection.close()     

def get_users_from_database(db_name):

    connection = connect(database=db_name)
    db = connection.cursor()

    sql_instruction = f"SELECT * FROM Users"

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

# #Demo of try and except:
# try:
#     print(get_users_from_database())
# except TypeError:
#     print("You forgot to put the db_name into the function...you idiot")
# except:
#     print("This is a demo")

# print("The program continues")

def execute_sql_instruction_on_database(db_name, sql_instruction):

    connection = connect(database=db_name)
    db = connection.cursor()

    try:
        db.execute(sql_instruction)
        result = db.fetchall()
        connection.commit()
        db.close()
        connection.close()
    except:
        print("Something went wrong")
        db.close()
        connection.close() 

    return result

print(execute_sql_instruction_on_database(db_name, "CREATE TABLE Animals(UserId INTEGER UNIQUE primary key AUTOINCREMENT, AnimalName TEXT);"))