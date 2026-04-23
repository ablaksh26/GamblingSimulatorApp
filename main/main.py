from services.gambler_service import GamblerProfileService
from services.stake_management_service import StakeManagementService



if __name__ == "__main__":
    print("App started...\n")

    gambler_service = GamblerProfileService()
    stake_service = StakeManagementService()

    print("Creating gambler...")
    gambler_service.create_gambler("John", "john@test.com", 1000, 1500, 500)

    gambler_id = 1   # adjust if needed

    print("Initializing stake...")
    stake_service.initialize_stake(gambler_id, 1000)

    print("Processing bets...")

    warning = stake_service.process_bet(gambler_id, 100, True)
    print("Bet 1 (WIN):", warning)

    warning = stake_service.process_bet(gambler_id, 50, False)
    print("Bet 2 (LOSS):", warning)

    warning = stake_service.process_bet(gambler_id, 200, True)
    print("Bet 3 (WIN):", warning)

    print("Deposit & Withdraw...")

    stake_service.deposit(gambler_id, 500)
    print("Deposited 500")

    stake_service.withdraw(gambler_id, 200)
    print("Withdrew 200")

    print("\nGambler Statistics:")
    stats = gambler_service.get_statistics(gambler_id)
    print(stats)

    print("\nStake Monitoring:")
    monitor = stake_service.monitor(gambler_id)
    print(monitor)

    print("\nEligibility Check:")
    print("Eligible:", gambler_service.validate_gambler(gambler_id))

    print("\nStake History Report:")
    report = stake_service.report(gambler_id)
    print("Total Transactions:", report["total_transactions"])
    print("Wins:", report["wins"])
    print("Losses:", report["losses"])

    print("\nTransaction History:")
    for tx in report["history"]:
        print(tx)

    print("\nResetting gambler...")
    gambler_service.reset_gambler(gambler_id)

    print("Deactivating gambler...")
    gambler_service.deactivate(gambler_id)

    print("\nDemo completed successfully!")