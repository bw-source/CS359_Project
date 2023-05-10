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

    print("*************************************************************************")
    print(f"*{'*' : >72}")
    print(f"*{'Digital Display Database Interface System' : ^71}*")
    print(f"*{'*' : >72}")
    print("*************************************************************************")

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

        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'Digital Display Database Interface System' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")

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
            return        
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
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'Digital Display Database Interface System' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")
        print("1. Display all the digital displays")
        print("2. Search digital displays")
        print("3. Add a new digital display")
        print("4. Edit an exisiting digital display")
        print("5. Delete and existing digital display") 
        print("Q. Quit and log out of current database")

        userInput = input("? ")

        if (userInput == '1'):
            display_digital_displays(db_conn)
        elif (userInput == '2'):
            search_by_scheduler_system(db_conn)
        elif (userInput == '3'):
            return_state = '1'
            while (return_state != '0'):
                return_state = insert_new_digital_display(db_conn)
        elif (userInput == '4'):
            update_digital_display(db_conn)
        elif (userInput == '5'):
            delete_digital_display(db_conn)

        elif (userInput.upper() == 'Q'):
            return
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
    print(f"*{'*' : >72}")
    print(f"*{'Digital Display Database Interface System' : ^71}*")
    print(f"*{'*' : >72}")
    print("*************************************************************************")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print(f"*{'Serial Number:' : ^23}*{'Scheduler System:' : ^23}*{'Model Number:' : ^23}*")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print("*************************************************************************")
    for row in digitalDisplay_rows:
        print(f"*{row[0] : ^23}*{row[1] : ^23}*{row[2] : ^23}*")
        print("*************************************************************************")

    input("Press enter to continue")

#*******************************************************************************
#   search_by_scheduler_system(db_conn)
#   Purpose: Display all digital displays currently in entered database
#            that have selected scheduler system
#   Param: Database Connection
#   Return: None
#********************************************************************************

def search_by_scheduler_system(db_conn):

    cursor1 = db_conn.cursor()
    user_input = ''

    while (user_input == ''):
        clear_screen()
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'Digital Display Database Interface System' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")
        print("Please select the scheduler system you with to search for:")
        print("1: Random")
        print("2: Smart")
        print("3: Virtue") 
        user_input = input("? ")

    
        if (user_input == '1'):
            scheduler = 'Random'
        elif (user_input == '2'):
            scheduler = 'Smart'
        elif (user_input == '3'):
            scheduler = 'Virtue'
        else:
            print("Invalid entry.")
            input("Press enter to continue")
            user_input = ''

    cursor1.execute('SELECT * FROM DigitalDisplay WHERE schedulerSystem=?',('{}'.format(scheduler),))
    digitalDisplay_rows = cursor1.fetchall()
    clear_screen()
    
    print("*************************************************************************")
    print(f"*{'*' : >72}")
    print(f"*{'Digital Display Database Interface System' : ^71}*")
    print(f"*{'*' : >72}")
    print("*************************************************************************")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print(f"*{'Serial Number:' : ^23}*{'Scheduler System:' : ^23}*{'Model Number:' : ^23}*")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print("*************************************************************************")
    for row in digitalDisplay_rows:
        print(f"*{row[0] : ^23}*{row[1] : ^23}*{row[2] : ^23}*")
        print("*************************************************************************")

    input("Press enter to continue")

#*******************************************************************************
#   insert_new_digital_display(db_conn)
#   Purpose: Insert new digital display in entered database
#   Param: Database Connection
#   Return: Return state
#********************************************************************************

