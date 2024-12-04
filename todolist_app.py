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
# task_list: the tasks should be stored in a list format
task_list = []
isActive = True

# Functions List
# - Add tasks
def add_task():
    # if task_name:
    print('adding user added task now...')
        
# - View tasks
def view_task_list():
    print(task_list)
    
# - Delete tasks
def delete_task():
    # if task_name:
    print('deleting user added task now...')

# Project Code
# Welcome users to the JeniDub To Do App
# Get user's name

# Display customized welcome message
print("\nWelcome to the JeniDub To Do List App!".upper())
print("This app will allow you to add, view, delete tasks so you can stay on track with your life")
print("We hope you enjoy using our app!")
print("\nLet's get started...")

# Run the app until the user types in the keyword 'quit'
while isActive:
    # Displays a menu with options to add, view, delete tasks, quit the application.
    task_choice = input("=> Type in one of the following options: [ add | view | delete | quit ]  ").lower()

    # Core Features via Function
    # - Quit the app
    if task_choice == 'quit':
        isActive = False
        break
    
    # - Add tasks
    elif task_choice == 'add':
        add_task()
    
    # - View tasks
    elif task_choice == 'view':
        view_task_list()
    
    # - Delete tasks
    elif task_choice == 'delete':
        delete_task()
    
    # - Invalid entry
    else:
        # - Quit the application
        print('invalid entry. try again')

# Close Program
print("\n########## end of program ##########".upper())
print("\nHere was the final list:")
print(task_list)

print("\n##########")
print(f'Have a nice day! See you again soon!\n')


### VALIDATION ###
# ** Code Organization **
# - Organize your code into functions to improve clarity and maintainability. 
# - Use descriptive function names and add comments/docstrings where necessary.

# ** Testing and Debugging **
# - Thoroughly test your application, considering edge cases
# such as empty lists and invalid input.

### FINAL STEP before SUBMISSION ###
# Create a README.md on the repository that gives information about 
# your project and how to run/use it
