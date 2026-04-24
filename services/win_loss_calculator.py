from models.game_result import GameResult
from models.running_totals import RunningTotals
from models.win_loss_statistics import WinLossStatistics
from strategies.random_outcome_strategy import RandomOutcomeStrategy

class WinLossCalculator:

    def __init__(self, strategy=None):
        self.strategy = strategy or RandomOutcomeStrategy()
        self.totals = RunningTotals()
        self.stats = WinLossStatistics()

    def play(self, bet, stake, probability, odds):

        outcome = self.strategy.determine(probability)

        result = GameResult(
            bet,
            outcome,
            stake,
            odds,
            probability
        )

        self.totals.update(result)
        self.stats.update(result)

        return result

    def summary(self):

        stats = self.stats.summary()

        return {
            "net_profit": self.totals.net_profit,
            "total_winnings": self.totals.total_winnings,
            "total_losses": self.totals.total_losses,
            "profit_factor": self.totals.profit_factor(),
            "win_rate": stats["win_rate"],
            "wins": stats["wins"],
            "losses": stats["losses"],
            "avg_win": stats["avg_win"],
            "avg_loss": stats["avg_loss"],
            "largest_win": stats["largest_win"],
            "largest_loss": stats["largest_loss"],
            "max_win_streak": stats["max_win_streak"],
            "max_loss_streak": stats["max_loss_streak"]
        }