def insert_new_digital_display(db_conn):

    serial_number = ''

    while (len(serial_number) != 10):
        clear_screen()

        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'Digital Display Database Interface System' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'New Digital Display Insertion' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")
        print()
        print("Please enter the digital display's serial number:")
        serial_number = input("?")
        if (len(serial_number) != 10):
            print("Please enter a ten character serial number.")
            input("Press enter to continue.")

    user_input = ''

    while ((user_input != '1') and (user_input != '2') and (user_input != '3')):
        clear_screen()
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'Digital Display Database Interface System' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'New Digital Display Insertion' : ^71}*")
        print(f"*{'*' : >72}")
        print(f"* {'Serial number: ' + serial_number : <70}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")

        print()
        print("Please select the digital display's scheduler system:")
        print()
        print("1: Random")
        print("2: Smart")
        print("3: Virtue") 
        user_input = input("? ")

        if (user_input == '1'):
            scheduler = 'Random'
        elif (user_input == '2'):
            scheduler = 'Smart'
        elif (user_input == '3'):
            scheduler = 'Virtue'
        else:
            print("Please enter a valid entry.")
            input("Press enter to continue.")

    model_number = ''
    while (len(model_number) == 0):
        clear_screen()
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'Digital Display Database Interface System' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'New Digital Display Insertion' : ^71}*")
        print(f"*{'*' : >72}")
        print(f"* {'Serial number: ' + serial_number : <70}*")
        print(f"* {'Scheduler systen: ' + scheduler : <70}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")

        print()
        print("Please enter the model number of the digital display: ")
        model_number = input("? ")

        if (len(model_number) == 0):
            print("Please enter a valid entry.")
            input("Press enter to continue.")


    user_continue = ''
    while (user_continue.upper() != 'Y') and (user_continue.upper() != 'N'):
        clear_screen()
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'Digital Display Database Interface System' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'New Digital Display Insertion' : ^71}*")
        print(f"*{'*' : >72}")
        print(f"* {'Serial number: ' + serial_number : <70}*")
        print(f"* {'Scheduler systen: ' + scheduler : <70}*")
        print(f"* {'Model number: ' + model_number : <70}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")

        print()
        print("Is this okay?")
        print("Y: Press Y to continue.")
        print("N: Press N to start over.")
        user_continue = input("? ")

        if (user_continue.upper() == 'Y'):
            break
        elif (user_continue.upper() == 'N'):
            return '1'
        else:
            print("Please enter a valid entry.")
            input("Press enter to continue.")

    cursor1 = db_conn.cursor()

    new_digital_display = [(serial_number),(scheduler),(model_number)]
    cursor1.execute("INSERT INTO DigitalDisplay(serialNo, schedulerSystem, modelNo) VALUES(?,?,?)", new_digital_display)
    db_conn.commit()

    display_digital_displays(db_conn)

    return '0'

#*******************************************************************************
#   delete_digital_display(db_conn)
#   Purpose: Delete digital display in entered database
#   Param: Database Connection
#   Return: Return state
#********************************************************************************

def delete_digital_display(db_conn):
    
    cursor1 = db_conn.cursor()
    delete_display = 'DELETE FROM DigitalDisplay WHERE serialNo=?'

    clear_screen()

    cursor1.execute('SELECT * FROM DigitalDisplay')
    digitalDisplay_rows = cursor1.fetchall()
    
    print("*************************************************************************")
    print(f"*{'*' : >72}")
    print(f"*{'Digital Display Database Interface System' : ^71}*")
    print(f"*{'*' : >72}")
    print("*************************************************************************")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print(f"*{'Serial Number:' : ^23}*{'Scheduler System:' : ^23}*{'Model Number:' : ^23}*")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print("*************************************************************************")
    for row in digitalDisplay_rows:
        print(f"*{row[0] : ^23}*{row[1] : ^23}*{row[2] : ^23}*")
        print("*************************************************************************")

    print("Enter the serial number of the digital display you want to delete.")
    serial_number = input("? ")    

    

    cursor1.execute(delete_display, (serial_number,))
    db_conn.commit()

    clear_screen()
    display_digital_displays(db_conn)



#*******************************************************************************
#   update_digital_display(db_conn)
#   Purpose: Update digital display field values in entered database
#   Param: Database Connection
#   Return: None
#********************************************************************************

