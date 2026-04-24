from services.gambler_service import GamblerProfileService
from services.stake_management_service import StakeManagementService
from services.betting_service import BettingService
from services.game_session_manager import GameSessionManager
from services.win_loss_calculator import WinLossCalculator

from strategies.fixed_strategy import FixedAmountStrategy
from strategies.martingale_strategy import MartingaleStrategy

from models.session_parameters import SessionParameters
from models.odds_config import OddsConfig, OddsType


if __name__ == "__main__":
    print("App started...\n")

    gambler_service = GamblerProfileService()
    stake_service = StakeManagementService()
    betting_service = BettingService()
    session_manager = GameSessionManager()
    calculator = WinLossCalculator()

    print("Creating gambler...")
    gambler_service.create_gambler(
        "John", "john@test.com", 1000, 1500, 500
    )

    gambler_id = 1 

    print("Initializing stake...")
    stake_service.initialize_stake(gambler_id, 1000)

    print("\nStake Operations")

    print("Bet WIN:", stake_service.process_bet(gambler_id, 100, True))
    print("Bet LOSS:", stake_service.process_bet(gambler_id, 50, False))

    stake_service.deposit(gambler_id, 500)
    stake_service.withdraw(gambler_id, 200)

    print("Monitor:", stake_service.monitor(gambler_id))
    print("Report:", stake_service.report(gambler_id))

    print("\nBetting Engine")

    result = betting_service.place_bet(gambler_id, 100, 0.5)
    print("Single Bet:", result)

    strategy = FixedAmountStrategy(50)
    context = {}

    result = betting_service.place_bet_with_strategy(
        gambler_id, strategy, context, 0.5
    )
    print("Strategy Bet:", result)

    martingale = MartingaleStrategy(50)

    results = betting_service.place_consecutive_bets(
        gambler_id, martingale, 5, 0.5
    )
    print("Martingale Results:", results)

    print("\nGame Session")

    params = SessionParameters(
        min_stake=500,
        max_stake=2000,
        min_bet=50,
        max_bet=200,
        max_games=10,
        max_duration=300,
        probability=0.5
    )

    session = session_manager.start_new_session(
        gambler_id, params, 1000
    )

    summary = session_manager.continue_session(
        gambler_id, betting_service, 5, 100
    )
    print("Session Progress:", summary)

    session_manager.pause_session(gambler_id)
    print("Session paused")

    session_manager.resume_session(gambler_id)
    print("Session resumed")

    summary = session_manager.continue_session(
        gambler_id, betting_service, 5, 100
    )
    print("Final Session:", summary)

    print("\nWin/Loss Calculation")

    odds = OddsConfig(OddsType.FIXED, 2)
    stake = 1000

    for i in range(5):
        result = calculator.play(100, stake, 0.5, odds)
        stake = result.stake_after
        print(f"Game {i+1}:", result.to_dict())

    print("\nWin/Loss Summary:")
    print(calculator.get_summary())

    
    print("\nGambler Stats")
    print(gambler_service.get_statistics(gambler_id))

    print("\nEligible:", gambler_service.validate_gambler(gambler_id))

   
    print("\nReset gambler...")
    gambler_service.reset_gambler(gambler_id)

    print("Deactivate gambler...")
    gambler_service.deactivate(gambler_id)

    print("\nDemo completed successfully!")