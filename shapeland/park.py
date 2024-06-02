import simpy as S
from ride import Ride
from guest import Guest


def main():
    env = S.Environment()
    ride = Ride(env, 2, 5)

    guests = [Guest(env, i) for i in range(10)]

    for guest in guests:
        env.process(guest.run([ride]))

    env.run(until=26)


if __name__ == "__main__":
    main()
