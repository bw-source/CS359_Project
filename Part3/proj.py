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

    sql_create_Video_table = """ CREATE TABLE IF NOT EXISTS Video (
                                        videoCode integer PRIMARY KEY NOT NULL,
                                        videoLength integer NOT NULL
                                    ); """

    sql_create_Model_table = """ CREATE TABLE IF NOT EXISTS Model (
                                        modelNO varchar(10) PRIMARY KEY NOT NULL,
                                        width numeric(6,2),
                                        height numeric(6,2),
                                        weight numeric(6,2),
                                        depth numeric(6,2),
                                        screensize numeric(6,2)
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create Video table
        create_table(conn, sql_create_Video_table)
        # create Model table
        create_table(conn,sql_create_Model_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()