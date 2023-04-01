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
                                        CHECK (type = 'bar'or type ='restaurant')
                                    ); """
    sql_create_DigitalDisplay_table = """ CREATE TABLE IF NOT EXISTS DigitalDisplay (
                                        serialNo        char(10) PRIMARY KEY NOT NULL,
                                        schedulerSystem char(10),
                                        modelNo         char(10),
                                        CHECK (schedulerSystem = 'Random'or schedulerSystem ='Smart' or schedulerSystem ='Virtue'),
                                        FOREIGN KEY     (modelNo) REFERENCES Model (modelNo)
                                    ); """
    sql_create_Client_table =       """ CREATE TABLE IF NOT EXISTS Client (
                                        clientId        integer PRIMARY KEY NOT NULL,
                                        name            varchar(40),
                                        phone           varchar(16),
                                        address         varchar(100)
                                    ); """
    sql_create_TechnicalSupport_table = """ CREATE TABLE IF NOT EXISTS TechnicalSupport (
                                        empId           integer PRIMARY KEY NOT NULL,
                                        name            varchar(40),
                                        gender          char(1)
                                    ); """
    sql_create_Administrator_table = """ CREATE TABLE IF NOT EXISTS Administrator (
                                        empId           integer PRIMARY KEY NOT NULL,
                                        name            varchar(40),
                                        gender          char(1)
                                    ); """
    sql_create_Salesman_table =     """ CREATE TABLE IF NOT EXISTS Salesman (
                                        empId           integer PRIMARY KEY NOT NULL,
                                        name            varchar(40),
                                        gender          char(1)
                                    ); """
    sql_create_AirtimePackage_table = """ CREATE TABLE IF NOT EXISTS AirtimePackage (
                                        packageId       integer PRIMARY KEY NOT NULL,
                                        class           varchar(16),
                                        startDate       date,
                                        lastDate        date,
                                        frequency       int,
                                        videoCode       int,
                                        CHECK (class ='economy' or class='whole day' or class ='golden hours')
                                    ); """
    sql_create_AdmWorkHours_table = """ CREATE TABLE IF NOT EXISTS AdmWorkHours (
                                        empID           integer NOT NULL,
                                        day             date NOT NULL,
                                        hours           numeric(4,2),
                                        PRIMARY KEY     (empID, day),
                                        FOREIGN KEY     (empId) REFERENCES Administrator (empId)
                                    ); """
    sql_create_Broadcasts_table =   """ CREATE TABLE IF NOT EXISTS Broadcasts (
                                        videoCode       integer NOT NULL,
                                        siteCode        int NOT NULL,
                                        PRIMARY KEY     (videoCode, siteCode),
                                        FOREIGN KEY     (videoCode) REFERENCES Video (videoCode),
                                        FOREIGN KEY     (siteCode)  REFERENCES Site (siteCode)
                                    ); """
    sql_create_Administers_table =  """ CREATE TABLE IF NOT EXISTS Administers (
                                        empId           integer NOT NULL, 
                                        siteCode        integer NOT NULL,
                                        PRIMARY KEY     (empId, siteCode),
                                        FOREIGN KEY     (empId)     REFERENCES Administrator (empId),
                                        FOREIGN KEY     (siteCode)  REFERENCES Site (siteCode)
                                    ); """
    sql_create_Specializes_table =  """ CREATE TABLE IF NOT EXISTS Specializes (
                                        empId           integer NOT NULL,
                                        modelNo         char NOT NULL,
                                        PRIMARY KEY     (empId, modelNo),
                                        FOREIGN KEY     (empId)     REFERENCES TechnicalSupport (empId),
                                        FOREIGN KEY     (modelNo)   REFERENCES Model (modelNo)
                                    ); """
    sql_create_Purchases_table =    """ CREATE TABLE IF NOT EXISTS Purchases (
                                        clientId        integer NOT NULL,
                                        empId           integer NOT NULL,
                                        packageId       integer NOT NULL,
                                        commisionRate   numeric(4,2),
                                        PRIMARY KEY     (clientId, empId, packageId),
                                        FOREIGN KEY     (empId)     REFERENCES Salesman (empId),
                                        FOREIGN KEY     (packageId) REFERENCES AirtimePackage (packageId)
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
        # create Administrator table
        create_table(conn,sql_create_Administrator_table)
        # create Salesman table
        create_table(conn,sql_create_Salesman_table)
        # create AirtimePackage table
        create_table(conn,sql_create_AirtimePackage_table)
        # create AdmWorkHours table
        create_table(conn,sql_create_AdmWorkHours_table)
        # create Broadcasts table
        create_table(conn,sql_create_Broadcasts_table)
        # create Administraters table
        create_table(conn,sql_create_Administers_table)
        # create Specializes table
        create_table(conn,sql_create_Specializes_table)
        # create Purchases table
        create_table(conn,sql_create_Purchases_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()