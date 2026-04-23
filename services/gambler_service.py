from config.db_config import get_connection
from repository.gambler_repository import GamblerRepository
from utils.validators import validate_min_stake

class GamblerProfileService:

    def __init__(self):
        self.repo = GamblerRepository()

    def create_gambler(self, name, email, initial_stake, win_th, loss_th):
        print("creating.......")
        validate_min_stake(initial_stake)

        conn = get_connection()
        cursor = conn.cursor()

        self.repo.create(cursor, (name, email, initial_stake, initial_stake, win_th, loss_th))

        conn.commit()
        cursor.close()
        conn.close()

    def update_gambler(self, gambler_id, name=None, email=None):
        conn = get_connection()
        cursor = conn.cursor()

        self.repo.update_name_email(cursor, gambler_id, name, email)

        conn.commit()
        cursor.close()
        conn.close()

    def get_statistics(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor()

        row = self.repo.find_by_id(cursor, gambler_id)

        cursor.close()
        conn.close()

        if not row:
            raise Exception("Gambler not found")

        total_bets = row[7]
        wins = row[8]
        losses = row[9]
        winnings = row[10]
        current_stake = row[4]
        initial_stake = row[3]

        win_rate = (wins / total_bets * 100) if total_bets else 0
        net_profit = current_stake - initial_stake
        avg_bet = (winnings / total_bets) if total_bets else 0

        return {
            "total_bets": total_bets,
            "wins": wins,
            "losses": losses,
            "win_rate": round(win_rate, 2),
            "net_profit": net_profit,
            "avg_bet": round(avg_bet, 2),
            "current_stake": current_stake
        }

    def validate_gambler(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor()

        row = self.repo.find_by_id(cursor, gambler_id)

        cursor.close()
        conn.close()

        if not row:
            return False

        stake, win_th, loss_th, active = row[4], row[5], row[6], row[11]

        return active and loss_th < stake < win_th

    def reset_gambler(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor()

        row = self.repo.find_by_id(cursor, gambler_id)
        initial = row[3]

        win_th = initial * 1.5
        loss_th = initial * 0.5

        self.repo.reset(cursor, gambler_id, initial, win_th, loss_th)

        conn.commit()
        cursor.close()
        conn.close()

    def record_bet(self, gambler_id, amount, won):
        conn = get_connection()
        cursor = conn.cursor()

        row = self.repo.find_by_id(cursor, gambler_id)
        stake = row[4]

        if stake < amount:
            raise Exception("Insufficient funds")

        if won:
            stake += amount
            self.repo.update_after_win(cursor, gambler_id, stake, amount)
        else:
            stake -= amount
            self.repo.update_after_loss(cursor, gambler_id, stake)

        conn.commit()
        cursor.close()
        conn.close()

    def deactivate(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor()

        self.repo.deactivate(cursor, gambler_id)

        conn.commit()
        cursor.close()
        conn.close()