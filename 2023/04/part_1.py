def main() -> None:
    total = 0

    lines = read_lines("input.txt")

    raw_cards = [line.split(":")[1].split("|") for line in lines]
    cards = []
    for raw_card in raw_cards:
        winning_numbers = raw_card[0].replace("  ", " ").strip().split(" ")
        numbers = raw_card[1].replace("  ", " ").strip().split(" ")
        cards.append([winning_numbers, numbers])

    print(cards)

    for card in cards:
        value = 0
        winning_numbers = card[0]
        numbers = card[1]
        for number in numbers:
            if number in winning_numbers:
                if value == 0:
                    value = 1
                else:
                    value += value
        total += value

    print(total)


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
