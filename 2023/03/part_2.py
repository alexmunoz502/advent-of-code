from string import punctuation, digits

SYMBOLS = "*"

Grid = list[list[str]]


def main(filename: str) -> None:
    lines = read_lines(filename)
    grid = to_multi_dimensional_list(lines)
    total = parse(grid)

    print(total)


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def to_multi_dimensional_list(lines: list[str]) -> Grid:
    return [[char for char in line] for line in lines]


def parse(grid: Grid) -> int:
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    sum = 0

    numbers = {}
    match_ = ""
    symbol_found = ""

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col in digits:
                match_ += col
            else:
                if symbol_found:
                    print(f"Found Match: {match_}")
                    value = int(match_)
                    if symbol_found in numbers:
                        numbers[symbol_found].append(value)
                    else:
                        numbers[symbol_found] = [value]
                    symbol_found = ""
                match_ = ""
                continue  # don't need to check adjacent if not a digit

            # scan for adjacent symbols
            # top-left: i - 1, j - 1
            if i > 0 and j > 0:
                if grid[i - 1][j - 1] in SYMBOLS:
                    symbol_found = f"[{i - 1}, {j - 1}]"
                    continue
            # top i - 1, j
            if i > 0:
                if grid[i - 1][j] in SYMBOLS:
                    symbol_found = f"[{i - 1}, {j}]"
                    continue
            # top-right i - 1, j + 1
            if i > 0 and j < max_col:
                if grid[i - 1][j + 1] in SYMBOLS:
                    symbol_found = f"[{i - 1}, {j + 1}]"
                    continue
            # left i, j - 1
            if j > 0:
                if grid[i][j - 1] in SYMBOLS:
                    symbol_found = f"[{i}, {j - 1}]"
                    continue
            # right i, j + 1
            if j < max_col:
                if grid[i][j + 1] in SYMBOLS:
                    symbol_found = f"[{i}, {j + 1}]"
                    continue
            # bottom-left i + 1, j - 1
            if i < max_row and j > 0:
                if grid[i + 1][j - 1] in SYMBOLS:
                    symbol_found = f"[{i + 1}, {j - 1}]"
                    continue
            # bottom i + 1, j
            if i < max_row:
                if grid[i + 1][j] in SYMBOLS:
                    symbol_found = f"[{i + 1}, {j}]"
                    continue
            # bottom-right i + 1, j + 1
            if i < max_row and j < max_col:
                if grid[i + 1][j + 1] in SYMBOLS:
                    symbol_found = f"[{i + 1}, {j + 1}]"

        # clear between rows
        if symbol_found:
            value = int(match_)
            if symbol_found in numbers:
                numbers[symbol_found].append(value)
            else:
                numbers[symbol_found] = [value]
            symbol_found = ""
        match_ = ""

    for key, values in numbers.items():
        if len(values) < 2:
            print(f"{key}: {values} is not a gear")
        elif len(values) == 2:
            total = values[0] * values[1]
            print(f"GEAR FOUND: {key}: {values} = {total}")
            sum += total
        else:
            raise ValueError("There are too many values?")

    return sum


if __name__ == "__main__":
    FILE = "input.txt"
    main(FILE)
