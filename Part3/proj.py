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

def create_project_tables(db_file):
    

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
                                        CHECK           (type = 'Bar'OR type ='Restaurant')
                                    ); """
    sql_create_DigitalDisplay_table = """ CREATE TABLE IF NOT EXISTS DigitalDisplay (
                                        serialNo        char(10) PRIMARY KEY NOT NULL,
                                        schedulerSystem char(10),
                                        modelNo         char(10),
                                        CHECK           (schedulerSystem = 'Random' OR schedulerSystem = 'Smart' OR schedulerSystem = 'Virtue'),
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
                                        CHECK           (class = 'economy' OR class= 'whole day' OR class = 'golden hours')
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
                                        commissionRate   numeric(4,2),
                                        PRIMARY KEY     (clientId, empId, packageId),
                                        FOREIGN KEY     (empId)     REFERENCES Salesman (empId),
                                        FOREIGN KEY     (packageId) REFERENCES AirtimePackage (packageId)
                                    ); """ 
    sql_create_Locates_table =      """ CREATE TABLE IF NOT EXISTS Locates (
                                        serialNo        char(10) NOT NULL,
                                        siteCode        integer NOT NULL,
                                        PRIMARY KEY     (serialNo, siteCode),
                                        FOREIGN KEY     (serialNo)  REFERENCES DigitalDisplay (serialNo),
                                        FOREIGN KEY     (siteCode)  REFERENCES Site (siteCode)
                                    ); """       
# create a database connection
    conn = create_connection(db_file)

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
        # create Locates table
        create_table(conn,sql_create_Locates_table)

    else:
        print("Error! cannot create the database connection.")
        
def insert_data(db_file):
    conn = create_connection(db_file)
    cursor = conn.cursor()

    videoColumns = [(567, 92),
                    (823, 34),
                    (231, 134),
                    (356, 21),
                    (321, 14)]
    cursor.executemany("INSERT INTO Video(videoCode, videoLength) VALUES(?,?)", videoColumns)
    modelColumns = [('ABC4K32', 27.90, 15.70, 20.50, 2.84, 32.00),
                    ('ABC4K40', 34.69, 17.43, 24.30, 3.35, 40.00),
                    ('ABC4K50', 44.20, 25.60, 29.30, 3.50, 50.00),
                    ('ABC4K55', 48.80, 28.40, 39.20, 3.89, 55.00),
                    ('ABC4K60', 53.27, 32.18, 48.23, 4.21, 60.00)]
    cursor.executemany("INSERT INTO Model(modelNo, width, height, weight, depth, screenSize) VALUES(?,?,?,?,?,?)", modelColumns)
    siteColumns = [(23, 'Bar', '34 N 56th St, Phoenix, AZ 85013', '480-555-9623'),
                   (14, 'Restaurant', '12543 N Victory Blvd, Van Nuys, CA 91404', '818-555-0945'),
                   (65, 'Restaurant', '6523 E Katella Blvd, Anaheim, CA 92805', '714-555-5423'),
                   (46, 'Bar', '876 MacArthur Dr, Tempe, AZ 85284', '480-555-2765'),
                   (54, 'Bar', '2876 Sahara Blvd, Las Vegas, NV 89127', '702-555-8723')]
    cursor.executemany("INSERT INTO Site(siteCode, type, address, phone) VALUES(?,?,?,?)", siteColumns)
    digitalDisplayColumns = [('1467367200', 'Virtue', 'ABC4K32'),
                             ('5265360807', 'Random', 'ABC4K50'),
                             ('6083450383', 'Random', 'ABC4K60'),
                             ('9154677989', 'Smart','ABC4K40'),
                             ('1696599316', 'Virtue', 'ABC4K55')]
    cursor.executemany("INSERT INTO DigitalDisplay(serialNo, schedulerSystem, modelNo) VALUES(?,?,?)", digitalDisplayColumns)
    clientColumns = [(56, 'Roberto Martinez', '480-555-0978', '2765 W Mesa Blvd, Tempe, AZ 85284'),
                     (51, 'Colby Butler', '505-555-4321', '654 Ocean Dr, Ventura, CA 93003'),
                     (21, 'Morton Bush', '702-555-1543', '10231 Desert Vista Blvd 89128'),
                     (12, 'Laura Hunnisett', '909-555-2765', '1532 Jackrabbit Ln, 92502'),
                     (65, 'Randell Simonson', '480-555-2134', '654 Cactus Flower Dr, 85283')]
    cursor.executemany("INSERT INTO Client(clientId, name, phone, address) VALUES(?,?,?,?)", clientColumns)
    technicalSupportColumns = [(76, 'Allison', 'F'),
                               (22, 'Louise', 'F'),
                               (89, 'Charnette', 'F'),
                               (26, 'Arlo', 'M'),
                               (78, 'Ivan', 'M')]
    cursor.executemany("INSERT INTO TechnicalSupport(empId, name, gender) VALUES(?,?,?)", technicalSupportColumns)
    administratorColumns = [(7, 'Irene', 'F'),
                            (43, 'Jannette', 'F'),
                            (11, 'Kailey', 'F'),
                            (64, 'Cash', 'M'),
                            (24, 'Kaden', 'M')]
    cursor.executemany("INSERT INTO Administrator(empId, name, gender) VALUES(?,?,?)", administratorColumns)
    salesmanColumns = [(25, 'Frank', 'M'),
                       (26, 'Merton', 'M'),
                       (98, 'Tooru', 'M'),
                       (12, 'Lester', 'M'),
                       (87, 'Frank', 'F')]
    cursor.executemany("INSERT INTO Salesman(empId, name, gender) VALUES(?,?,?)", salesmanColumns)
    airtimePckgColumns = [('3', 'economy', '2023-01-01', '2025-12-31', 60, 321),
                          ('1', 'whole day', '2022-04-15', '2025-1-1', 120, 823),
                          ('2', 'economy', '2022-12-01', '2025-11-31', 60, 567),
                          ('4', 'golden hours', '2020-01-01', '2026-12-31', 180, 356),
                          ('5', 'whole day', '2021-01-01', '2024-12-31', 120, 231)]
    cursor.executemany("INSERT INTO AirtimePackage(packageID, class, startDate, lastDate, frequency, videoCode) VALUES(?,?,?,?,?,?)", airtimePckgColumns)
    admWorkHoursColumns = [(7, '2023-02-14', 8.75),
                           (26, '2022-12-23', 9.75),
                           (87, '2023-12-12', 7.00),
                           (43, '2022-11-23', 10.25),
                           (11, '2023-03-01', 8.25)]
    cursor.executemany("INSERT INTO AdmWorkHours(empId, day, hours) VALUES(?,?,?)", admWorkHoursColumns)
    broadcastsColumns = [(823, 23),
                         (321, 14),
                         (356, 65),
                         (567, 54),
                         (231, 46)]
    cursor.executemany("INSERT INTO Broadcasts(videoCode, siteCode) VALUES(?,?)", broadcastsColumns)
    administersColumns = [(7, 23),
                          (64, 54),
                          (24, 14),
                          (43, 65),
                          (11, 46)]
    cursor.executemany("INSERT INTO Administers(empId, siteCode) VALUES(?,?)", administersColumns)
    specializesColumns = [(76, 'ABC4K32'),
                          (22, 'ABC4K32'),
                          (78, 'ABC4K50'),
                          (89, 'ABC4K55'),
                          (26, 'ABC4K50')]
    cursor.executemany("INSERT INTO Specializes(empId, modelNo) VALUES(?,?)", specializesColumns)
    purchasesColumns = [(56, 25, 1, 6.25),
                        (51, 25, 4, 7),
                        (12, 87, 3, 5.75),
                        (65, 12, 1, 3.5),
                        (21, 98, 2, 10.5)]
    cursor.executemany("INSERT INTO Purchases(clientId, empId, packageId, commissionRate) VALUES(?,?,?,?)", purchasesColumns)
    locatesColumns = [('1467367200', 23),
                      ('5265360807', 54),
                      ('1696599316', 65),
                      ('6083450383', 46),
                      ('9154677989', 14)]
    cursor.executemany("INSERT INTO Locates(serialNo, siteCode) VALUES(?,?)", locatesColumns)
    conn.commit()

def sql_query_one(db_file, street_name):
    
    conn = create_connection(db_file)

    cur = conn.cursor()
    cur.execute('SELECT * FROM Site WHERE address LIKE ?',('%{}%'.format(street_name),))

    rows = cur.fetchall()

    for row in rows:
        print("Site Code: ", row[0])
        print("Type: ", row[1])
        print("Address: ", row[2])
        print("Phone Number: ", row[3])
        print("\n")

def sql_query_two(db_file, scheduler_system):
    
    conn = create_connection(db_file)
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    cursor3 = conn.cursor()

    cursor1.execute('SELECT serialNo,modelNo FROM DigitalDisplay WHERE schedulerSystem=?',('{}'.format(scheduler_system),))
    digital_display_rows = cursor1.fetchall()
    for dd_row in digital_display_rows:
        print("Serial Number: ", dd_row[0])
        print("Model Number: ", dd_row[1])
        cursor2.execute('SELECT empId FROM Specializes WHERE modelNo=?',('{}'.format(dd_row[1]),))        
        specializes_rows = cursor2.fetchall()
        for s_row in specializes_rows:
            cursor3.execute('SELECT name FROM TechnicalSupport WHERE empId=?',('{}'.format(s_row[0]),))
            ts_rows = cursor3.fetchall()
            for ts_row in ts_rows: 
                    print("Technical Support Who Specializes in this model: ", ts_row[0])
        print("\n")

def sql_query_three(db_file):
    
    conn = create_connection(db_file)

    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    cursor3 = conn.cursor()

    cursor1.execute('SELECT DISTINCT name FROM Salesman')

    name_rows = cursor1.fetchall()
    print("Name            cnt")
    print("___________________")
    for n_row in name_rows:
       cursor2.execute('SELECT COUNT(name) FROM Salesman WHERE name=?', ('{}'.format(n_row[0]),))
       count_row = cursor2.fetchone();
       cursor3.execute('SELECT * FROM Salesman WHERE name=?', ('{}'.format(n_row[0]),))
       name_rows = cursor3.fetchall()
       print(n_row[0], "\t\t", count_row[0], name_rows)
    print("\n")


def main():
    database = r"proj3db.sqlite"

    create_project_tables(database)
    insert_data(database)
    #sql_query_one(database, 'sahara')
    #sql_query_two(database, 'Random')
    sql_query_three(database)

if __name__ == '__main__':
    main()
