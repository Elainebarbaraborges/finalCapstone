#=====importing libraries===========
import os
from datetime import datetime, date

# Define the datetime string format
DATETIME_STRING_FORMAT = "%Y-%m-%d"

def reg_user():
    """
    Registers a new user by prompting for a new username and password. 
    If the passwords match and the username doesn't already exist, 
    the new user is added to the user.txt file.
    
    Raises:
        None
    
    Returns:
        None
    """
    try:
        # Prompt for a new username
        while True:
            new_username = input("New Username: ")
            if new_username in username_password:
                print("Username already exists. Please choose a different username:\n")
            else:
                break

        # Prompt for a new password
        while True:
            new_password = input("New Password: ")
            confirm_password = input("Confirm Password: ")

            if new_password == confirm_password:
                print("New user added")
                # Add new user to the username_password dictionary
                username_password[new_username] = new_password

                # Update the user.txt file
                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    out_file.write("\n".join(user_data))
                    break
            else:
                print("Passwords do not match, please try again.\n")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def add_task():
    """
    Adds a new task to the task list. 
    Prompts for task details such as username, title, description, and due date.
    The task is then added to the tasks.txt file.
    
    Raises:
        None
    
    Returns:
        None
    """
    try:
        while True:
            task_username = input("Name of person assigned to task: ")
            if task_username not in username_password.keys():
                print("User does not exist. Please enter a valid username.\n")
            else:
                task_title = input("Title of Task: ")
                task_description = input("Description of Task: ")
                while True:
                    try:
                        task_due_date = input("Due date of task (YYYY-MM-DD): ")
                        due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                        break
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified")

                curr_date = date.today()

                new_task = {
                    "username": task_username,
                    "title": task_title,
                    "description": task_description,
                    "due_date": due_date_time,
                    "assigned_date": curr_date,
                    "completed": False
                }

                task_list.append(new_task)

                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                        ]
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                print("Task successfully added.")
                break
    except Exception as e:
        print(f"An error has occurred: {str(e)}")


