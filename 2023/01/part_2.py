import re


PATTERN = "(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))"
NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def main() -> None:
    lines = to_lines("input.txt")
    sum = 0
    for line in lines:
        sum += calculate_calibration_value(line)
    print(sum)


def to_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def calculate_calibration_value(string: str) -> int:
    matches = find_all(string)
    first = matches[0]
    second = matches[-1]
    return int(first + second)


def find_all(string: str) -> list:
    matches = re.findall(PATTERN, string)
    return list(map(convert, matches))


def convert(string: str) -> str:
    if string in NUMBERS:
        return NUMBERS[string]
    return string


if __name__ == "__main__":
    main()