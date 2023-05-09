#*******************************************************************************
#   CS359 Project Part 4
#   File: proj.py
#
#   Notes:
#********************************************************************************

import sqlite3, sys
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def main():

    database = r"proj3db.sqlite"
    create_project_tables(database)
    

if __name__ == '__main__':
    main()
