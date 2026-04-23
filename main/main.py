from services.gambler_service import GamblerProfileService

if __name__ == "__main__":
    print("app started....")
    service = GamblerProfileService()

    print("service called.....")
    service.create_gambler("John", "john@test.com", 1000, 1500, 500)

    gid = 1

    service.update_gambler(gid, name="John Updated")

    service.record_bet(gid, 100, True)
    service.record_bet(gid, 50, False)

    stats = service.get_statistics(gid)
    print(stats)

    print("Eligible:", service.validate_gambler(gid))

    service.reset_gambler(gid)

    service.deactivate(gid)