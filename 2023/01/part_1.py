from string import digits

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
    first = find_first_number(string)
    second = find_first_number(string[::-1])
    return int(first + second)

def find_first_number(string: str) -> str:
    for char in string:
        if char in digits:
            return char
    raise Exception("No number found")

if __name__ == "__main__":
    main()