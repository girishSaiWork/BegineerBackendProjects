from datetime import date,datetime
import pandas as pd




def id_getter(id_list):
    """
    Generate and return the next available ID from the given ID list.

    This function takes the first ID from the provided list of IDs,
    removes it from the list, and returns it. This ensures that each
    new expense gets a unique sequential ID.

    Args:
        id_list (list): A list of available IDs.

    Returns:
        int: The next available ID.

    Note:
        This function modifies the input list by removing the returned ID.
    """
    current_id = id_list.pop(0)
    return current_id

# Function to validate date input
def get_valid_date(prompt):
    """
    Prompt the user for a valid date input and return it as a string.

    This function repeatedly prompts the user to enter a date until a valid date
    in the format YYYY-MM-DD is provided. It uses the datetime.strptime() method
    to validate the input and convert it to a date object.

    Args:
        prompt (str): The message to display when prompting the user for input.

    Returns:
        str: A string representation of the valid date in the format YYYY-MM-DD.

    Raises:
        ValueError: If the input cannot be parsed as a valid date.

    Note:
        This function will continue to prompt the user until a valid date is entered.
        It handles the ValueError exception raised by datetime.strptime() when an
        invalid date format is provided.
    """
    while True:
        user_input = input(prompt)
        try:
            valid_date = datetime.strptime(user_input, '%Y-%m-%d')
            return str(valid_date.date())
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


trackerList = []

def addExpense(id_list):
    """
    Add a new expense to the expense tracker.

    This function prompts the user for expense details, generates a unique ID,
    and adds the expense to the tracker list. It then converts the list to a
    pandas DataFrame and returns it.

    Args:
        id_list (list): A list of available sequential IDs.

    Returns:
        pandas.DataFrame: A DataFrame containing all expenses, including the newly added one.

    Note:
        This function modifies the global trackerList by appending the new expense.
        It uses the id_getter function to obtain a unique sequential ID.
        The expense date can be set to the current date or a user-specified date.
    """
    # get current date
    current_Date_str = str(date.today())
    seq_id = id_getter(id_list)
    expense_id = current_Date_str + '_' + str(seq_id)
    expense_description = input("Enter the description of expense : ")
    amount_spent = float(input("Enter the amount spent : "))
    date_flag = input('Is the expense today say Y or N : ')
    if date_flag == 'Y':
        date_spent = current_Date_str
    else:
        # Ask user to enter the date in YYYY-MM-DD format
        date_spent = get_valid_date('Enter the date in YYYY-MM-DD format: ')

    expenseList = [expense_id,expense_description,amount_spent,date_spent]
    trackerList.append(expenseList)
    df_cols = ['ID','Description','Amount','Date Spent']
    trackerDF = pd.DataFrame(trackerList, columns=df_cols)
    return trackerDF

def viewExpnses(trackerDF):
    """
    Display all expenses in the expense tracker.

    This function prints out all expenses currently stored in the trackerDF DataFrame.
    It displays the entire DataFrame, including all columns (ID, Description, Amount, Date Spent).
    If there are no expenses in the DataFrame, it will display an empty DataFrame.

    Args:
        trackerDF (pandas.DataFrame): The DataFrame containing all the expense records.

    Returns:
        None

    Note:
        This function does not modify the trackerDF; it only reads and displays the information.
        The actual printing of the DataFrame is done by the print statement following this docstring.
    """
    print(trackerDF)

def updateExpnses(df,expense_id,description=None,amount_spent=None,date_spent=None):
    """
    Update an existing expense in the expense tracker.

    This function allows for updating the description, amount spent, and/or date spent of an expense
    identified by its expense_id. If a parameter is not provided, that field remains unchanged.

    Args:
        df (pandas.DataFrame): The DataFrame containing all the expense records.
        expense_id (str): The ID of the expense to be updated.
        description (str, optional): The new description for the expense. Defaults to None.
        amount_spent (float, optional): The new amount spent for the expense. Defaults to None.
        date_spent (str, optional): The new date spent for the expense in 'YYYY-MM-DD' format. Defaults to None.

    Returns:
        pandas.DataFrame: The updated DataFrame containing all expenses.

    Note:
        If the expense_id is not found in the DataFrame, a message is printed indicating that
        the expense was not found. The function will still return the unchanged DataFrame in this case.
    """
    # Find the row with the matching expense_id
    mask = df['ID'] == expense_id

    # Update the fields if new values are provided
    if description:
        df.loc[mask, 'Description'] = description
    if amount_spent:
        df.loc[mask, 'Amount'] = float(amount_spent)
    if date_spent:
        df.loc[mask, 'Date Spent'] = date_spent

    print(f"Expense with ID {expense_id} updated successfully.")
    
    return df

def delExpnses(df,expense_id):
    """
    Delete an expense from the expense tracker based on its ID.

    This function removes an expense from the DataFrame if an expense with the given expense_id exists.
    If no expense with the given ID is found, an appropriate message is displayed.

    Args:
        df (pandas.DataFrame): The DataFrame containing all the expense records.
        expense_id (str): The ID of the expense to be deleted.

    Returns:
        pandas.DataFrame: The updated DataFrame with the specified expense removed (if found).

    Note:
        If the expense_id is not found in the DataFrame, the function will print a message
        and return the unchanged DataFrame.
    """
    mask = df['ID'] == expense_id
    if not mask.any():
        print(f"Expense with ID {expense_id} not found.")
    else:
        # Delete rows where the city is Chicago
        df = df.drop(df[df['ID'] == expense_id].index)
    return df
    
def main():
    """
    Main function to run the Expense Tracker CLI application.

    This function implements the main loop of the Expense Tracker, presenting a menu of options to the user
    and executing the corresponding functions based on user input. The available options are:

    1. Add Expense
    2. View All Expenses
    3. Update Expense
    4. Delete Expense
    5. Summary Expense
    6. Exit

    For each option, the function prompts for necessary inputs and calls the
    corresponding function to perform the requested operation.

    The function handles invalid inputs by displaying an error message and
    continuing the loop.

    The function uses a pandas DataFrame to store and manipulate expense data.

    Returns:
        None
    """
    print("####################################################################################################")
    print("#                               EXPENSE TRACKER IN PYTHON                                          #")
    print("####################################################################################################")

    id_list = list(range(1,1001)) 
    while True:
        print("\nExpense Tracker CLI")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Summary Expense")
        print("6. Exit")
    
        choice = input("Enter your choice: ")
        if choice == '1':
            trackerDF = addExpense(id_list)
        elif choice == '2':
            viewExpnses(trackerDF)
        elif choice == '3':
            if not trackerList:
                print("No expenses to update. Please add expenses first.")
            else:
                expense_id = input("Enter expense ID to update: ")
                # Find the row with the matching expense_id
                mask = trackerDF['ID'] == expense_id
                if not mask.any():
                    print(f"Expense with ID {expense_id} not found.")
                else:
                    description = input("Enter new description (leave blank to keep current): ")
                    amount_spent = input("Enter new amount (leave blank to keep current): ")
                    date_spent = input("Enter new date (leave blank to keep current): ")
                    updateExpnses(trackerDF,expense_id,description,amount_spent,date_spent)
                    print(trackerDF)
        elif choice == '4':
            expense_id = input("Enter expense ID to delete: ")
            trackerDF = delExpnses(trackerDF,expense_id)
            print(trackerDF)
        elif choice == '5':
            total_expenses = sum(trackerDF['Amount'].values)
            print("Total expenses summary : ", total_expenses)
        elif choice == '6':
                print("Exiting Task Tracker. Goodbye!")
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()