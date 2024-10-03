# Enhanced Bank Account Management System with Loan Feature

# Initialize lists to hold account data

account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    # 1. Prompt the user for the account holder's name.
    name_account = input("Please use the name of the account holder: ")
    if name_account not in account_holders:
        # 2. Add the new account holder to the list of account holders.
        account_holders.append(name_account)
        # 3. Initialize the balance to 0 for the new account.
        balances.append(0)
        # 4. Initialize an empty transaction history for the new account.
        transaction_histories.append([])
        # 5. Initialize the outstanding loan amount to 0.
        loans.append(0)
        # 6. Notify the user of the successful account creation.
        print("Congratulations! You have successfully created your account.")
    else:
        print("Account already exists!")


def deposit():
    """Deposit money into an account."""
    # 1. Prompt the user for the account holder's name.
    name_account_deposit = input("Specify the account to which you want to deposit:  ")
    # 2. Check if the account exists in the system.
    # 3. If the account exists, prompt the user for the amount to deposit.
    if name_account_deposit in account_holders:
        index = account_holders.index(name_account_deposit)
        amount_deposited = float(input("Please enter deposit amount: "))
        # 4. Update the account's balance with the deposited amount.
        balances[index] += amount_deposited
        # 5. Log the transaction in the account's transaction history.
        transaction_histories[index].append([f"You deposited: {amount_deposited} leva."])
        # 6. Display the updated balance to the user.
        print(f"Your balance is: {balances[index]:.2f} leva.")
    # 7. If the account does not exist, inform the user.
    else:
        print("Sorry! Accounts do not exist.")


def withdraw():
    """Withdraw money from an account."""
    # 1. Prompt the user for the account holder's name.
    name_account_withdraw = input("Specify the account you want to withdraw from: ")
    # 2. Check if the account exists in the system.
    # 3. If the account exists, prompt the user for the amount to withdraw.
    if name_account_withdraw in account_holders:
        index = account_holders.index(name_account_withdraw)
        withdrawal_amount = float(input("Please specify the amount you wish to withdraw: "))
        # 4. Check if there are sufficient funds for the withdrawal.
        if withdrawal_amount <= balances[index]:
            # 5. If funds are sufficient, update the balance and log the transaction.
            balances[index] -= withdrawal_amount
            transaction_histories[index].append(f"You withdrawn: {withdrawal_amount} leva.")
            # 6. Display the updated balance to the user.
            print(f"Your balance is: {balances[index]:.2f} leva.")
        # 7. If insufficient funds, inform the user.
        else:
            print("Sorry! There are insufficient balances on the account!")
    # 8. If the account does not exist, inform the user.
    else:
        print("Sorry! Accounts do not exist.")


def check_balance():
    """Check the balance of an account."""
    # 1. Prompt the user for the account holder's name.
    name_account_check_balance = input("Enter the account whose current balance you want to check: ")
    # 2. Check if the account exists in the system.
    if name_account_check_balance in account_holders:
        index = account_holders.index(name_account_check_balance)
        # 3. If the account exists, display the current balance.
        print(f"Your balance is: {balances[index]:.2f} leva.")
    # 4. If the account does not exist, inform the user.
    else:
        print("Sorry! Accounts do not exist.")


def list_accounts():
    """List all accounts and their balances."""
    # 1. Check if there are any accounts in the system.
    if len(account_holders) > 0:
        # 2. If there are accounts, loop through each account holder.
        # 3. Display the account holder's name, balance, and outstanding loan amount.
        for account in account_holders:
            index = account_holders.index(account)
            print(f"Account name: {account}.")
            print(f"Your balance: {balances[index]} leva.")
            print(f"Outstanding loan amount: {loans[index]} leva.")
    # 4. If there are no accounts, inform the user.
    else:
        print("Sorry! Accounts do not exist.")


def transfer_funds():
    """Transfer funds between two accounts."""
    # 1. Prompt the user for the sender's and recipient's account holder names.
    name_account_sender = input("Please enter the name of the sender holder: ")
    if name_account_sender in account_holders:
        name_account_recipient = input("Please enter the name of the recipient holder: ")
        if name_account_recipient in account_holders:
            # 2. Check if both accounts exist in the system.
            index_sender = account_holders.index(name_account_sender)
            index_recipient = account_holders.index(name_account_recipient)
            # 3. If both accounts exist, prompt the user for the amount to transfer.
            amount_transfer = float(input("Enter amount to transfer: "))
            # 4. Check if the sender has sufficient funds for the transfer.
            if amount_transfer <= balances[index_sender]:
                # 5. If funds are sufficient, update both balances and log the transactions.
                balances[index_sender] -= amount_transfer
                balances[index_recipient] += amount_transfer
                transaction_histories[index_sender].append(f"{name_account_sender} send {amount_transfer:.2f} leva to {name_account_recipient}.")
                transaction_histories[index_recipient].append(f"{name_account_recipient} received {amount_transfer:.2f} leva from {name_account_sender}.")
                # 6. Inform the user of the successful transfer.
                print("You have successfully transferred.")
                # 7. If insufficient funds or if either account does not exist, inform the user.
            else:
                print("Sorry! Not enough funds.")
        else:
            print("Sorry! Recipient does not exist.")
    else:
        print("Sorry! Sender does not exist.")


def view_transaction_history():
    """View transaction history for a specific account."""
    # 1. Prompt the user for the account holder's name.
    name_account_transaction_history = input("Please use the name of the account holder: ")
    # 2. Check if the account exists in the system.
    if name_account_transaction_history in account_holders:
        index = account_holders.index(name_account_transaction_history)
        # 3. If the account exists, display the transaction history.
        if len(account_holders) > 0:
            print(f"{transaction_histories[index]:.2f}")
        # 4. If there are no transactions, inform the user.
        else:
            print("Sorry! There are no transactions")
    # 5. If the account does not exist, inform the user.
    else:
        print("Sorry! Accounts do not exist.")


def apply_for_loan():
    """Apply for a loan."""
    name = input("Enter the account holder's name: ")
    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index
        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))
        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest
            transaction_histories[index].append(f"You received a loan of: {loan_amount:.2f} leva.")
            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    name = input("Enter the account holder's name: ")
    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index
        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))
        # Check if the repayment amount is valid
        if repayment_amount <= loans[index]:
            # Update balance and outstanding loan amount
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount
            transaction_histories[index].append(f"You returned a loan of: {repayment_amount:.2f} leva.")
            print(f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")


print(main())
