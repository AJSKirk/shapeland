import simpy as S
from ride import Ride
from guest import Guest


def main():
    env = S.Environment()
    rides = [Ride(env, 1, 2, 5), Ride(env, 2, 2, 8)]

    guests = [Guest(env, i, 10) for i in range(10)]

    for guest in guests:
        env.process(guest.run(rides))

    env.run(until=26)


if __name__ == "__main__":
    main()
