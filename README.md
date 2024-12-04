# JeniDub To-Do List App

Welcome to the **JeniDub To-Do List App**
A simple command-line interface (CLI) application written in Python where the user can use text commands to run the app.

---

## Features
- **Add Task**: Easily add tasks to your to-do list.
- **View Tasks**: Display all tasks in a formatted list.
- **Delete Task**: Remove tasks from your list when completed.
- **Quit Program**: Quit the application.

The app includes user-friendly error handling and displays clear messages for invalid input or actions.

---

## Requirements
- Python 3.6 or later.

---

## How to Run
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
4. Run the application by typing (select the proper command based on your Python version):
   ```
   python3 todolist_app.py
   ```
   or
   ```
   python todolist_app.py
   ```

---

## Usage
Upon running the program, you will be greeted with a personalized welcome message. The app will continuously run until you choose to quit by typing `quit`. Here’s a quick guide to the commands:

- **Add**: Type `add` and then enter the task you want to add.
- **View**: Type `view` to display the current tasks in your list.
- **Delete**: Type `delete` to remove a task from the list.
- **Quit**: Type `quit` to exit the application.

### Example
```text
Welcome! What is your name? John

WELCOME TO THE JENIDUB TO DO LIST APP!
This app will allow you to add, view, delete tasks so you can stay on track with your life.
We hope you enjoy using our app John!

Let's get started...
=> Type in one of the following options: [ add | view | delete | quit ]
add
What task would you like to add to your to-do list? Buy groceries

=> Type in one of the following options: [ add | view | delete | quit ]
view

##########

YOUR CURRENT TO DO LIST:
* Buy Groceries

##########

```

---

## Error Handling
- Invalid inputs, invalid task deletions or empty task additions are handled with descriptive messages.
- If no tasks exist, a message will inform the user.

---

## README file generated with assistance using ChatGPT
