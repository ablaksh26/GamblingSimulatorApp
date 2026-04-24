from services.gambler_service import GamblerProfileService
from services.stake_management_service import StakeManagementService

from validation.input_validator import InputValidator
from validation.validation_config import ValidationConfig

from user.simple_game_engine import SimpleGameEngine


if __name__ == "__main__":

    gambler_service = GamblerProfileService()
    stake_service = StakeManagementService()
    validator = InputValidator(ValidationConfig())

    stake_validation = validator.validate_initial_stake(1000)
    limit_validation = validator.validate_limits(500, 1500, 1000)

    if not (stake_validation.is_valid() and limit_validation.is_valid()):
        print("Validation Failed")
        print(stake_validation.summary())
        print(limit_validation.summary())
        exit()

    gambler_service.create_gambler(
        "John",
        "john@test.com",
        1000,
        1500,
        500
    )

    gambler_id = 1

    stake_service.initialize_stake(gambler_id, 1000)

    engine = SimpleGameEngine(gambler_id, stake_service)
    engine.run()

    print(gambler_service.get_statistics(gambler_id))
    print(gambler_service.validate_gambler(gambler_id))