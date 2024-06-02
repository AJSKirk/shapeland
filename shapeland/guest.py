import simpy as S
from ride import Ride

import random
from typing import Iterable


class Guest:
    def __init__(self, env: S.Environment, id: int):
        self.env = env
        self._id = id

    def run(self, available_rides=Iterable[Ride]):
        while True:
            yield self.env.process(self.ride(random.choice(available_rides)))

    def ride(self, ride: Ride):
        print(f"Guest {self._id} evaluating the queue at time {self.env.now} - queue is {ride.wait_time}")
        with ride.request() as req:
            yield req  # Wait in queue
            print(f"Guest {self._id} started the ride at time {self.env.now}")
            yield self.env.process(ride.ride())
            print(f"Guest {self._id} finished the ride at time {self.env.now}")