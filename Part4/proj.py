#*******************************************************************************
#   CS359 Project Part 4
#   File: proj.py
#
#   Notes:
#********************************************************************************

import sqlite3, os
from sqlite3 import Error


#*******************************************************************************
#   get_fileName()
#   Purpose: Prompt user for filename of database
#
#   Param: None
#   Return: Filename of database
#********************************************************************************

def get_db_fileName():

    db_filename = input("What is the name of the SQLite3 database: ")

    return db_filename

#*******************************************************************************
#   get_db_fileName()
#   Purpose: Create a database connection to the SQLite database
#   Param db_file: database filename
#   Return: Connection object or None
#
#********************************************************************************

def create_Connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

#*******************************************************************************
#   create_Connection(db_file)
#   Purpose: Close a database connection
#   Param db_conn: database connection
#   Return: None
#********************************************************************************

def close_connection(db_conn):

    try:
        db_conn.close()
    except Error as e:
        print(e)

#*******************************************************************************
#   userTopLevelMenu()
#   Purpose: Create a Top Level User Menu
#   Param: None
#   Return: None
#********************************************************************************

def userTopLevelMenu():

    userInput = ''
    db_connection = None

    while userInput.upper() != 'Q':
        print("1.  Login")
        print("Q.  Quit")
        userInput = input("? ")
    
        if userInput == '1':
            db_fileName = get_db_fileName()
            db_connection = create_Connection(db_fileName)

        elif userInput.upper() == 'Q':
            continue        

    if db_connection != None:
        close_connection(db_connection)


def main():

    userTopLevelMenu()
    

if __name__ == '__main__':
    main()
