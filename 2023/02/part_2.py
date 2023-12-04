import re
from typing import TypedDict

COLORS = ["red", "green", "blue"]


class Count(TypedDict):
    red: int
    green: int
    blue: int


class Game(TypedDict):
    id_: int
    rounds: list[Count]


def main() -> None:
    lines = read_lines("input.txt")
    games = lines_to_games(lines)

    sum = 0

    for game in games:
        minimum = find_minimum_count(game["rounds"])
        power = minimum["red"] * minimum["green"] * minimum["blue"]
        sum += power

    print(sum)


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def lines_to_games(lines: list[str]) -> list[Game]:
    games = []
    for line in lines:
        games.append(line_to_game(line))
    return games


def line_to_game(string: str) -> Game:
    parts = string.split(":")
    match_ = re.search(r"Game (\d+)", parts[0])
    if not match_:
        raise ValueError("There is an error with the input file.")

    id_ = int(match_.group(1))

    rounds: list[Count] = parse_rounds(parts[1])

    return {"id_": id_, "rounds": rounds}


def parse_rounds(string: str) -> list[Count]:
    return [parse_round(x) for x in string.split(";")]


def parse_round(string: str) -> Count:
    count: Count = {"red": 0, "blue": 0, "green": 0}
    matches = re.findall(r"(\d+) (blue|green|red)", string)
    for match in matches:
        count[match[1]] = int(match[0])
    return count


def check_round(config: Count, round_: Count) -> bool:
    # check if each exceeds allowed amount
    for color, count in round_.items():
        if config[color] < count:
            return False
    return True


def find_minimum_count(rounds: list[Count]) -> Count:
    minimum: Count = {"red": 0, "blue": 0, "green": 0}
    for round_ in rounds:
        for color, count in round_.items():
            if minimum[color] < count:
                minimum[color] = count
    return minimum


if __name__ == "__main__":
    main()
