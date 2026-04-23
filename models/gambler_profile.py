class GamblerProfile:
    def __init__(self, *args):
        (
            self.id, self.name, self.email,
            self.initial_stake, self.current_stake,
            self.win_threshold, self.loss_threshold,
            self.total_bets, self.total_wins,
            self.total_losses, self.total_winnings,
            self.is_active
        ) = args