import random  # Built-in module for the motivation generator


def grade_calculator():
    print("\nVII Grade Calculator XIII:")
    try:
        score = float(input("Enter your score (0 to 100): "))

        # Validating user input using comparison and logical operators
        if score < 0 or score > 100:
            print("Invalid score! Please enter a value between 0 and 100.")
            return

        if score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"

        # Cleans up float trailing zeros (e.g., 95.0 becomes 95)
        print(f"Your score of {score:g} gives you a grade of: {grade}")

        if grade != "F":
            print("Great job! You have passed.")
        else:
            print(
                "Sorry you have not met passing requirements, don't give up! Keep studying and you'll get it next time."
            )

    except ValueError:
        print("Error: Please enter a valid number.")


def todo_list():
    print("\n--- To-Do List ---")
    tasks = []  # Initializes an empty list to store tasks
    
    while True:
        print("\n⋆*·⋅˚₊‧˖꙳ To-Do Menu ⋆*·⋅˚₊‧˖꙳:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit To-Do List")
        
        choice = input("Choose an option (1-4): ").strip()
        #The strip() method removes any leading, and trailing whitespaces. Leading means at the beginning of the string, trailing means at the end. You can specify which character(s) to remove, if not, any whitespaces will be removed.
        
        if choice == '1':
            if not tasks:
                print("Your to-do list is currently empty!")
            else:
                print("\nYour Current Tasks:")
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")
                    
        elif choice == '2':
            new_task = input("Enter the task you want to add: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"'{new_task}' has been added.")
            else:
                print("Task cannot be empty!")
                
        elif choice == '3':
            if not tasks:
                print("Nothing to remove!")
            else:
                raw_input = input("Enter the task number to remove: ").strip()
                if not raw_input:
                    print("Please enter a number.")
                    continue
                try:
                    task_num = int(raw_input)
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        #The pop() method removes the element at the specified position.
                        print(f"Removed: {removed}")
                    else:
                        print(f"Invalid task number. Please choose between 1 and {len(tasks)}.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == '4':
            print("Exiting To-Do List...")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 4.")


def daily_motivation():
    print("\n ˖⟡˚ ࣪Daily Motivation Generator ˚⟡˖ ࣪")

    quotes = [
        "Believe you can and you're halfway there.",
        "The expert in anything was once a beginner.",
        "Progress, not perfection. Every step counts!",
        "Mistakes are proof that you are trying.",
        "Your future self will thank you for the effort you put in today.",
        "Put in the work NOW for a better tomorrow! ",
        "Life is not always easy, but you can work hard to make it easier",
        "Nobody sets the rules but you. You can design your own life.”— Carrie Ann Moss",
        "Your talent determines what you can do. Your motivation determines how much you’re willing to do. Your attitude determines how well you do it. —Lou Holtz",
        "Change brings opportunity. —Nido Qubein",
        "The only way to do great work is to love what you do. —Steve Jobs",
    ]

    # Selects a random quote using the built-in random module
    random_quote = random.choice(quotes)
    print(f'\n𑣲Theme Quote For Your Day: "{random_quote}"')