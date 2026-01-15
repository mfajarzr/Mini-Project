# tasks = []

# while True:
#     print("--------TO-DO LIST APP--------")
#     if not tasks:
#         print("No task\n")
#     print("Please input the number of command you want to run")
#     print("1. Add Task\n2. Show Task\n3. Exit Program")

#     choice = input("Input: ")
#     if choice == "1":
#         name = input("Enter Name: ")
#         priority = input("Enter Priority: ")
#         status_input = input("Status (Done/Not done): ").lower()
#         status = True if status_input == "done" else False

#         task = {"Name": name,
#                 "Priority": priority,
#                 "Status": status
#                 }

#         tasks.append(task)
#         print(f"\nTask {name} added!\n")

#     elif choice == "2":
#         if not tasks:
#             print("No task yet\n")
#         else:
#             print("\nCurrent Tasks:\n")
#             for i, task in enumerate(tasks, start=1):
#                 status_text = "Done" if task["Status"] else "Not done"
#                 print(f"{i}. {task["Name"]}")
#                 print(f"priority: {task["Priority"]}")
#                 print(f"status: [{status_text}]")
#                 print(" ")

#     elif choice == "3":
#         print("Goodbye")
#         break
#     else:
#         print("Invalid Input")


tasks = []

while True:
    print("----------TO-DO LIST APP----------")
    if not tasks:
        print("No task\n")
    print("Please input the number of command you want to run")
    print("1. Add Task\n2. Show Task\n3. Exit Program\n")

    choice = int(input("Input: "))

    if choice == 1:
        task_name = input("Task name: ")

        while True:
            priority = int(input("Priority (1.High, 2.Low): "))
            if priority == 1:
                priority = "High"
                break
            elif priority == 2:
                priority = "Low"
                break
            else:
                priority = "Invalid option, please enter 1 or 2"

        while True:
            status_input = int(
                input("Status (1.Not Done, 2.On-Going, 3.Done): "))
            if status_input == 1:
                status_input = "Not Done"
                break
            if status_input == 2:
                status_input = "On-Going"
                break
            if status_input == 3:
                status_input = "Done"
                break
            else:
                status_input = "Invalid option, please enter 1, 2 or 3"

        task = {"Task Name": task_name,
                "Priority": priority,
                "Status": status_input}

        tasks.append(task)
        print(f"\n{task_name} added to your list\n")

    elif choice == 2:
        if not tasks:
            print("\nNo task\n")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"\n{number}. {task["Task Name"]}")
                print(f"Priority : {task["Priority"]}")
                print(f"Status : {task["Status"]}")
                print(" ")

    elif choice == 3:
        print("Have a nice day 👋")
        break

    else:
        print("Invalid Input, please use one of the options available")
