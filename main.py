# Importing the custom module containing the tools
import helpers


def display_menu():
    print("\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘")
    print(" 🛠️  WELCOME TO MY PYTHON MINI TOOLKIT  🛠️")
    print("-ˋˏ✄┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ˎˊ-")
    print("1. Grade Calculator ")
    print("2. To-Do List ")
    print("3. Daily Motivation Generator ")
    print("4. Exit Program ")
    print("⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘")


def main():
    while True:
        display_menu()
        user_choice = input("Select a tool to open (1-4): ").strip()

        # Conditional control logic based on user input
        if user_choice == "1":
            helpers.grade_calculator()
        elif user_choice == "2":
            helpers.todo_list()
        elif user_choice == "3":
            helpers.daily_motivation()
        elif user_choice == "4":
            print("\nThank you for using my Python Mini Toolkit!!\n")
            break  # Exits the loop and closes the application
        else:
            print("\nInvalid selection. Please type 1, 2, 3, or 4.")


# Standard Python boilerplate to ensure main() runs when file is executed directly
if __name__ == "__main__":
    main()