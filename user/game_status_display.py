class GameStatusDisplay:

    def display_current_status(self, gambler_id, stake_service):
        stake = stake_service.get_current_stake(gambler_id)
        print("\nCurrent Status")
        print(f"Gambler ID: {gambler_id}")
        print(f"Current Stake: {stake}")

    def display_game_outcome(self, result):
        print("\nGame Result")
        print(f"Outcome: {result.outcome}")
        print(f"Bet: {result.bet_amount}")
        print(f"Win: {result.win_amount}")
        print(f"Loss: {result.loss_amount}")
        print(f"Stake Before: {result.stake_before}")
        print(f"Stake After: {result.stake_after}")