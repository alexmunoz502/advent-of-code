from functools import lru_cache, cmp_to_key

CARDS = "J23456789TQKA"
Strength = 1 | 2 | 3 | 4 | 5 | 7


def main() -> None:
    lines = read_lines("sample.txt")

    hands = []
    for line in lines:
        hand, bid = line.split(" ")
        strength = calculate_strength(hand)
        hands.append({"hand": hand, "bid": int(bid), "strength": strength})

    hands_sorted = sorted(hands, key=cmp_to_key(compare))

    total = 0
    for i, hand in enumerate(hands_sorted, 1):
        total += hand["bid"] * i

    print(total)


def calculate_strength(hand: str) -> int:
    cards = {}
    for char in hand:
        if char in cards:
            cards[char] += 1
        else:
            cards[char] = 1

    if "J" in cards:
        highest_card = None
        for card, count in cards.items():
            if card == "J":
                continue
            if highest_card is None:
                highest_card = card
            elif cards[highest_card] < count:
                highest_card = card
        if highest_card:
            cards[highest_card] += cards["J"]
            del cards["J"]

    hand_value = sorted(cards.values())
    # 7 : Five of a kind - 5
    if hand_value == [5]:
        return 7
    # 6 : Four of a kind - 4 1
    if hand_value == [1, 4]:
        return 6
    # 5 : Full House - 3 2
    if hand_value == [2, 3]:
        return 5
    # 4 : Three of a Kind - 3 1 1
    if hand_value == [1, 1, 3]:
        return 4
    # 3 : Two Pair - 2 2 1
    if hand_value == [1, 2, 2]:
        return 3
    # 2 : One Pair - 2 1 1 1
    if hand_value == [1, 1, 1, 2]:
        return 2
    # 1 : High Card - 1 1 1 1 1
    return 1


def compare(hand_1: dict, hand_2: dict) -> int:
    if hand_1["strength"] < hand_2["strength"]:
        return -1
    if hand_2["strength"] < hand_1["strength"]:
        return 1

    if hand_1 == hand_2:
        return 0

    for i, card_1 in enumerate(hand_1["hand"]):
        card_2 = hand_2["hand"][i]
        value_1 = get_card_value(card_1)
        value_2 = get_card_value(card_2)
        if value_1 > value_2:
            return 1
        elif value_1 < value_2:
            return -1


@lru_cache
def get_card_value(card: str) -> int:
    return CARDS.find(card) + 1


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
