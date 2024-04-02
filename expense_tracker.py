from expense import Expense
import calendar
import datetime


def main():
    print(f"Running Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user to input expense.
    expense = get_user_expense()

    # Write expense to a file.
    save_expense_to_file(expense, expense_file_path)

    #Read the file and summerize expenses.
    summarize_expense(expense_file_path, budget)
    pass

def get_user_expense():
    print(f"Getting user input")
    expense_name = input("Enter Expense name: ")
    expense_amount = float(input("Enter Expense amount: "))
    expense_categories = [
        "FOOD",
        "WORK",
        "HOME",
        "FUN",
        "MISC"
        ]
    
    while True:
        print("Select Category: ")
        for i , category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_input = int(input(f"Enter The Category Number {value_range}: "))-1

        if selected_input in range(len(expense_categories)):
            selected_category = expense_categories[selected_input]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category. Please Try Again!")

    


def save_expense_to_file(expense, expense_file_path):
    print(f"Saving expense to file :{expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")
    

def summarize_expense(expense_file_path, budget    ):
    print(f"Summarizing user expense")
    expenses = []
    with open(expense_file_path, "r") as f:

        lines  = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by category: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")


    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"Budget Remaining: ${remaining_budget:.2f} ")



    # Get the current date
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print("remaining days in the month",remaining_days )

    daily_budget = (remaining_budget/remaining_days)
    print(f"Budget per day: ${daily_budget:.2f}")

if __name__=="__main__":
    main()