import simpy as S


class Ride(S.Resource):
    def __init__(self, env: S.Environment, id: int, capacity: int, runtime: int):
        super().__init__(env, capacity)
        self.env = env
        self.runtime = runtime
        self._id = id

    def ride(self):
        yield self.env.timeout(self.runtime)

    @property
    def wait_time(self):
        current_run_remaining = self.runtime / 2
        return self.runtime * (len(self.queue) // self.capacity) + current_run_remaining

    @property
    def current_riders(self):
        return len(self.users)
