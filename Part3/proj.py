#*******************************************************************************
#   CS359 Project Part 3
#   File: proj.py
#
#   Notes:
#********************************************************************************

import sqlite3
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


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"proj3db.sqlite"

    sql_create_Video_table =        """ CREATE TABLE IF NOT EXISTS Video (
                                        videoCode       integer PRIMARY KEY NOT NULL,
                                        videoLength     integer NOT NULL
                                    ); """
    sql_create_Model_table =        """ CREATE TABLE IF NOT EXISTS Model (
                                        modelNO         varchar(10) PRIMARY KEY NOT NULL,
                                        width           numeric(6,2),
                                        height          numeric(6,2),
                                        weight          numeric(6,2),
                                        depth           numeric(6,2),
                                        screensize      numeric(6,2)
                                    ); """
    sql_create_Site_table =         """ CREATE TABLE IF NOT EXISTS Site (
                                        siteCode        integer PRIMARY KEY NOT NULL, 
                                        type            varchar(16), 
                                        address         varchar(100),
                                        phone           varchar(16),
                                        site_type       CHECK (type = 'bar'or type ='restaurant')
                                    ); """
    sql_create_DigitalDisplay_table = """ CREATE TABLE IF NOT EXISTS DigitalDisplay (
                                        serialNo        char(10) PRIMARY KEY NOT NULL,
                                        schedulerSystem char(10),
                                        modelNo         char(10),
                                        ss              CHECK (schedulerSystem = 'Random'or schedulerSystem ='Smart' or schedulerSystem ='Virtue'),
                                        FOREIGN KEY     (modelNo) REFERENCES Model (modelNo)
                                    ); """
    sql_create_Client_table =       """ CREATE TABLE IF NOT EXISTS Client (
                                        clientId        integer PRIMARY KEY NOT NULL,
                                        name            varchar(40),
                                        phone           varchar(16),
                                        address         varchar(100)
                                    ); """
    sql_create_TechnicalSupport_table = """ CREATE TABLE IF NOT EXISTS TechnicalSupport (
                                        empId   integer NOT NULL,
                                        name    varchar(40),
                                        gender  char(1)
                                    ); """
# create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create Video table
        create_table(conn, sql_create_Video_table)
        # create Model table
        create_table(conn,sql_create_Model_table)
        # create Site table
        create_table(conn,sql_create_Site_table)
        # create DigitalDisplay table
        create_table(conn,sql_create_DigitalDisplay_table)
        # create Client table
        create_table(conn,sql_create_Client_table)
        # create TechnicalSupport table
        create_table(conn,sql_create_TechnicalSupport_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()