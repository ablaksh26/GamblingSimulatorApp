class InteractiveMenu:

    def display_main_menu(self):
        print("\n==== MAIN MENU ====")
        print("1. Show Status")
        print("2. Place Bet")
        print("3. Play Multiple Bets")
        print("4. Show Summary")
        print("5. Exit")

    def get_choice(self):
        try:
            return int(input("Enter choice: "))
        except:
            return -1

    def prompt_bet_amount(self):
        try:
            return float(input("Enter bet amount: "))
        except:
            return None