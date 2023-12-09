def main() -> None:
    lines = read_lines("input.txt")

    histories = [[int(n) for n in row] for row in [line.split(" ") for line in lines]]

    total = 0
    for history in histories:
        predicted_value = calculate_prediction(history)
        total += predicted_value

    print(total)


def calculate_prediction(history: list[int]) -> int:
    totals = [history[-1]]
    differences = history
    while not all([n == 0 for n in differences]):
        difference = []
        for i, n in enumerate(differences):
            if (i + 1) < len(differences):
                difference.append(differences[i + 1] - n)
        totals.append(difference[-1])
        differences = difference
    return sum(totals)


def read_lines(filename) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
