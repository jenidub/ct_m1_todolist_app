# JeniDub To-Do List App

Welcome to the **JeniDub To-Do List App**, a simple command-line interface (CLI) application written in Python. This app allows users to manage their daily tasks effectively by providing features to add, view, delete tasks, and quit the application.

---

## Features
- **Add Task**: Easily add tasks to your to-do list.
- **View Tasks**: Display all tasks in a formatted list.
- **Delete Task**: Remove tasks from your list when completed.
- **Exit Program**: Quit the application gracefully.

The app includes user-friendly error handling and displays clear messages for invalid input or actions.

---

## Requirements
- Python 3.6 or later.

---

## How to Run
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `todolist_app.py`.
4. Run the application by typing:
   ```
   python todolist_app.py
   ```
5. Follow the on-screen prompts to:
   - Add a new task.
   - View your current to-do list.
   - Delete tasks.
   - Exit the application by typing `quit`.

---

## Usage
Upon running the program, you will be greeted with a personalized welcome message. The app will continuously run until you choose to quit by typing `quit`. Here’s a quick guide to the commands:

- **Add**: Type `add` and then enter the task you want to add.
- **View**: Type `view` to display the current tasks in your list.
- **Delete**: Type `delete` to remove a task from the list. You will be prompted to specify which task to remove.
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
- Invalid inputs are handled with descriptive messages.
- If no tasks exist, appropriate messages inform the user.
- Graceful handling for invalid task deletions or empty task additions.

---

## Customization
Feel free to customize the app to suit your needs. You can modify the global variables or extend the functionality by adding more commands.

---

## License
This project is open-source and available under the MIT License.
