#=====importing libraries===========
import datetime

#=====functions======

def reg_user(new_user, new_password):
       #write the new user onto the user.txt document
        with open("user.txt", "a") as user_file:
            user_file.write(new_user + ", " + new_password + "\n")

        #tell the user that the new user has been added
        print(f"\n{new_user} has now been added as a user.")

        #update the user list to prevent the user adding the same user twice in a session
        user_dict.update({new_user: new_password})
def add_task(task_assign_user, task_name, task_description, current_date, task_due_date):
     #add the data to the task.txt file
    with open("tasks.txt", "a") as task_file:
        task_file.write(task_assign_user + ", " + task_name + ", " + task_description + ", " + current_date + ", " + task_due_date + ", No\n")
        
    #let the user know that this has happened
    print(f"\nYou have added {task_name} to the list of tasks.")
    print("\n-------\n")

def view_all(data):
    #split each task into its parts
    for count, line in enumerate(data, 1):
        split_data = line.split(", ")
        data_output = f"---{count}----\n"
        data_output += "\n"
        data_output += f"Assigned to: \t{split_data[0]}\n"
        data_output += f"Task name: \t{split_data[1]}\n"
        data_output += f"Assigned date: \t{split_data[3]}\n"
        data_output += f"Due date: \t{split_data[4]}\n"
        data_output += f"Is completed: \t{split_data[5]}"
        data_output += f"Description: \n\t{split_data[2]}\n"
        print(data_output)

def view_mine(data):
    #make a list for the data
    task_user_list = []

    #if the task is assigned to the user, add it to the list
    for line in data:
        split_data = line.split(", ")
        if split_data[0] == user_name:
            task_user_list.append(line)
    return task_user_list

def task_report_generator(task_report):
    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(task_report)

def user_report_generator(user_overview_report):
    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(user_overview_report)

#====Login Section====

#styling
print("\n-------\n")
print("Welcome to the task manager app.\n")

#prompt the user iput their username
user_name = input("Enter your username: ")

#prompt the user to input their password
user_pass = input("Enter your password: ")

with open("user.txt", "r") as user_passwords:
    user_name_passwords = user_passwords.readlines()


user_name_all = []
password_all = []
user_dict = {}

for value in user_name_passwords:
    value = value.replace(",", "")
    user_name_passwords_split = value.split()
    user_name_all.append(user_name_passwords_split[0])
    password_all.append(user_name_passwords_split[1])

user_dict = dict(zip(user_name_all, password_all))

if user_dict.get(user_name) == None:
    correct_name = False
elif user_dict.get(user_name) == user_pass:
    correct_name = True
    correct_password = True
else:
    correct_name = True
    correct_password = False

while correct_name == False:
    print("Incorrect username")
    user_name = input("Please input the correct username: ")
    user_pass = input("Enter your password: ")
    if user_dict.get(user_name) == None:
        correct_name = False
    elif user_dict.get(user_name) == user_pass:
        correct_name = True
        correct_password = True
    else:
        correct_name = True
        correct_password = False

