import simpy as S
import random


class Ride(S.Resource):
    def __init__(self, env: S.Environment, name: str, runtime: int, capacity: int):
        super().__init__(env, capacity)
        self.env = env
        self.runtime = runtime
        self.name = name

    def ride(self):
        yield self.env.timeout(self.runtime)

    @property
    def wait_time(self):
        current_run_remaining = self.runtime / 2
        return self.runtime * (len(self.queue) // self.capacity) + current_run_remaining

    @property
    def current_riders(self):
        return len(self.users)


class Activity:
    def __init__(self, env: S.Environment, name: str, mean_time):
        self.env = env
        self.name = name
        self.mean_time = mean_time

    def do_activity(self):
        # TODO: Use a more realistic distro, probably Weibull
        activity_time = int(max(random.gauss(self.mean_time, self.mean_time / 2), 1))
        yield self.env.timeout(activity_time)