def update_digital_display(db_conn):

    cursor1 = db_conn.cursor()
    cursor1.execute('SELECT * FROM DigitalDisplay')
    digitalDisplay_rows = cursor1.fetchall()

    clear_screen()
     
    print("*************************************************************************")
    print(f"*{'*' : >72}")
    print(f"*{'Digital Display Database Interface System' : ^71}*")
    print(f"*{'*' : >72}")
    print("*************************************************************************")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print(f"*{'Serial Number:' : ^23}*{'Scheduler System:' : ^23}*{'Model Number:' : ^23}*")
    print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
    print("*************************************************************************")
    for row in digitalDisplay_rows:
        print(f"*{row[0] : ^23}*{row[1] : ^23}*{row[2] : ^23}*")
        print("*************************************************************************")

    print("Enter the serial number of the digital display you want to update.")
    serial_number = input("? ")    
    cursor1.execute('SELECT * FROM DigitalDisplay WHERE serialNo=?',('{}'.format(serial_number),))
    digitalDisplay_rows = cursor1.fetchall()

    user_input = ''

    while (user_input == ''):
        clear_screen()
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'Digital Display Database Interface System' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")
        print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
        print(f"*{'Serial Number:' : ^23}*{'Scheduler System:' : ^23}*{'Model Number:' : ^23}*")
        print(f"*{'*' : >24}{'*' : >24}{'*' : >24}")
        print("*************************************************************************")
        for row in digitalDisplay_rows:
            print(f"*{row[0] : ^23}*{row[1] : ^23}*{row[2] : ^23}*")
            print("*************************************************************************")

        print("Please select what you would like to update")
        print("1: Serial Number")
        print("2: Scheduler System")
        print("3: Model Number")
        print("Q: Cancel editing and return to menu") 
        user_input = input("? ")

        if (user_input == '1'):
            update_field = 'Serial Number'
        elif (user_input == '2'):
            update_field = 'Scheduler System'
        elif (user_input == '3'):
            update_field = 'Model Number'
        elif (user_input.upper() == 'Q'):
            return
        else:
            print("Invalid entry.")
            input("Press enter to continue")
            user_input = ''

    user_input = ''

    while (user_input == ''):
        clear_screen()
        print("*************************************************************************")
        print(f"*{'*' : >72}")
        print(f"*{'Digital Display Database Interface System' : ^71}*")
        print(f"*{'*' : >72}")
        print("*************************************************************************")

        if (update_field == 'Serial Number'): 
            
            print()
            print("What would you like the new value for " + update_field + " to be?")
            new_serial_number = input("? ")
                    
            if (len(new_serial_number) != 10):
                print("Please enter a ten character serial number.")
                input("Press enter to continue.")
            else:
                clear_screen()
                print("*************************************************************************")
                print(f"*{'*' : >72}")
                print(f"*{'Digital Display Database Interface System' : ^71}*")
                print(f"*{'*' : >72}")
                print("*************************************************************************")
                print()
                print("Is the value " + new_serial_number + " for the field " + update_field + " okay?") 
                
                print("Y: Press Y to continue.")
                print("N: Press N to reenter the serial number.")
                print("Q: Press Q to quit and return to the menu")
                user_input = input("? ")
                
                if (user_input.upper() == 'Y'):
                     sql = ''' UPDATE DigitalDisplay
                               SET serialNo = ? 
                               WHERE serialNo = ?'''
                     cursor1.execute(sql, (new_serial_number, serial_number))
                     db_conn.commit()
                     display_digital_displays(db_conn)     
                elif (user_input.upper() == 'N'):
                    user_input = ''
                elif (user_input.upper() == 'Q'):
                    return
                else:
                    print("Please enter a valid entry.")
                    input("Press enter to continue.")
       
        elif (update_field == 'Scheduler System'): 
            print("Please select the digital display's scheduler system:")
            print()
            print("1: Random")
            print("2: Smart")
            print("3: Virtue") 
            user_input = input("? ")

            if (user_input == '1'):
                scheduler = 'Random'
            elif (user_input == '2'):
                scheduler = 'Smart'
            elif (user_input == '3'):
                scheduler = 'Virtue'
            else:
                print("Please enter a valid entry.")
                input("Press enter to continue.")
                user_input = ''
                continue
            
            print("Is the value " + scheduler + " for the field " + update_field + " okay?") 
            print("Y: Press Y to continue.")
            print("N: Press N to choose again.")
            print("Q: Press Q to quit and return to the menu")

            user_input = input("? ")
            
            if (user_input.upper() == 'Y'):              
                sql = ''' UPDATE DigitalDisplay
                          SET schedulerSystem = ? 
                          WHERE serialNo = ?'''
                cursor1.execute(sql, (scheduler, serial_number))
                db_conn.commit()
                display_digital_displays(db_conn)                
            elif (user_input.upper() == 'N'):
                user_input = ''
            elif (user_input.upper() == 'Q'):
                return
            else:
                print("Please enter a valid entry.")
                input("Press enter to continue.")
        elif (update_field == 'Model Number'): 
            print()
            print("What would you like the new value for " + update_field + " to be?")
            new_model_number = input("? ")
                    
            if (len(new_model_number) == 0):
                print("Please enter a valid model number.")
                input("Press enter to continue.")
            else:
                print("Is the value " + new_model_number + " for the field " + update_field + " okay?") 
                print("Y: Press Y to continue.")
                print("N: Press N to reenter the model number.")
                print("Q: Press Q to quit and return to the menu")
                user_input = input("? ")
                
                if (user_input.upper() == 'Y'):
                    sql = '''  UPDATE DigitalDisplay
                               SET modelNo = ? 
                               WHERE serialNo = ?'''
                    cursor1.execute(sql, (new_model_number, serial_number))
                    db_conn.commit()
                    display_digital_displays(db_conn)    
                elif (user_input.upper() == 'N'):
                    user_input = ''
                elif (user_input.upper() == 'Q'):
                    return
                else:
                    print("Please enter a valid entry.")
                    input("Press enter to continue.")









#*******************************************************************************
#   main()
#********************************************************************************

def main():

    userTopLevelMenu()
    clear_screen()
    

if __name__ == '__main__':
    main()
