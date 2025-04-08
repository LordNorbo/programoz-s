import random


class Account:
    def __init__(self, username: str):
        self.username = username
        self.balance = 0
    
    def deposit(self, amount: int):
        self.balance += amount
    
    def withdraw(self, amount: int):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} successfully. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    def get_balance(self) -> int:
        return self.balance

class Game:
    def __init__(self, casino: 'Casino'):
        self.casino = casino
    
    def place_bet(self, amount: int) -> bool:
        if amount > 0 and amount <= self.casino.current_user.get_balance():
            self.casino.current_user.withdraw(amount)
            return True
        else:
            print("Insufficient funds or invalid bet amount.")
            return False


class SlotGame(Game):
    def play(self):
        print("--- Slots Game ---")
        bet = int(input("Enter your bet amount: "))
        if self.place_bet(bet):
            slot_results = [random.choice(["Cherry", "Lemon", "Bell", "Star", "Seven"]) for _ in range(3)]
            print(f"Slot results: {' | '.join(slot_results)}")
            if len(set(slot_results)) == 1:  # All three are the same
                winnings = bet * 10
                self.casino.current_user.deposit(winnings)
                print(f"Jackpot! You won {winnings}. New balance: {self.casino.current_user.get_balance()}")
            else:
                print("You lost. Better luck next time!")


class RouletteGame(Game):
    def play(self):
        print("--- Roulette Game ---")
        bet = int(input("Enter your bet amount: "))
        if self.place_bet(bet):
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
                        self.casino.current_user.deposit(winnings)
                        print(f"Congratulations! You guessed the correct number and won {winnings}. New balance: {self.casino.current_user.get_balance()}")
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
                    self.casino.current_user.deposit(winnings)
                    print(f"Congratulations! You guessed the correct color and won {winnings}. New balance: {self.casino.current_user.get_balance()}")
                else:
                    print("You lost. Better luck next time!")
            else:
                print("Invalid bet type. Bet lost.")


class BlackjackGame(Game):
    def play(self):
        print("--- Blackjack Game ---")
        bet = int(input("Enter your bet amount: "))
        if self.place_bet(bet):
            player_hand = random.randint(15, 21)
            dealer_hand = random.randint(17, 23)
            print(f"Your hand: {player_hand}")
            print(f"Dealer's hand: {dealer_hand}")

            if player_hand > 21:
                print("You busted! You lose.")
            elif dealer_hand > 21 or player_hand > dealer_hand:
                winnings = bet * 2
                self.casino.current_user.deposit(winnings)
                print(f"You win! Your winnings: {winnings}. New balance: {self.casino.current_user.get_balance()}")
            else:
                print("You lose. Better luck next time!")


class Casino:
    def __init__(self):
        self.accounts = {}
        self.current_user = None
    
    def create_account(self, username: str) -> bool:
        if username in self.accounts:
            print("Account already exists!")
            return False
        self.accounts[username] = Account(username)
        print(f"Account for {username} created successfully.")
        return True
    
    def switch_account(self, username: str) -> bool:
        if username in self.accounts:
            self.current_user = self.accounts[username]
            print(f"Switched to account: {username}")
            return True
        else:
            print("Account does not exist!")
            return False


def main():
    casino = Casino()
    
    while True:
        menu = {
            '0': 'Exit',
            '1': 'Check Balance',
            '2': 'Deposit Money',
            '3': 'Withdraw Money',
            '4': 'Play Slots',
            '5': 'Play Roulette',
            '6': 'Play Blackjack',
            '7': 'Create account',
            '8': 'Change account'
        }

        print("\n--- Casino Menu ---")
        for key, value in menu.items():
            print(f"{key}. {value}")

        choice = input("Choose an option (0-8): ")

        if choice == '0':
            print("Thank you for playing! Goodbye!")
            break
        elif choice == '1':
            if casino.current_user:
                print(f"Your current balance is: {casino.current_user.get_balance()}")
            else:
                print("No account selected.")
        elif choice == '2':
            if casino.current_user:
                deposit_amount = int(input("Enter the amount to deposit: "))
                casino.current_user.deposit(deposit_amount)
            else:
                print("No account selected.")
        elif choice == '3':
            if casino.current_user:
                withdraw_amount = int(input("Enter the amount to withdraw: "))
                casino.current_user.withdraw(withdraw_amount)
            else:
                print("No account selected.")
        elif choice == '4':
            if casino.current_user:
                slot_game = SlotGame(casino)
                slot_game.play()
            else:
                print("No account selected.")
        elif choice == '5':
            if casino.current_user:
                roulette_game = RouletteGame(casino)
                roulette_game.play()
            else:
                print("No account selected.")
        elif choice == '6':
            if casino.current_user:
                blackjack_game = BlackjackGame(casino)
                blackjack_game.play()
            else:
                print("No account selected.")
        elif choice == '7':
            username = input("Enter your username to create an account: ")
            casino.create_account(username)
        elif choice == '8':
            username = input("Enter username to switch to: ")
            casino.switch_account(username)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
else:
    raise ImportError("This file is not meant to be imported")
