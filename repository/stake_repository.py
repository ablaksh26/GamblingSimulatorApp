class StakeRepository:

    def insert_transaction(self, cursor, data):
        cursor.execute("""
            INSERT INTO stake_transaction
            (gambler_id, transaction_type, amount, balance_after, bet_id)
            VALUES (%s, %s, %s, %s, %s)
        """, data)

    def get_transactions(self, cursor, gambler_id):
        cursor.execute("""
            SELECT * FROM stake_transaction
            WHERE gambler_id=%s
            ORDER BY created_at
        """, (gambler_id,))
        return cursor.fetchall()