tasks = []

name = input("Enter Name: ")
priority = input("Enter Priority: ")
status_input = input("Status (Done/Not done): ").lower()
status = True if status_input == "done" else False

task = {"Name": name,
        "Priority": priority,
        "Status": status
        }

tasks.append(task)

for i, task in enumerate(tasks, start=1):
    status_text = "Done" if task["Status"] else "Not done"
    print(f"{i}. {task["Name"]}")
    print(f"priority: {task["Priority"]}")
    print(f"status: [{status_text}]")
