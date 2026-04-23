class GamblerRepository:

    def create(self, cursor, data):
        cursor.execute("""
            INSERT INTO gambler_profile
            (name, email, initial_stake, current_stake, win_threshold, loss_threshold)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, data)

    def find_by_id(self, cursor, gambler_id):
        cursor.execute("SELECT * FROM gambler_profile WHERE id=%s", (gambler_id,))
        return cursor.fetchone()

    def update_name_email(self, cursor, gambler_id, name, email):
        if name:
            cursor.execute("UPDATE gambler_profile SET name=%s WHERE id=%s", (name, gambler_id))
        if email:
            cursor.execute("UPDATE gambler_profile SET email=%s WHERE id=%s", (email, gambler_id))

    def update_after_win(self, cursor, gambler_id, stake, amount):
        cursor.execute("""
            UPDATE gambler_profile
            SET current_stake=%s,
                total_wins=total_wins+1,
                total_bets=total_bets+1,
                total_winnings=total_winnings+%s
            WHERE id=%s
        """, (stake, amount, gambler_id))

    def update_after_loss(self, cursor, gambler_id, stake):
        cursor.execute("""
            UPDATE gambler_profile
            SET current_stake=%s,
                total_losses=total_losses+1,
                total_bets=total_bets+1
            WHERE id=%s
        """, (stake, gambler_id))

    def reset(self, cursor, gambler_id, stake, win_th, loss_th):
        cursor.execute("""
            UPDATE gambler_profile
            SET current_stake=%s,
                win_threshold=%s,
                loss_threshold=%s,
                total_bets=0,
                total_wins=0,
                total_losses=0,
                total_winnings=0
            WHERE id=%s
        """, (stake, win_th, loss_th, gambler_id))

    def deactivate(self, cursor, gambler_id):
        cursor.execute("UPDATE gambler_profile SET is_active=FALSE WHERE id=%s", (gambler_id,))