from services.gambler_service import GamblerProfileService
from services.stake_management_service import StakeManagementService
from services.betting_service import BettingService
from services.game_session_manager import GameSessionManager
from services.win_loss_calculator import WinLossCalculator

from strategies.fixed_strategy import FixedAmountStrategy
from strategies.martingale_strategy import MartingaleStrategy
from strategies.weighted_probability_strategy import WeightedProbabilityStrategy

from models.session_parameters import SessionParameters
from models.odds_config import OddsConfig, OddsType

from validation.input_validator import InputValidator
from validation.validation_config import ValidationConfig


if __name__ == "__main__":

    gambler_service = GamblerProfileService()
    stake_service = StakeManagementService()
    betting_service = BettingService()
    session_manager = GameSessionManager()
    calculator = WinLossCalculator(WeightedProbabilityStrategy(0.05))

    validator = InputValidator(ValidationConfig())

    stake_validation = validator.validate_initial_stake(1000)
    limit_validation = validator.validate_limits(500, 1500, 1000)
    prob_validation = validator.validate_probability(0.5)

    if not (stake_validation.is_valid() and
            limit_validation.is_valid() and
            prob_validation.is_valid()):
        print("Validation Failed")
        print(stake_validation.summary())
        print(limit_validation.summary())
        print(prob_validation.summary())
        exit()

    gambler_service.create_gambler(
        "John", "john@test.com", 1000, 1500, 500
    )

    gambler_id = 1

    stake_service.initialize_stake(gambler_id, 1000)

    bet_check = validator.validate_bet_amount(100, 1000)
    if bet_check.is_valid():
        print(stake_service.process_bet(gambler_id, 100, True))

    bet_check = validator.validate_bet_amount(50, 1000)
    if bet_check.is_valid():
        print(stake_service.process_bet(gambler_id, 50, False))

    stake_service.deposit(gambler_id, 500)
    stake_service.withdraw(gambler_id, 200)

    print(stake_service.monitor(gambler_id))
    print(stake_service.report(gambler_id))

    print(betting_service.place_bet(gambler_id, 100, 0.5))

    strategy = FixedAmountStrategy(50)
    context = {}

    print(
        betting_service.place_bet_with_strategy(
            gambler_id, strategy, context, 0.5
        )
    )

    martingale = MartingaleStrategy(50)

    print(
        betting_service.place_consecutive_bets(
            gambler_id, martingale, 5, 0.5
        )
    )

    params = SessionParameters(
        500,
        2000,
        50,
        200,
        10,
        300,
        0.5
    )

    session_manager.start_new_session(
        gambler_id, params, 1000
    )

    print(
        session_manager.continue_session(
            gambler_id, betting_service, 5, 100
        )
    )

    session_manager.pause_session(gambler_id)
    session_manager.resume_session(gambler_id)

    print(
        session_manager.continue_session(
            gambler_id, betting_service, 5, 100
        )
    )

    odds = OddsConfig(OddsType.PROBABILITY_BASED, 0)
    stake = 1000

    for _ in range(10):
        result = calculator.play(100, stake, 0.5, odds)
        stake = result.stake_after
        print(result.to_dict())

    print(calculator.summary())

    print(gambler_service.get_statistics(gambler_id))
    print(gambler_service.validate_gambler(gambler_id))

    gambler_service.reset_gambler(gambler_id)
    gambler_service.deactivate(gambler_id)

    print("Done")