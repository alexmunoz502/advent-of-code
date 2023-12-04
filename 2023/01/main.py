from string import digits
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

def to_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def part_1():
    sum = 0
    lines = to_lines("input.txt")
    for line in lines:
        sum += calculate_code(line)
    return sum


def part_2():
    sum = 0

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            sum += calculate_code_2(line)

    print(sum)

def calculate_code(string: str) -> int:
    first = find_first_number(string)
    second = find_first_number(string[::-1])
    return int(first + second)

def find_first_number(string: str) -> str:
    for char in string:
        if char in digits:
            return char
    raise Exception("No number found")



def calculate_code_2(string: str) -> int:
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
    part_1()
    part_2()