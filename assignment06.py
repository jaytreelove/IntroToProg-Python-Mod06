# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# JPlemons,5.20.2020,Modified code to complete assignment 6
# JPlemons,5.21.2020, Second Draft
# JPlemons,5.22.2020, Finishing Touches
# JPlemons,5.23.2020, Proof-read and final edit
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
file = None  # An object that represents a file
row = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
choice = ""  # Captures the user option selection
task = ""  # Captures the user task data
priority = ""  # Captures the user priority data
task_check = ""  # a string boolean to test if task is in list
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds a task to the list of dictionary rows
        :param task: (string) name of task to be completed
        :param priority: (string)
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows
        """
        list_of_rows.append({"Task": task, "Priority": priority})
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes a task from the list of dictionary rows
        :param task: (string) name of task to be removed
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows
        """
        task_check = False
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():
                strData = True
                lstTable.remove(row)
                print(f"\nCongrats on a job well done! {task.capitalize()} has been removed.")
                continue
        if not task_check:
            print(f"\n{task.capitalize()} not found, you must have completed it earlier.")
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Saves the list of tasks to text file
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "w")
        for line in lstTable:
            file.write(f"{line['Task']}, {line['Priority']}\n")
        file.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
****** Menu of Options *******
      1) Add a New Task
       2) Remove Task
        3) Save File        
         4) Reload
          5) Exit
******************************
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = input("Which option would you like to perform? [1 to 5] - ").strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n********* To-Do List *********")
        print("       Task --- Priority")
        print("      -------------------")
        for row in list_of_rows:
            print("       " + row["Task"] + " --- " + row["Priority"])
        print("******************************")
        # print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gets the task and priority from user
        :return: task and priority
        """
        task = input("What do you need to accomplish? ")
        priority = input("What is the priority level? ")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Gets the task that is completed to remove from the list
        :return: task
        """
        task = input("Which task have you completed? ")
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(task, priority, lstTable)
        IO.input_press_to_continue(strStatus)

    elif strChoice == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        Processor.remove_data_from_list(task, lstTable)
        IO.input_press_to_continue(strStatus)

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
            print("\nSaving Data...")
            print("Your To-Do list has been saved.")
        else:
            IO.input_press_to_continue("Save Cancelled!")

    elif strChoice == '4':  # Reload Data from File
        print("WARNING: Unsaved Tasks Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':  # to confirm user wants to reload
            Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")

    elif strChoice == '5':  # Exit Program
        print("WARNING: Unsaved Tasks Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to exit? (y/n) -  ")
        if strChoice.lower() == 'y':  # To confirm user is ready to exit program
            print("\nGoodbye! Go out there and complete these tasks!\n")
            break  # and Exit
        else:
            IO.input_press_to_continue("Exit Cancelled!")

    else: # to be displayed in user types anything other than 1-5
        print("You have unlocked the secret menu!")
        print("Actually there is nothing to see here.  Please select 1-5 only.")
