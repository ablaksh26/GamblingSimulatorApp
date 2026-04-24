from user.game_status_display import GameStatusDisplay
from user.interactive_menu import InteractiveMenu
from user.session_summary import SessionSummary

from services.win_loss_calculator import WinLossCalculator
from models.odds_config import OddsConfig, OddsType
from validation.input_validator import InputValidator
from validation.validation_config import ValidationConfig


class SimpleGameEngine:

    def __init__(self, gambler_id, stake_service):

        self.gambler_id = gambler_id
        self.stake_service = stake_service

        self.display = GameStatusDisplay()
        self.menu = InteractiveMenu()
        self.summary = SessionSummary()

        self.calculator = WinLossCalculator()
        self.validator = InputValidator(ValidationConfig())

        self.odds = OddsConfig(OddsType.FIXED, 2)

    def run(self):

        while True:

            self.menu.display_main_menu()
            choice = self.menu.get_choice()

            if choice == 1:
                self.display.display_current_status(
                    self.gambler_id,
                    self.stake_service
                )

            elif choice == 2:
                self.handle_single_bet()

            elif choice == 3:
                self.handle_multiple_bets()

            elif choice == 4:
                self.summary.display_session_summary(self.calculator)

            elif choice == 5:
                print("Exiting...")
                break

            else:
                print("Invalid choice")

    def handle_single_bet(self):

        bet = self.menu.prompt_bet_amount()

        if bet is None:
            print("Invalid input")
            return

        stake = self.stake_service.get_current_stake(self.gambler_id)

        validation = self.validator.validate_bet_amount(bet, stake)

        if not validation.is_valid():
            print(validation.summary())
            return

        result = self.calculator.play(
            bet,
            stake,
            0.5,
            self.odds
        )

        self.stake_service.update_stake(self.gambler_id, result.stake_after)

        self.display.display_game_outcome(result)

    def handle_multiple_bets(self):

        for _ in range(5):
            self.handle_single_b