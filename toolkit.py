
import random

# Store tasks in a list
tasks = []


# Calculator function
def calculator():
    print("\n--- CALCULATOR ---")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Choose operation: ")

        if operation == "1":
            print("Result:", num1 + num2)

        elif operation == "2":
            print("Result:", num1 - num2)

        elif operation == "3":
            print("Result:", num1 * num2)

        elif operation == "4":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero!")

        else:
            print("Invalid operation.")

    except ValueError:
        print("Please enter valid numbers.")


# To-do list function
def todo_list():
    print("\n--- TO-DO LIST ---")

    print("1. Add task")
    print("2. View tasks")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your task list is empty.")
        else:
            print("\nYour Tasks:")
            for task in tasks:
                print("-", task)

    else:
        print("Invalid choice.")


# Number guessing game
def guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")

    secret_number = random.randint(1, 10)

    try:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == secret_number:
            print("Congratulations! You guessed correctly!")

        else:
            print("Sorry! The correct number was", secret_number)

    except ValueError:
        print("Please enter a valid number.")


# Main menu
def show_menu():
    print("\n===== PERSONAL MINI TOOLKIT =====")
    print("1. Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Exit")


# Keep the program running until the user exits
while True:

    show_menu()

    choice = input("Choose a tool (1-4): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("Thank you for using Personal Mini Toolkit!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")
