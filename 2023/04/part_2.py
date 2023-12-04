from collections import namedtuple
from dataclasses import dataclass


Score = namedtuple("Score", ["value", "matches"])
Memo = namedtuple("Memo", ["count", "cards"])


@dataclass
class Card:
    id_: int
    winning_numbers: list[str]
    numbers: list[str]


def main() -> None:
    lines = read_lines("input.txt")
    cards = parse_cards(lines)
    n_cards = len(cards)

    memo = {}

    for card in cards[::-1]:
        value, matches = score_card(card)
        n_links = 0
        for match_ in range(matches):
            next_id = card.id_ + match_ + 1
            if next_id > len(cards):
                break
            n_links += 1 + memo[next_id]
        memo[card.id_] = n_links
        n_cards += n_links

    print(n_cards)


def parse_cards(lines: list[str]) -> list[Card]:
    raw_cards = [line.split(":")[1].split("|") for line in lines]
    cards = []
    for i, raw_card in enumerate(raw_cards):
        winning_numbers = raw_card[0].replace("  ", " ").strip().split(" ")
        numbers = raw_card[1].replace("  ", " ").strip().split(" ")
        cards.append(Card(i, winning_numbers, numbers))
    return cards


def score_card(card: Card) -> Score:
    value = 0
    matches = 0
    for number in card.numbers:
        if number in card.winning_numbers:
            matches += 1
            if value == 0:
                value = 1
            else:
                value += value
    return Score(value, matches)


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
