# banking app
# bank account handling (add, remove, update, list, search)
# deposit and withdrawal
# balance check
#
# - file handling
def create_account(accounts):
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    if account_number in accounts:
        print("Account already exists.")
    else:
        accounts[account_number] = {"holder": account_holder, "balance": 0}
        print("Account created successfully.")

def remove_account(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        del accounts[account_number]
        print("Account removed successfully.")
    else:
        print("Account not found.")

def update_account_holder(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        new_holder = input("Enter new account holder name: ")
        accounts[account_number]["holder"] = new_holder
        print("Account holder name updated successfully.")
    else:
        print("Account not found.")

def list_accounts(accounts):
    if accounts:
        print("\nList of Accounts:")
        for account_number, details in accounts.items():
            print(f"Account Number: {account_number}, Account Holder: {details['holder']}, Balance: {details['balance']}")
    else:
        print("No accounts found.")

def search_account(accounts):
    account_holder = input("Enter account holder name: ")
    found_accounts = [acc_num for acc_num, details in accounts.items() if details["holder"] == account_holder]
    if found_accounts:
        print("\nFound Accounts:")
        for acc_num in found_accounts:
            print(f"Account Number: {acc_num}, Balance: {accounts[acc_num]['balance']}")
    else:
        print("No accounts found for the given account holder name.")

def check_balance(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print(f"Account balance: {accounts[account_number]['balance']}")
    else:
        print("Account not found.")

def deposit_money(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            accounts[account_number]["balance"] += amount
            print(f"Deposited {amount}. New balance is {accounts[account_number]['balance']}.")
        else:
            print("Deposit amount must be positive.")
    else:
        print("Account not found.")

def withdraw_money(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= amount
            print(f"Withdrew {amount}. New balance is {accounts[account_number]['balance']}.")
        else:
            print("Invalid withdrawal amount.")
    else:
        print("Account not found.")

def main():
    accounts = {}

    while True:
        print("\nBanking App")
        print("1. Create Account")
        print("2. Remove Account")
        print("3. Update Account Holder")
        print("4. List Accounts")
        print("5. Search Account by Holder Name")
        print("6. Check Balance")
        print("7. Deposit Money")
        print("8. Withdraw Money")
        print("9. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                create_account(accounts)
            case '2':
                remove_account(accounts)
            case '3':
                update_account_holder(accounts)
            case '4':
                list_accounts(accounts)
            case '5':
                search_account(accounts)
            case '6':
                check_balance(accounts)
            case '7':
                deposit_money(accounts)
            case '8':
                withdraw_money(accounts)
            case '9':
                print("Exiting the app.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
