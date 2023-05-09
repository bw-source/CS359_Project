#*******************************************************************************
#   CS359 Project Part 4
#   File: proj.py
#
#   Notes:
#********************************************************************************

import sqlite3, sys
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

def main():

    db_fileName = get_db_fileName()
    db_connection = create_Connection(db_fileName)
    close_connection(db_connection)

if __name__ == '__main__':
    main()
