import simpy as S


class Ride(S.Resource):
    def __init__(self, env: S.Environment, capacity: int, runtime: int):
        super().__init__(env, capacity)
        self.env = env
        self.runtime = runtime

    def ride(self):
        yield self.env.timeout(self.runtime)

    @property
    def wait_time(self):
        return len(self.queue)

    @property
    def current_riders(self):
        return len(self.users)
