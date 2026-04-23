from services.gambler_service import GamblerProfileService
from services.stake_management_service import StakeManagementService
from services.betting_service import BettingService

from strategies.fixed_strategy import FixedAmountStrategy
from strategies.martingale_strategy import MartingaleStrategy


if __name__ == "__main__":
    print("App started...\n")

    gambler_service = GamblerProfileService()
    stake_service = StakeManagementService()
    betting_service = BettingService()

    # -------------------------------
    # 1. CREATE GAMBLER
    # -------------------------------
    print("Creating gambler...")
    gambler_service.create_gambler("John", "john@test.com", 1000, 1500, 500)

    gambler_id = 1   # 👈 IMPORTANT

    # -------------------------------
    # 2. INITIALIZE STAKE
    # -------------------------------
    print("Initializing stake...")
    stake_service.initialize_stake(gambler_id, 1000)

    # -------------------------------
    # 3. BETTING SECTION
    # -------------------------------
    print("\nBetting Section")

    # SINGLE BET
    result = betting_service.place_bet(gambler_id, 100, 0.5)
    print("Single Bet Result:", result)

    # STRATEGY BET
    strategy = FixedAmountStrategy(50)
    context = {}

    result = betting_service.place_bet_with_strategy(gambler_id, strategy, context, 0.5)
    print("Strategy Bet:", result)

    # MARTINGALE SESSION
    martingale = MartingaleStrategy(50)

    results = betting_service.place_consecutive_bets(gambler_id, martingale, 5, 0.5)
    print("Martingale Session:", results)

    print("\nDemo completed!")