### PROJECT REQUIREMENTS ###
# ** Error Handling **
# - Implement error handling using try, except, else, and finally blocks to catch errors

### VARIABLES and FUNCTIONS ###
## Global Variables List ##
# isActive: determines whether the app should continue to run after each step
isActive = True 

# task_list: the tasks should be stored in a list format
task_list = []

## Functions List ##
# => Start App Function
def start_app(user):
    """ Display the opening messages for the app including a personalized welcome message to {user} """
    print(f"\nWelcome to the JeniDub To Do List App!".upper())
    print("This app will allow you to add, view, delete tasks so you can stay on track with your life")
    print(f"We hope you enjoy using our app {user}!")
    print("\nLet's get started...")
    
# => Add Tasks Function
def add_task(task_name):
    """ Append the user input {task_name} to the global variable task_list """
    if task_name:
        task_list.append(task_name.lower().strip())
        
    # - Alert the user if they provide invalid input
    else:
        print("You did not enter a task to add. Please try again. Returning to main menu...")
        
# => View To Do List Function
def view_todo_list():
    """ Check if the task_list is empty """
    """ If the list is empty, send a message stating that the list is empty """
    """ Else, display a formatted title and run display_task_list """
    
    # - Alert the user if there are no tasks to view
    if not task_list:
        print("\nThere are no tasks in your to-do list. Returning to main menu...\n")
    else:
        print("\n##########\n")
        print("your current to do list:\n".upper())
        display_task_list()
        print("\n##########\n")

# => Display Tasks in To Do List Function
def display_task_list():
    """ Display a formatted list of tasks from the global variable task_list """
    for task in task_list:
        print(f"* {task.title()}")
    
# - Delete Tasks Function
def delete_task(task_name):
    """ Check if the task_name entry is empty """
    """ If task_name is empty, print a message then return to the main menu """
    """ Else, iterate through task_list to see if the task is in the list """
    """ => if the task is in task_list, delete it from the list and print a confirmation message """
    """ => if the task is not in task_list, print an invalid entry message and return to the main menu """

    # - Alert the user if they provide invalid input
    if not task_name:
        print("You did not enter a task to remove. Returning to main menu...\n")
    
    else:
        for task in task_list:
            if task_name.lower() in task:
                task_index = task_list.index(task_name)
                del task_list[task_index]
                print(f"Success! You have successfully removed {task.title()} from your to-do list")
                return
            
        # - Alert the user if they try to delete a task that doesn't exist
        # The message occurs if the task is not found during iteration of task_list
        print("Invalid entry. Returning to main menu...\n")        

# - Delete Tasks Function
def close_app(user):
    """ Display the closing messages for the app depending if the task_list is empty """
    """ => If task_list is populated, print out a final list of tasks """
    """ => If task_list is empty, print out a 'no items' message """
    print("\n########## end of program ##########".upper())
    if task_list:
        print(f"\nHere are the tasks remaining on your to-do list {user}:")
        display_task_list()
    else:
        print("\nThere are no items remaining on your to-do list")
    print("\n##########")
    print(f"\nHave a nice day {user}! See you again soon!\n")

### MAIN PROGRAM ###
# Welcome users to the JeniDub To Do App
# Get user's name
user_name = input("Welcome! What is your name? ").title()

# Display customized welcome message
start_app(user_name)

# Run the app until the user types in the keyword 'quit'
while isActive:
    # Displays a menu with options to add, view, delete tasks, quit the application.
    task_choice = input("=> Type in one of the following options: [ add | view | delete | quit ]  ").lower()
    
    # Core Features via Function
    # - Quit the application
    if task_choice == 'quit':
        isActive = False
        break
    
    # - Add tasks
    elif task_choice == 'add':
        new_task = input("What task would you like to add to your to-do list?  ")
        add_task(new_task)
    
    # - View tasks
    elif task_choice == 'view':
        view_todo_list()
    
    # - Delete tasks
    elif task_choice == 'delete':
        view_todo_list()
        task_to_remove = input("What task would you like to remove from your to-do list?  ")
        delete_task(task_to_remove)
    
    # # - Invalid entry
    # - Alert the user if they select an option on the main menu that doesn't exist
    else:
        print('Invalid option. Returning to main main...\n')

# Close Program
close_app(user_name)

### VALIDATION ###
# ** Testing and Debugging **
# - Thoroughly test your application, considering edge cases such as empty lists and invalid input.

### FINAL STEP before SUBMISSION ###
# Create a README.md on the repository that gives information about 
# your project and how to run/use it
