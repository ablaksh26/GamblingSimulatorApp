class SessionSummary:

    def display_session_summary(self, calculator):

        summary = calculator.summary()

        print("\nSession Summary")
        print(f"Net Profit: {summary['net_profit']}")
        print(f"Total Wins: {summary['wins']}")
        print(f"Total Losses: {summary['losses']}")
        print(f"Win Rate: {summary['win_rate']:.2f}%")
        print(f"Profit Factor: {summary['profit_factor']}")
        print(f"Max Win Streak: {summary['max_win_streak']}")
        print(f"Max Loss Streak: {summary['max_loss_streak']}")