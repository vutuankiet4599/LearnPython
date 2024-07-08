index = 0

def find_expense_by_index(expenses, index):
    return list(filter(lambda expense: expense['index'] == index, expenses))[0]
    
def add_expense(expenses, amount, category):
    global index
    expenses.append({'index': index, 'amount': amount, 'category': category})
    index += 1

def print_expenses(expenses):
    for expense in expenses:
        print(f"Index: {expense['index']}, Amount: {expense['amount']}, Category: {expense['category']}")

def print_expense(expenses, index):
    expense = find_expense_by_index(expenses, index)
    print(f"Amount: {expense['amount']}, Category: {expense['category']}")

def update_expense(expenses, index, amount, category):
    expense = find_expense_by_index(expenses, index)
    expense['amount'] = amount
    expense['category'] = category

def delete_expense(expenses, index):
    expense = find_expense_by_index(expenses, index)
    expenses.remove(expense)

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return list(filter(lambda expense: expense['category'].find(category) != -1, expenses))    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show expense')
        print('4. Show total expenses')
        print('5. Update expense')
        print('6. Delete expense')
        print('7. Filter expenses by category')
        print('Other. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nExpense Detail:')
            index = int(input('Enter index: '))
            print_expense(expenses, index)
    
        elif choice == '4':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '5':
            index = int(input('Enter index: '))
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            update_expense(expenses, index, amount, category)
            print('Expense updated successfully')

        elif choice == '6':
            index = int(input('Enter index: '))
            delete_expense(expenses, index)
            print('Expense deleted successfully')

        elif choice == '7':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        else:
            print('Exiting the program.')
            break

main()
