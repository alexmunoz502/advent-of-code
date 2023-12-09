def main() -> None:
    lines = read_lines("input.txt")

    histories = [[int(n) for n in row] for row in [line.split(" ") for line in lines]]

    total = 0
    for history in histories:
        predicted_value = calculate_prediction(history)
        total += predicted_value

    print(total)


def calculate_prediction(history: list[int]) -> int:
    totals = [history[0]]
    differences = history
    while not all([n == 0 for n in differences]):
        difference = []
        for i, n in enumerate(differences):
            if (i + 1) < len(differences):
                difference.append(differences[i + 1] - n)
        totals.append(difference[0])
        differences = difference

    return reduce_totals(totals)


def reduce_totals(totals: list[int]) -> int:
    i = len(totals) - 2
    value = totals[-1]
    while i >= 0:
        n = totals[i]
        value = n - value
        i -= 1
    return value


def read_lines(filename) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
