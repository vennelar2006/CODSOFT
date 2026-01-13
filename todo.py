print("To-do list")
tasks = []
while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to remove: "))
            tasks.pop(num - 1)
            print("Task removed")

    elif choice == "4":
        print("Thank-you!")
        break

    else:
        print("Invalid choice")
