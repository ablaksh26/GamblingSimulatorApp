def validate_min_stake(stake):
    if stake < 100:
        raise ValueError("Minimum stake must be at least 100")