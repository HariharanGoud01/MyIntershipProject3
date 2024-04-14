print("PYTHON PROGRAMMING PROJECT - 3\n\n\n")

# Project title and description
print("PROJECT TITLE: EXPENSE TRACKER\n")
print("This program helps you track, store, and view your expenses.\n")

# Defining empty list for expenses and sample entries
expenses = []
expense1 = {'amount': '1400', 'category': 'Dress'}
expenses.append(expense1)
expense2 = {'amount': '2155', 'category': 'Fuel'}
expenses.append(expense2)


# Function to display the menu
def print_menu():
    print("\nPlease choose from one of the following options...")
    print("1. Add a New Expense")
    print("2. Remove an Expense")
    print("3. List All Expenses")
    print("4. Exit")


# Function to add expenses with error handling
def add_expense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)


# Function to remove expenses with error handling
def remove_expense():
    while True:
        list_expenses()
        print("What expense would you like to remove? (Enter the number)")
        try:
            expense_to_remove = int(input("> "))
            del expenses[expense_to_remove]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")


# Function to display a list of expenses
def list_expenses():
    print("\n------------------------------------")
    print("............YOUR EXPENSES.............")
    print("------------------------------------\n")
    counter = 0
    for expense in expenses:
        print(f"#{counter} - Amount: {expense['amount']}, Category: {expense['category']}")
        counter += 1
    print("\n\n")


# Main program loop
if __name__ == "__main__":
    while True:
        # Display menu
        print_menu()

        # Get user input and validate
        option_selected = input("> ")
        if not option_selected.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        # Handle menu options
        if option_selected == "1":
            print("How much was this expense?")
            while True:
                try:
                    amount_to_add = float(input("> "))  # Validate for numeric amount
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            print("What category was this expense?")
            category = input("> ")
            add_expense(amount_to_add, category)
        elif option_selected == "2":
            remove_expense()
        elif option_selected == "3":
            list_expenses()
        elif option_selected == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")