def view_all():
    """
    Displays all tasks stored in the task list.
    
    Raises:
        FileNotFoundError: If the tasks.txt file is not found.
        Exception: If an unexpected error occurs during execution.
    
    Returns:
        None
    """
    try:
        for index, task in enumerate(task_list, start=1):
            display_str = f"Task: {index} \t {task['title']}\n"
            display_str += f"Assigned to: \t {task['username']}\n"
            display_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            display_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            display_str += f"Task Description: \n{task['description']}\n"
            display_str += f"Completed: {'Yes' if task['completed'] else 'No'}\n"
            print(display_str)
    except FileNotFoundError:
        print("Error! File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def view_mine(curr_user):
    """
    Displays tasks assigned to the currently logged-in user.
    Allows the user to select a task for completion or editing.
    Args:
        curr_user (str): The username of the currently logged-in user.
    
    Raises:
        None
    
    Returns:
        None
    """
    while True:
        try:
            print("Your Tasks:")
            my_tasks = [task for task in task_list if task["username"] == curr_user]
            if my_tasks:
                for index, task in enumerate(my_tasks, start=1):
                    display_str = f"Task: {index} \t {task['title']}\n"
                    display_str += f"Assigned to: \t {task['username']}\n"
                    display_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                    display_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                    display_str += f"Task Description: \n{task['description']}\n"
                    display_str += f"Completed: {'Yes' if task['completed'] else 'No'}\n"
                    print(display_str)
            else:
                print("You have no tasks.")

            selected_task = input("Enter the number of the task you want to select (or -1 to return to the main menu): ")

            if selected_task.isdigit():
                selected_task_index = int(selected_task) - 1
                if 0 <= selected_task_index < len(my_tasks):
                    selected_task_data = my_tasks[selected_task_index]
                    action = input("Enter 'c' to mark the task as complete or 'e' to edit the task: ").lower()
                    if action == 'c':
                        selected_task_data["completed"] = True
                        with open("tasks.txt", 'w') as task_file:
                            task_file.write("\n".join([f"{task['username']};{task['title']};{task['description']};{task['due_date'].strftime(DATETIME_STRING_FORMAT)};{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if task['completed'] else 'No'}" for task in task_list]))
                        print("Task marked as complete.")
                        break
                    elif action == 'e':
                        if not selected_task_data["completed"]:
                            new_username = input("Enter the new username or press enter to keep the current one: ")
                            selected_task_data["username"] = new_username if new_username else selected_task_data["username"]
                            new_due_date = input("Enter the new due date (YYYY-MM-DD) or press enter to keep the current one: ")
                            if new_due_date:
                                try:
                                    selected_task_data["due_date"] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                                except ValueError:
                                    print("Invalid datetime format. The due date was not changed.")
                            print("Task edited successfully.")
                            break
                        else:
                            print("Completed tasks cannot be edited.")
                    else:
                        print("Invalid action. No changes made.")
                elif selected_task_index == -1:
                    print("Returning to the main menu...")
                    break
                else:
                    print("Invalid task number.")
            else:
                print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")


def generate_reports():
    """
    Generates task and user overview reports and saves them to text files.
    
    Raises:
        None
    
    Returns:
        None
    """
    try:
        # Calculate various statistics
        total_tasks = len(task_list)
        completed_tasks = sum(1 for task in task_list if task['completed'])
        uncompleted_tasks = total_tasks - completed_tasks
        overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'].date() < date.today())

        total_users = len(username_password)
        tasks_per_user = {username: sum(1 for task in task_list if task['username'] == username) for username in username_password}

        # Check for zero tasks per user
        for username, tasks in tasks_per_user.items():
            if tasks == 0:
                print(f"Warning: User '{username}' has zero tasks assigned.")

        tasks_percentage = {username: (tasks_per_user[username] / total_tasks) * 100 for username in username_password}
        completed_percentage = {username: (sum(1 for task in task_list if task['username'] == username and task['completed']) / tasks_per_user[username]) * 100 for username in username_password}
        uncompleted_percentage = {username: 100 - completed_percentage[username] for username in username_password}
        overdue_percentage = {username: (sum(1 for task in task_list if task['username'] == username and not task['completed'] and task['due_date'] < datetime.combine(date.today(), datetime.min.time())) / tasks_per_user[username] * 100 if tasks_per_user[username] > 0 else 0) for username in username_password}

        # Write task overview to file
        with open("task_overview.txt", 'w') as task_overview_file:
            task_overview_file.write("Task Overview\n\n")
            task_overview_file.write(f"Total number of tasks: {total_tasks}\n")
            task_overview_file.write(f"Total number of completed tasks: {completed_tasks}\n")
            task_overview_file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
            task_overview_file.write(f"Total number of overdue tasks: {overdue_tasks}\n")
            task_overview_file.write(f"Percentage of incomplete tasks: {(uncompleted_tasks / total_tasks) * 100}%\n")
            task_overview_file.write(f"Percentage of overdue tasks: {(overdue_tasks / total_tasks) * 100}%\n")

        # Write user overview to file
        with open("user_overview.txt", 'w') as user_overview_file:
            user_overview_file.write("User Overview\n\n")
            user_overview_file.write(f"Total number of users: {total_users}\n")
            for username in username_password:
                user_overview_file.write(f"User: {username}\n")
                user_overview_file.write(f"Total number of tasks assigned: {tasks_per_user[username]}\n")
                user_overview_file.write(f"Percentage of total tasks: {tasks_percentage[username]}%\n")
                user_overview_file.write(f"Percentage of completed tasks: {completed_percentage[username]}%\n")
                user_overview_file.write(f"Percentage of uncompleted tasks: {uncompleted_percentage[username]}%\n")
                user_overview_file.write(f"Percentage of overdue tasks: {overdue_percentage[username]}%\n\n")

        print("Reports generated successfully!\n")
    except Exception as e:
        print(f"An error occurred while generating reports: {str(e)}")


def display_statistics():
    """
    Displays statistics including the number of users and tasks.
    
    Raises:
        None
    
    Returns:
        None
    """
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    print('-' * 44)
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print('-' * 44)


def main():
    """
    Main function to execute the task manager application.
    Handles user authentication, menu navigation, and function calls.
    
    Raises:
        None
    
    Returns:
        None
    """
    # Check if tasks.txt exists, if not create it
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass

    # Read task data from tasks.txt and populate task_list
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    global task_list
    task_list = []
    for t_str in task_data:
        curr_t = {}
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False
        task_list.append(curr_t)

    # If user.txt doesn't exist, create it with a default account
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    # Read user data from user.txt and populate username_password dictionary
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    global username_password
    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    # Prompt user for login credentials
    logged_in = False
    while not logged_in:
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True

    print("\nWelcome to Task Manager")
    while True:
        print("Select one of the following options below:")
        print('-' * 44)
        print("""r  - Registering a user
a  - Adding a task
va - View all tasks
vm - View my tasks
ds - Display statistics
gr - Generate reports
e  - Exit""")
        print('-' * 44)
        menu = input('- ').lower()

        # Execute the selected menu option
        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine(curr_user)
        elif menu == 'ds':
            display_statistics()
        elif menu == 'gr':
            generate_reports()
        elif menu == 'e':
            print("Goodbye!!!")
            exit()
        else:
            print("You have made a wrong choice. Please try again.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
