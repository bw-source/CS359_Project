#*******************************************************************************
#   CS359 Project Part 4
#   File: proj.py
#
#   Notes:
#********************************************************************************

import sqlite3, os
from sqlite3 import Error
from os import system, name

#*******************************************************************************
#   clear_screen()
#   Purpose: Clear the screen of the OS's terminal
#
#   Param: None
#   Return: None
#********************************************************************************

# define our clear function
def clear_screen():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#*******************************************************************************
#   get_fileName()
#   Purpose: Prompt user for filename of database
#
#   Param: None
#   Return: Filename of database
#********************************************************************************

def get_db_fileName():

    db_filename = input("What is the filename of the Digital Display Database: ")

    return db_filename

#*******************************************************************************
#   get_db_fileName()
#   Purpose: Create a database connection to the SQLite database
#   Param db_file: database filename
#   Return: Connection object or None
#
#********************************************************************************

def create_Connection(db_file):

    db_conn = None
    check_file = os.path.isfile(db_file)
    if check_file:
        try:
            db_conn = sqlite3.connect(db_file)
            return db_conn
        except Error as e:
            print(e)
    else:
        return None

    return db_conn

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


    while (userInput.upper() != 'Q'):
        clear_screen()
        print("1.  Log into Digital Display Database System")
        print("Q.  Quit the program")
        userInput = input("? ")
    
        if userInput == '1':
            clear_screen()
            db_fileName = get_db_fileName()
            db_connection = create_Connection(db_fileName)
            if db_connection != None:
                userSubLevelMenu(db_connection)
                close_connection(db_connection)
            else:
                print("Please enter a valid database filename.")
                input("Press enter to continue.")
        elif userInput.upper() == 'Q':
            continue        
        else:
            print("Please enter valid input.")
            input("Press enter to continue.")

    

#*******************************************************************************
#   userSubLevelMenu()
#   Purpose: Create a Sub Level User Menu
#   Param: None
#   Return: None
#********************************************************************************

def userSubLevelMenu(db_conn):

    userInput = ''

    while (userInput.upper() != 'Q'):
        clear_screen()
        print("1. Display all the digital displays")
        print("2. Search digital displays")
        print("3. Add a new digital display")
        print("4. Edit an exisiting digital display")
        print("5. Delete and existing digital display") 
        print("Q. Quit and log out of current database")

        userInput = input("? ")

        if (userInput == '1'):
            display_digital_displays(db_conn)
        elif (userInput.upper == 'Q'):
            continue
        else:
            print("Please enter a valid input")
            input("Press enter to continue")

#*******************************************************************************
#   display_digital_displays(db_conn)
#   Purpose: Display all digital displays currently in entered database
#   Param: Database Connection
#   Return: None
#********************************************************************************

def display_digital_displays(db_conn):

    clear_screen()

    cursor1 = db_conn.cursor()
    cursor1.execute('SELECT * FROM DigitalDisplay')
    digitalDisplay_rows = cursor1.fetchall()
    
    
    print("*************************************************************************")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print(f"*{'Serial Number:' : ^23}*{'Scheduler System:' : ^23}*{'Model Number:' : ^23}*")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print("*************************************************************************")
    for row in digitalDisplay_rows:
        print(f"*{row[0] : ^23}*{row[1] : ^23}*{row[2] : ^23}*")
        print("*************************************************************************")

    input("Press enter to continue")



def main():

    userTopLevelMenu()
    clear_screen()
    

if __name__ == '__main__':
    main()
