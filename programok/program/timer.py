import time


class Timer:

    def __init__(self):
        self.start_time = None
        self.elapsed_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.elapsed_time = time.perf_counter() - self.start_time
