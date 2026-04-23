import time
from app.models.session_enums import SessionStatus, SessionEndReason
from app.models.game_record import GameRecord
from app.models.pause_record import PauseRecord


class GamingSession:

    def __init__(self, gambler_id, parameters, initial_stake):
        self.gambler_id = gambler_id
        self.parameters = parameters
        self.status = SessionStatus.INITIALIZED

        self.start_time = None
        self.end_time = None

        self.games = []
        self.pauses = []

        self.current_stake = initial_stake
        self.total_pause_time = 0

    # START
    def start(self):
        self.start_time = time.time()
        self.status = SessionStatus.ACTIVE

    # PLAY GAME
    def play_game(self, betting_service, bet_amount):
        if self.status != SessionStatus.ACTIVE:
            raise Exception("Session not active")

        if bet_amount > self.current_stake:
            raise Exception("Insufficient stake")

        start = time.time()

        outcome = betting_service.place_bet(
            self.gambler_id,
            bet_amount,
            self.parameters.probability
        )

        before = self.current_stake

        if outcome == "WIN":
            self.current_stake += bet_amount
        else:
            self.current_stake -= bet_amount

        record = GameRecord(bet_amount, outcome, before, self.current_stake)
        record.set_duration(start)

        self.games.append(record)

        self._check_boundaries()

    # CHECK LIMITS
    def _check_boundaries(self):
        if self.current_stake >= self.parameters.max_stake:
            self._end(SessionStatus.ENDED_WIN, SessionEndReason.UPPER_LIMIT)

        elif self.current_stake <= self.parameters.min_stake:
            self._end(SessionStatus.ENDED_LOSS, SessionEndReason.LOWER_LIMIT)

    # PAUSE
    def pause(self, reason="User Pause"):
        if self.status != SessionStatus.ACTIVE:
            return

        self.status = SessionStatus.PAUSED
        pause = PauseRecord(reason)
        self.pauses.append(pause)

    # RESUME
    def resume(self):
        if self.status != SessionStatus.PAUSED:
            return

        last_pause = self.pauses[-1]
        last_pause.resume()

        self.total_pause_time += last_pause.duration()
        self.status = SessionStatus.ACTIVE

    # END
    def _end(self, status, reason):
        self.status = status
        self.end_time = time.time()
        self.end_reason = reason

    # SUMMARY
    def summary(self):
        total_games = len(self.games)
        wins = sum(1 for g in self.games if g.outcome == "WIN")

        return {
            "status": self.status.value,
            "games_played": total_games,
            "wins": wins,
            "losses": total_games - wins,
            "final_stake": self.current_stake,
            "duration": (self.end_time or time.time()) - self.start_time,
            "pause_time": self.total_pause_time
        }