from config.db_config import get_connection
from repository.stake_repository import StakeRepository
from models.transaction_type import TransactionType
from models.stake_boundary import StakeBoundary

class StakeManagementService:

    def __init__(self):
        self.repo = StakeRepository()
        self.boundary = StakeBoundary(100, 10000)

    # INITIALIZE
    def initialize_stake(self, gambler_id, amount):
        status = self.boundary.validate(amount)
        if status != "OK":
            raise Exception("Invalid initial stake")

        conn = get_connection()
        cursor = conn.cursor()

        self.repo.insert_transaction(cursor, (
            gambler_id,
            TransactionType.INITIAL_STAKE.value,
            amount,
            amount,
            None
        ))

        conn.commit()
        cursor.close()
        conn.close()

    # PROCESS BET
    def process_bet(self, gambler_id, amount, won):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT current_stake FROM gambler_profile WHERE id=%s", (gambler_id,))
        stake = cursor.fetchone()[0]

        if stake < amount:
            raise Exception("Insufficient balance")

        if won:
            stake += amount
            t_type = TransactionType.BET_WIN.value
        else:
            stake -= amount
            t_type = TransactionType.BET_LOSS.value

        cursor.execute("UPDATE gambler_profile SET current_stake=%s WHERE id=%s", (stake, gambler_id))

        self.repo.insert_transaction(cursor, (
            gambler_id,
            t_type,
            amount,
            stake,
            "BET123"
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return self.boundary.warning(stake)

    # DEPOSIT
    def deposit(self, gambler_id, amount):
        return self._adjust(gambler_id, amount, TransactionType.DEPOSIT)

    # WITHDRAW
    def withdraw(self, gambler_id, amount):
        return self._adjust(gambler_id, -amount, TransactionType.WITHDRAWAL)

    def _adjust(self, gambler_id, amount, t_type):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT current_stake FROM gambler_profile WHERE id=%s", (gambler_id,))
        stake = cursor.fetchone()[0]

        stake += amount

        cursor.execute("UPDATE gambler_profile SET current_stake=%s WHERE id=%s", (stake, gambler_id))

        self.repo.insert_transaction(cursor, (
            gambler_id,
            t_type.value,
            abs(amount),
            stake,
            None
        ))

        conn.commit()
        cursor.close()
        conn.close()

    # MONITOR
    def monitor(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor()

        rows = self.repo.get_transactions(cursor, gambler_id)

        balances = [r[4] for r in rows]

        peak = max(balances) if balances else 0
        low = min(balances) if balances else 0
        volatility = peak - low

        cursor.close()
        conn.close()

        return {
            "peak": peak,
            "lowest": low,
            "volatility": volatility
        }

    # REPORT
    def report(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor()

        rows = self.repo.get_transactions(cursor, gambler_id)

        total = len(rows)
        wins = sum(1 for r in rows if r[2] == "BET_WIN")
        losses = sum(1 for r in rows if r[2] == "BET_LOSS")

        cursor.close()
        conn.close()

        return {
            "total_transactions": total,
            "wins": wins,
            "losses": losses,
            "history": rows
        }

    def get_current_stake(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT balance_after
            FROM stake_transaction
            WHERE gambler_id = %s
            ORDER BY id DESC
            LIMIT 1
        """, (gambler_id,))

        row = cursor.fetchone()

        conn.close()

        return row[0] if row else 0


    def update_stake(self, gambler_id, new_stake):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO stake_transaction
            (gambler_id, transaction_type, amount, balance_after)
            VALUES (%s, %s, %s, %s)
        """, (gambler_id, "ADJUSTMENT", 0, new_stake))

        conn.commit()
        conn.close()