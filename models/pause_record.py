import time

class PauseRecord:
    def __init__(self, reason):
        self.reason = reason
        self.start = time.time()
        self.end = None

    def resume(self):
        self.end = time.time()

    def duration(self):
        return (self.end - self.start) if self.end else 0