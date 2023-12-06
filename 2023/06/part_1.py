import re
from functools import reduce


def main() -> None:
    lines = read_lines("input.txt")

    times = parse_ints(lines[0])
    distances = parse_ints(lines[1])

    n_outcomes = 0
    winning_scenarios = []
    for i, time in enumerate(times):
        outcomes = get_outcomes(time)
        n_outcomes += len(outcomes)
        n_winning = 0
        for outcome in outcomes:
            if outcome > distances[i]:
                n_winning += 1
        winning_scenarios.append(n_winning)

    print(lines)
    print(times)
    print(distances)
    print(reduce(lambda x, y: x * y, winning_scenarios))
    print(n_outcomes)


def get_outcomes(time: int) -> list[int]:
    distances = []
    charge_time = time
    while charge_time >= 0:
        travel_time = time - charge_time
        distance = travel_time * charge_time
        distances.append(distance)
        charge_time -= 1
    return distances


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def normalize_spaces(string: str) -> str:
    return re.sub(r" +", " ", string)


def parse_ints(string: str) -> str:
    return [int(n) for n in normalize_spaces(string).split(":")[1].strip().split(" ")]


if __name__ == "__main__":
    main()
