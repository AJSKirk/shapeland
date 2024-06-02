import simpy as S
from ride import Activity, Ride
from guest import Guest


def main():
    env = S.Environment()
    activities = [
        Activity(env, "Sightseeing", 5),
        Activity(env, "Show", 30),
        Activity(env, "Merchandise", 30),
        Activity(env, "Food", 45),
    ]

    rides = [
        Ride(env, "Alpha", 10, int(3000 * 10 / 60)),
        Ride(env, "Beta", 5, int(2400 * 5 / 60)),
        Ride(env, "Gamma", 15, int(2000 * 15 / 60)),
        Ride(env, "Delta", 5, int(1200 * 5 / 60)),
        Ride(env, "Epsilon", 10, int(2000 * 10 / 60)),
        Ride(env, "Zeta", 6, int(2000 * 6 / 60)),
        Ride(env, "Eta", 12, int(2400 * 12 / 60)),
    ]

    guests = [Guest(env, i, 10) for i in range(2000)]

    for guest in guests:
        env.process(guest.run(rides))

    env.run(until=60 * 8)


if __name__ == "__main__":
    main()