while correct_password == False:
    print("Incorrect password")
    user_pass = input("Enter the correct password: ")
    if user_dict.get(user_name) == user_pass:
        correct_name = True
        correct_password = True
    else:
        correct_name = True
        correct_password = False

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    print('''Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task''')
    if user_name == "admin":
        print("ds - Statistics")
        print("gr - Generate reports")
    print("e - Exit")
    menu = input(": ").lower()
    
    #register a new user
    if menu == 'r':
        print("\n-------\n")
        if user_name == "admin": 
            #print that the user has chosen r
            print("Register a new user.\n")

            #ask the user to enter a username for the new user
            new_user = input("Please input the username of the new user: ")
            
            #check if the user already exists
            if user_dict.get(new_user) == None:
                new_user_check = True
            else:
                new_user_check = False

            #return an error if the user is already registered
            while new_user_check == False:
                print(f"{new_user} is already registered. Please try again.\n")
                new_user = input("Please input the username of the new user: ")
                if user_dict.get(new_user) == None:
                    new_user_check = True
                else:
                    new_user_check = False
            #ask the user to input the password for the new user
            new_password = input("Please input the password for the new user: ")
        
            #ask the user to confirm their password
            new_password_check = input("Please confirm your new password: ")

            #check if the passwords are the same
            if new_password == new_password_check:
                correct_new_password = True
            else:
                correct_new_password = False

            #return an error message if the passwords do not match
            while correct_new_password == False:
                print("Your passwords do not match. Please try again.\n")
                
                #ask the user to input the password again
                new_password = input("Please input the password for the new user: ")
                new_password_check = input("Please confirm your new password: ")
                if new_password == new_password_check:
                    correct_new_password = True

            #call reg_user function
            reg_user(new_user, new_password)   

        else:
            print("Sorry, only admin can add a user.")
        #styling
        print("\n-------\n")

    #add a new task   
    elif menu == 'a':
         #print that the user has chosen a
        print("\n-------\n")
        print("Adding a new task.\n")

        #prompt the user to assign the task to a user
        task_assign_user = input("Enter the name of the user this task is being assigned to: ")

        #check if this user exists
        if user_dict.get(task_assign_user) == None:
            user_exist = False
        else:
            user_exist = True
        
        #return an error if user does not exist
        while user_exist == False:
            print("\nThis user does not exist, please try again.\n")
            #prompt the user to assign the task to a user
            task_assign_user = input("Enter the name of the user this task is being assigned to: ")

            #check if this user exists
            if user_dict.get(task_assign_user) == None:
                user_exist = False
            else:
                user_exist = True

        #prompt the user to assign a name for the task
        task_name = input("Enter the title of the task: ")

        #prompt the user to enter a description of the task
        task_description = input("Enter a short description of the task: ")

        #prompt the user to enter the due date of the task
        task_due_date = input("Enter the date that this task must be completed by in this format (dd month yyyy): ")

        #get the current date
        current_date = datetime.date.today()
        current_date = current_date.strftime("%d %b %Y")

        #call the add_task function
        add_task(task_assign_user, task_name, task_description, current_date, task_due_date)
    
    elif menu == 'va':
        #print that the user has chosen va
        print("\n-------\n")
        print("View all tasks\n")

        #save the file as a list
        with open("tasks.txt", "r") as tasks_read:
            data = tasks_read.readlines()

        #call the view_all function
        view_all(data)
        
        #styling
        print("-------\n")

 #view my tasks
    elif menu == 'vm':
        print("\n-------\n")    
        print("Here are the tasks assigned to you:\n")

        #read the tasks.txt file and save to a list
        with open("tasks.txt", "r") as tasks_read:
            data = tasks_read.readlines()

        #call view_mine function
        task_user_list = view_mine(data)
        
        #is the task it assigned to the user, print it and count how many are assigned to the user
        for count, line in enumerate(task_user_list, 1):
            split_data = line.split(", ")
            data_output = f"---{count}----\n"
            data_output += "\n"
            data_output += f"Assigned to: \t{split_data[0]}\n"
            data_output += f"Task name: \t{split_data[1]}\n"
            data_output += f"Assigned date: \t{split_data[3]}\n"
            data_output += f"Due date: \t{split_data[4]}\n"
            data_output += f"Is completed: \t{split_data[5]}"
            data_output += f"Description: \n\t{split_data[2]}\n"
            print(data_output)

        #styling
        print("-------\n")
        
        #ask the user to choose a task
        task_choice = int(input("Select the number of the task you wish to edit. \nIf you wish to go back to the main menu, type '-1'\nEnter your choice here: ")) - 1
        
        #if the user enters -1, return to the menu
        if task_choice != -2:
        #return an error if the user has entered the wrong number
            if task_choice >= 0 or task_choice < (len(data) - 1 ):
                corret_task_choice = True
            else:
                corret_task_choice = False
            while corret_task_choice == False:
                print("You have selected an invalid option, please try again.")
                task_choice = input("Select a task number: ") - 1
                if task_choice >= 0 or task_choice < (len(data) - 1):
                    corret_task_choice = True

            #ask the user to choose if they want to edit a due date of mark as completed
        
            task_edit = task_user_list[task_choice]

            print("""
            --- Select an option ---
            1 - Mark as completed
            2 - Edit the task
            ----------------------

            """)
            choice = int(input("Enter here: "))
        
            #return an error if user doesn't put 1 or 2 
            if choice < 1 or choice > 2:
                print("You have selected an invalid option, please try again.")
                continue

            elif choice == 1:
                #split the data
                split_task_edit = task_edit.split(", ")
                #check if the task is already completed
                if split_task_edit[-1] == "No\n":

                
                    #mark the task as complete
                    split_task_edit[-1] = "Yes\n"

                    #rejoin the data back together
                    new_data = ", ".join(split_task_edit)

                    #find the index of the task_choice from the task list
                    index_replace = data.index(task_edit)

                    #replace the old task with the updated one
                    data[index_replace] = new_data

                    #replace the old task with the updated one
                    data[task_choice] = new_data

                    #let the user know that the task has been marked completed
                    print("The task has been marked as completed.")

                else:
                    print("\nThis task is already completed.\n")
                
            else:
                #split that task into its parts
                split_task_edit = task_edit.split(", ")
                if split_task_edit[-1] == "No\n":
                    #ask the user to enter the new due date
                    new_due_date = input("Enter the updated due date (dd mon yyyy, eg: 27 Sep 2011): ")

                    #edit only the due date
                    split_task_edit[-2] = new_due_date
                    
                    #join the data back together
                    new_data = ", ".join(split_task_edit)
                    
                    #find the index of the task_choice from the task list
                    index_replace = data.index(task_edit)

                    #replace the old task with the updated one
                    data[index_replace] = new_data

                    #let the user know this is done
                    print("\nThe date has been updated.")
                else: 
                    print("\nYou cannot edit a task that has already been completed.\n")    

            #write the data onto the file
            with open("tasks.txt", "w") as data_write:
                for line in data:
                    data_write.write(line)
        #styling
        print("\n")

    #generate reports or view statistics
    elif menu == "gr" or menu == "ds":
        if user_name == "admin":
            #read the tasks file and save as a list
            with open("tasks.txt", "r") as tasks_read:
                data = tasks_read.readlines()
            
            #count the number of tasks generated
            total_tasks = len(data)

            #make variables to count the complete/incomplete tasks
            count_complete = 0
            count_incomplete = 0
            count_incomplete_overdue = 0

            #today's date as a variable
            current_date = datetime.date.today()
            current_date = current_date.strftime("%d %b %Y")
            
            #cast the date as a date
            current_date = datetime.datetime.strptime(current_date, "%d %b %Y")

            #count the number of tasks that are complete/incomplete/overdue
            for value in data:
                split_data = value.split(", ")
                if split_data[-1] == "Yes\n":
                    count_complete += 1
                elif split_data[-1] == "No\n":
                    count_incomplete += 1

                #cast the due date as a datetime
                due_date_time = datetime.datetime.strptime(split_data[-2], "%d %b %Y")
                if due_date_time < current_date:
                    count_incomplete_overdue += 1
            
            #calculate the percent of tasks incomplete
            percent_incomplete = round((count_incomplete / total_tasks)*100, 2)

            #calculate teh percent of tasks that are overdue
            percent_overdue = round((count_incomplete / total_tasks)*100, 2)

            #generate report
            task_report = (f"""
            Total number of tasks:                  {total_tasks}
            Total number of completed tasks:        {count_complete}
            Total number of incompleted tasks:      {count_incomplete}
            Total number of overdue tasks:          {count_incomplete_overdue}
            
            Percent of tasks that are incomplete:   {percent_incomplete}%
            Percent of tasks that are overdue:      {percent_overdue}%
            """)
            
            #call task_report_generator function
            task_report_generator(task_report)

            #calculate total number of users
            total_users = len(user_name_all)

            #begin generating the report
            user_overview_report = f"""
            Total number of users:          {total_users}
            """

            #calulate for each user
            for user in user_name_all:

                #define the counter as 0
                total_user_tasks = 0
                user_tasks_completed = 0
                user_tasks_incomplete = 0
                user_tasks_overdue = 0

                #if the task it assigned to the user count how many are assigned to the user
                for line in data:
                    split_data = line.split(", ")
                    if split_data[0] == user:
                        total_user_tasks += 1

                        #count how many are completed
                        if split_data[-1] == "Yes\n":
                            user_tasks_completed += 1
                        
                        #count how many are incomplete
                        else: 
                            user_tasks_incomplete += 1
                        
                        #cast the due date as a date
                        due_date_time = datetime.datetime.strptime(split_data[-2], "%d %b %Y")
                        
                        #count how many are overdue
                        if due_date_time < current_date:
                            user_tasks_overdue += 1
                
                #prevent a 'divide by zero' error
                if total_user_tasks > 0:
                    #calculate the percent of total tasks assigned to the user
                    percent_user_total = round((total_user_tasks / total_tasks) * 100, 2)
                            
                    #calculate the percent of tasks the user has completed
                    percent_user_complete = round((user_tasks_completed / total_user_tasks) * 100, 2)

                    #calculate percent tasks incomplete
                    percent_user_incomplete = round((user_tasks_incomplete / total_user_tasks) * 100, 2)

                    #calculate percent tasks overdue
                    percent_user_overdue = round((user_tasks_overdue / total_user_tasks) * 100, 2)

                #if total tasks is 0 or a negative number:
                else:
                    #none of the tasks are for the user
                    percent_user_total = 0

                    #all their tasks are complete
                    percent_user_complete = 100

                    #none are incomplete
                    percent_user_incomplete = 0

                    #no tasks are overdue
                    percent_user_overdue = 0

                #add data to the report
                user_overview_report += f"""

                ------- {user} -------
                        
                Number of tasks assigned:                       {total_user_tasks}

                Percent of total tasks assigned:                {percent_user_total}%
                Percent tasks completed:                        {percent_user_complete}%
                Percent tasks incomplete:                       {percent_user_incomplete}%
                Percent tasks overdue:                          {percent_user_overdue}%

                """
            #call user_overview_generator function
            user_report_generator(user_overview_report)

            if menu == "gr":
                #notify user that the task has been completed
                print("\n---------\n\nReports Generated")
            elif menu == "ds":
                #read the task report
                with open("task_overview.txt", "r") as task_overview_file:
                    task_overview_read = task_overview_file.read()
                with open("user_overview.txt", "r") as user_overview_file:
                    user_overview_read = user_overview_file.read()
                print(f"\nTask overview report:\n{task_overview_read}\n\nUser overview report:\n{user_overview_read}")
        else:
            #return an error if a non-admin types in s
            print("\n-------\n") 
            print("You do not have access to this.")
            
        #styling
        print("\n-------\n") 

    elif menu == 'e':
        print("\n-------\n")
        print('Goodbye!!!')
        print("\n-------\n")
        exit()

    else:
        print("\n-------\n")
        print("You have made a wrong choice, Please Try again")
        print("\n-------\n")