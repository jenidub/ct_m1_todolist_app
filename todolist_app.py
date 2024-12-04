### PROJECT REQUIREMENTS ###
# ** User Interaction **
# - Use input() to capture user selections and ensure proper input 
# validation to handle invalid choices.

# ** Error Handling **
# - Implement error handling using try, except, else, and finally blocks to catch errors
# - Alert the user if they provide invalid input
# - Alert the user if there are no tasks to view
# - Alert the user if they try to delete a task that doesn't exist
# - Alert the user if they select an option on the main menu that doesn't exist

### PROJECT CODE ###
# Global Variables
# menu_options = ['add', 'view', 'delete', 'quit']
isActive = True

# task_list: the tasks should be stored in a list format
task_list = []

# Functions List
# - Start app
def start_app(user):
    print(f"\nWelcome to the JeniDub To Do List App!".upper())
    print("This app will allow you to add, view, delete tasks so you can stay on track with your life")
    print(f"We hope you enjoy using our app {user}!")
    print("\nLet's get started...")
    
# - Add tasks
def add_task(task_name):
    if task_name:
        task_list.append(task_name.lower().strip())
    else:
        print("You did not enter a task to add. Please try again. Returning to main menu...")
        
# - View tasks
def view_task_list():
    print("\n##########\n")
    print("your current to do list:\n".upper())
    display_task_list()
    print("\n##########\n")

def display_task_list():
    for task in task_list:
        print(f"* {task.title()}")
    
# - Delete tasks
def delete_task(task_name):
    if not task_name:
        print("You did not enter a task to remove. Returning to main menu...\n")
    else:
        for task in task_list:
            if task_name.lower() in task:
                task_index = task_list.index(task_name)
                del task_list[task_index]
                print(f"Success! You have successfully removed {task.title()} from your to-do list")
                return
        print("Invalid entry. Returning to main menu...\n")        

def close_program(user):
    print("\n########## end of program ##########".upper())
    print(f"\nHere are the tasks remaining on your to-do list {user}:")
    display_task_list()
    print("\n##########")
    print(f"Have a nice day {user}! See you again soon!\n")

# MAIN PROGRAM
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
        view_task_list()
    
    # - Delete tasks
    elif task_choice == 'delete':
        view_task_list()
        task_to_remove = input("What task would you like to remove from your to-do list?  ")
        delete_task(task_to_remove)
    
    # # - Invalid entry
    else:
        print('Invalid option. Please try again')

# Close Program
close_program(user_name)

### VALIDATION ###
# ** Code Organization **
# X Organize your code into functions to improve clarity and maintainability. 
# - Use descriptive function names and add comments/docstrings where necessary.

# ** Testing and Debugging **
# - Thoroughly test your application, considering edge cases such as empty lists and invalid input.

### FINAL STEP before SUBMISSION ###
# Create a README.md on the repository that gives information about 
# your project and how to run/use it
