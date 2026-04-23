from app.models.gaming_session import GamingSession

class GameSessionManager:

    def __init__(self):
        self.active_sessions = {}
        self.completed_sessions = []

    # START
    def start_new_session(self, gambler_id, parameters, initial_stake):
        if gambler_id in self.active_sessions:
            raise Exception("Session already active")

        session = GamingSession(gambler_id, parameters, initial_stake)
        session.start()

        self.active_sessions[gambler_id] = session
        return session

    # CONTINUE
    def continue_session(self, gambler_id, betting_service, rounds, bet_amount):
        session = self.active_sessions.get(gambler_id)

        if not session:
            raise Exception("No active session")

        for _ in range(rounds):
            if session.status != session.status.ACTIVE:
                break

            session.play_game(betting_service, bet_amount)

        if session.status != session.status.ACTIVE:
            self._end_session(gambler_id)

        return session.summary()

    # PAUSE
    def pause_session(self, gambler_id):
        self.active_sessions[gambler_id].pause()

    # RESUME
    def resume_session(self, gambler_id):
        self.active_sessions[gambler_id].resume()

    # END
    def end_session(self, gambler_id):
        session = self.active_sessions.pop(gambler_id)
        session._end(session.status, "MANUAL")
        self.completed_sessions.append(session)

    def _end_session(self, gambler_id):
        session = self.active_sessions.pop(gambler_id)
        self.completed_sessions.append(session)