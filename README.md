# Task Manager App

This is a command-line application that allows users to manage tasks. Users can register new users, add tasks, view all tasks, view tasks assigned to them, and generate reports. The application supports authentication, with an admin user having additional functionality.

## Getting Started

To run the application, you need to have Python installed on your machine. Clone the repository and navigate to the project directory.

```shell
$ git clone <repository-url>
$ cd task-manager-app
```

## Prerequisites

Make sure you have Python 3.x installed on your machine.

## Usage

To start the application, run the following command:

```shell
$ python task_manager.py
```

### Login

When prompted, enter your username and password to log in to the application. The username and password are case-sensitive.

### Menu Options

Once logged in, you will see a menu with the following options:

- `r`: Register a new user (admin only)
- `a`: Add a new task
- `va`: View all tasks
- `vm`: View my tasks
- `ds`: View statistics (admin only)
- `gr`: Generate reports (admin only)
- `e`: Exit the application

#### Register a New User (`r`)

Only the admin user can register new users. If you are logged in as admin, choose this option to register a new user. You will be prompted to enter the username and password for the new user. Make sure the username is unique.

#### Add a New Task (`a`)

Choose this option to add a new task. You will be prompted to assign the task to a user, enter a task name, provide a task description, and specify the due date. The current date will be automatically assigned as the task's assigned date. Note that the user must exist in the system.

#### View All Tasks (`va`)

Select this option to view all tasks. All tasks in the system will be displayed, including the assigned user, task name, assigned date, due date, and completion status.

#### View My Tasks (`vm`)

Choose this option to view tasks assigned to you. Only tasks assigned to your username will be displayed. The task's assigned user, task name, assigned date, due date, and completion status will be shown.

You can also choose a task from the list to edit its due date or mark it as completed.

#### View Statistics (`ds`)

This option is only available to the admin user. It displays statistics about the tasks in the system, including the total number of tasks, the number of completed tasks, and the number of incomplete tasks.

#### Generate Reports (`gr`)

The admin user can generate reports on task and user overviews. This option allows you to generate reports that summarize the tasks and users in the system. The reports will be saved in the `task_overview.txt` and `user_overview.txt` files, respectively.

### Exiting the Application (`e`)

To exit the application, choose this option. You will be logged out, and the program will terminate.

## Data Files

The application uses the following data files:

- `user.txt`: Stores user information (username and password)
- `tasks.txt`: Stores task information (assigned user, task name, description, assigned date, due date, and completion status)
- `task_overview.txt`: Generated report file containing task overviews
- `user_overview.txt`: Generated report file containing user overviews

Make sure these files are present in the same directory as the application script.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the application, feel free to open a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

This task manager app was inspired by the need for a simple and efficient way to manage tasks in a command-line environment. It serves as a basic foundation that can be expanded upon to meet specific requirements.
