import random

# Initialize account
def create_account(username: str) -> dict:
    """
    Creates a new casino account for the given username.

    Args:
        username: str
            The username for the new account.

    Returns:
        dict
            A dictionary containing the username and initial balance of the account.
    """
    return {"username": username, "balance": 100}

# Account management functions
def deposit(account: dict, amount: int) -> None:
    """
    Deposits a specified amount into a given account.

    Args:
        account (dict): The account to deposit into.
        amount (int): The amount to deposit.

    Returns:
        None
    """
    if amount > 0:
        account["balance"] += amount
        print(f"Deposited {amount} successfully. New balance: {account['balance']}")
    else:
        print("Deposit amount must be positive.")

def withdraw(account: dict, amount: int) -> None:
    """
    Withdraws a specified amount from a given account.

    Args:
        account (dict): The account to withdraw from.
        amount (int): The amount to withdraw.

    Returns:
        None
    """
    if 0 < amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Withdrew {amount} successfully. New balance: {account['balance']}")
    else:
        print("Insufficient funds or invalid amount.")

def get_balance(account: dict) -> int:
    """
    Retrieves the current balance of a given casino account.

    Args:
        account (dict): A dictionary containing the account information.

    Returns:
        int: The current balance of the account.
    """
    return account["balance"]

# Betting function
def place_bet(account: dict, amount: int) -> bool:
    """
    Places a bet on a casino game.

    Args:
        account (dict): The account to place the bet from.
        amount (int): The amount to bet.

    Returns:
        bool: True if the bet is placed successfully, False if there are insufficient funds.
    """
    if amount > 0 and amount <= account["balance"]:
        account["balance"] -= amount
        return True
    else:
        print("Insufficient funds or invalid bet amount.")
        return False

# Game functions
def play_slots(account: dict) -> None:
    """
    Plays a game of slots with the given account.

    Args:
        account (dict): The account to play with.

    Returns:
        None
    """
    print("--- Slots Game ---")
    bet = int(input("Enter your bet amount: "))
    if place_bet(account, bet):
        slot_results = [random.choice(["Cherry", "Lemon", "Bell", "Star", "Seven"]) for _ in range(3)]
        print(f"Slot results: {' | '.join(slot_results)}")
        if len(set(slot_results)) == 1:  # All three are the same
            winnings = bet * 10
            account["balance"] += winnings
            print(f"Jackpot! You won {winnings}. New balance: {account['balance']}")
        else:
            print("You lost. Better luck next time!")

def play_roulette(account: dict) -> None:
    """
    Plays a game of Roulette.

    Args:
        account (dict): The account to play with, containing the username and balance.

    Returns:
        None
    """
    print("--- Roulette Game ---")
    bet = int(input("Enter your bet amount: "))
    if place_bet(account, bet):
        bet_type = input("Do you want to bet on a 'number', 'red', 'black', or 'green'? ").lower()

        if bet_type == "number":
            chosen_number = int(input("Enter a number between 0 and 36: "))
            if 0 <= chosen_number <= 36:
                winning_number = random.randint(0, 36)
                colors = {0: "green", **dict.fromkeys(range(1, 37, 2), "red"), **dict.fromkeys(range(2, 37, 2), "black")}
                winning_color = colors[winning_number]
                print(f"The winning number is {winning_number} ({winning_color}).")

                if chosen_number == winning_number:
                    winnings = bet * 35
                    account["balance"] += winnings
                    print(f"Congratulations! You guessed the correct number and won {winnings}. New balance: {account['balance']}")
                else:
                    print("You lost. Better luck next time!")
            else:
                print("Invalid number. Bet lost.")

        elif bet_type in ["red", "black", "green"]:
            winning_number = random.randint(0, 36)
            colors = {0: "green", **dict.fromkeys(range(1, 37, 2), "red"), **dict.fromkeys(range(2, 37, 2), "black")}
            winning_color = colors[winning_number]
            print(f"The winning number is {winning_number} ({winning_color}).")

            if bet_type == winning_color:
                winnings = bet * 2
                account["balance"] += winnings
                print(f"Congratulations! You guessed the correct color and won {winnings}. New balance: {account['balance']}")
            else:
                print("You lost. Better luck next time!")

        else:
            print("Invalid bet type. Bet lost.")

def play_blackjack(account: dict) -> None:
    """
    Plays a game of Blackjack with the given account.

    Args:
        account (dict): The account to play with, containing the username (str) and balance (int).

    Returns:
        None
    """
    print("--- Blackjack Game ---")
    bet = int(input("Enter your bet amount: "))
    if place_bet(account, bet):
        player_hand = random.randint(15, 21)
        dealer_hand = random.randint(17, 23)
        print(f"Your hand: {player_hand}")
        print(f"Dealer's hand: {dealer_hand}")

        if player_hand > 21:
            print("You busted! You lose.")
        elif dealer_hand > 21 or player_hand > dealer_hand:
            winnings = bet * 2
            account["balance"] += winnings
            print(f"You win! Your winnings: {winnings}. New balance: {account['balance']}")
        else:
            print("You lose. Better luck next time!")

# Main program loop
def main():
    """
    The main function of the casino program.

    It creates a new account based on user input,
    then enters a loop where it continuously displays a menu of options to the user.
    The user can choose to check their balance, deposit or withdraw money, or exit the program.
    The user can also choose to play different games.

    Args:
        None

    Returns:
        None
    """
    username = input("Enter your username to create an account: ")
    account = create_account(username)
    while True:
        menu = {
            '0': 'Exit',
            '1': 'Check Balance',
            '2': 'Deposit Money',
            '3': 'Withdraw Money',
            '4': 'Play Slots',
            '5': 'Play Roulette',
            '6': 'Play Blackjack',
        }

        print("\n--- Casino Menu ---")
        for key, value in menu.items():
            print(f"{key}. {value}")

        choice = input("Choose an option (0-6): ")

        match choice:
            case '0':
                print("Thank you for playing! Goodbye!")
                break
            case '1':
                print(f"Your current balance is: {get_balance(account)}")
            case '2':
                deposit_amount = int(input("Enter the amount to deposit: "))
                deposit(account, deposit_amount)
            case '3':
                withdraw_amount = int(input("Enter the amount to withdraw: "))
                withdraw(account, withdraw_amount)
            case '4':
                play_slots(account)
            case '5':
                play_roulette(account)
            case '6':
                play_blackjack(account)
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
else:
    raise ImportError("This file is not meant to be imported")