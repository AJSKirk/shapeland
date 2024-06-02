import simpy as S
from ride import Ride

import random
from typing import Iterable


class Guest:
    def __init__(self, env: S.Environment, id: int, max_wait: int):
        self.env = env
        self._id = id

        self.max_wait = max_wait

    def run(self, available_rides=Iterable[Ride]):
        while True:
            yield self.env.process(self.ride(random.choice(available_rides)))

    def ride(self, ride: Ride):
        print(f"Guest {self._id} evaluating ride {ride._id}  at time {self.env.now} - wait is {ride.wait_time}")
        if ride.wait_time >= self.max_wait:
            print(f"Guest {self._id} balked at wait time of {ride.wait_time}")
            return

        with ride.request() as req:
            yield req  # Wait in queue
            print(f"Guest {self._id} started the ride at time {self.env.now}")
            yield self.env.process(ride.ride())
            print(f"Guest {self._id} finished the ride at time {self.env.now}")