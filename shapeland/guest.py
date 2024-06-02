import simpy as S
from ride import Activity, Ride

import random
from typing import Iterable


class Guest:
    def __init__(self, env: S.Environment, id: int, max_wait: int):
        self.env = env
        self._id = id

        self.max_wait = max_wait
        self.ride_preference = 0.5
        self.ride_history = []
        self.allow_repeats = True

        self.entrance_time = self.env.now
        self.time_preference = 4 * 60

    def run(self, activities=Iterable[Activity], rides=Iterable[Ride]):
        while not self.decide_to_leave():
            # Decide on activity or ride
            if random.uniform(0, 1) <= self.ride_preference:  # Ride
                ride = random.choice(self.valid_rides(rides))
                yield self.env.process(self.try_ride(ride))

            else:  # Do an activity
                # TODO: Make this a weighted choice
                activity = random.choice(activities)
                yield self.env.process(activity.do_activity())

    def try_ride(self, ride: Ride):
        if ride.wait_time >= self.max_wait:
            return

        with ride.request() as req:
            yield req  # Wait in queue
            yield self.env.process(ride.ride())
            self.ride_history.append(ride)

    def valid_rides(self, rides: Iterable[Ride]):
        allowed_rides = rides
        if not self.allow_repeats:
            # TODO: Also remove any FastPasses held
            allowed_rides = [r for r in allowed_rides if r not in self.ride_history]

        # TODO: Adult/child eligibility
        return allowed_rides

    def decide_to_leave(self):
        if self.env.now == self.entrance_time:  # Never leave immediately
            return False

        return self.env.now - self.entrance_time - self.time_preference > random.gauss(0, 1)
