# Task Manager Application

## Description

This is a simple task manager application implemented in Python. It allows users to register, add tasks, view tasks, generate reports, and display statistics.

---

## Clone

To clone this repository, run the following command:

git clone <https://github.com/Elainebarbaraborges/task_manager>

---

## Functions

### 1. Registration

- `reg_user()`: Registers a new user by prompting for a new username and password.

### 2. Adding Tasks

- `add_task()`: Adds a new task to the task list by prompting for task details such as username, title, description, and due date.

### 3. Viewing Tasks

- `view_all()`: Displays all tasks stored in the task list.
- `view_mine(curr_user)`: Displays tasks assigned to the currently logged-in user.

### 4. Reports

- `generate_reports()`: Generates task and user overview reports and saves them to text files.

### 5. Statistics

- `display_statistics()`: Displays statistics including the number of users and tasks.

---

## Parameters

- `curr_user`: The username of the currently logged-in user.

---

## Main Function

The main function to execute the task manager application is `main()`.

---

## Usage

1. Ensure you have Python installed on your system (version 3.x recommended).
2. Before adding new users or tasks, log in with the username `admin` and the password `password`.
3. Install the required dependencies:

pip install -r requirements.txt

4. Run the application by executing the `main.py` file:

python main.py

5. Follow the prompts to register, add tasks, view tasks, generate reports, and display statistics.

---

## Sample Data

- `user.txt`: File to store registered users' credentials.
- `tasks.txt`: File to store task details.

---

## Dependencies

- `os`
- `datetime`

---

## Error Handling

Error handling is implemented for various scenarios such as incorrect user input and file operations. Exceptions are caught and appropriate error messages are displayed to the user.

---

## Created with

This project was created with [HyperionDev](https://www.hyperiondev.com/)
