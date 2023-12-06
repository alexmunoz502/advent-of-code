import re


def main() -> None:
    lines = read_lines("input.txt")

    time = parse_int(lines[0])
    distance = parse_int(lines[1])

    n_possibilities = time + 1

    def calculate_distance(charge_time: int) -> int:
        travel_time = time - charge_time
        distance = travel_time * charge_time
        return distance

    # find lowest possible
    lowest_possible = 0

    lower_bound = 0
    upper_bound = n_possibilities

    while True:
        mid_point = (upper_bound + lower_bound) // 2
        if calculate_distance(mid_point) > distance:
            upper_bound = mid_point
        else:
            lower_bound = mid_point

        if upper_bound - lower_bound <= 1:
            lowest_possible = mid_point
            break

    # find highest possible
    highest_possible = 0

    lower_bound = 0
    upper_bound = n_possibilities

    while True:
        mid_point = (upper_bound + lower_bound) // 2
        if calculate_distance(mid_point) < distance:
            upper_bound = mid_point
        else:
            lower_bound = mid_point

        if upper_bound - lower_bound <= 1:
            highest_possible = mid_point
            break

    answer = n_possibilities - lowest_possible - (n_possibilities - highest_possible)
    print(answer)


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def normalize_spaces(string: str) -> str:
    return re.sub(r" +", "", string)


def parse_int(string: str) -> str:
    return int(normalize_spaces(string).split(":")[1].strip().split(" ")[0])


if __name__ == "__main__":
    main()
