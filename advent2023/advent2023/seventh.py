import dataclasses
from advent2023.read import read_file
from loguru import logger

card_val = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    # "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def solve_task1_1(input_list: list[str]) -> int:
    hands = []
    for line in input_list:
        hands.append(check_hand(line))
    hands.sort(key=lambda x: x.value)
    print(hands)
    answer = 0
    for i, hands in enumerate(hands):
        answer += hands.bet * (i + 1)
        print(answer)
    return answer


def solve_task1_2(input_list: list[str]) -> int:
    hands = []
    for line in input_list:
        hands.append(check_hand(line, part_two=True))
    hands.sort(key=lambda x: x.value)
    for hand in hands:
        print(hand)
    answer = 0
    for i, hands in enumerate(hands):
        answer += hands.bet * (i + 1)
    return answer


@dataclasses.dataclass
class Hand:
    value: int
    bet: int
    cards: dict
    cards_str: str = ""


def check_hand(line: str, part_two: bool = False) -> int:
    bet = int(line.split()[1])
    value = 0
    cards = {}
    for i, card in enumerate(line.split()[0]):
        cards[card] = cards.get(card, 0) + 1 if card in cards else 1
        value += 10 ** (10 - i * 2) * card_val[card]
    hand_rank = 0
    if part_two:
        num_of_Js = cards.get("J", 0)
        if "J" in cards:
            del cards["J"]
        for i in range(num_of_Js):
            try:
                max_key = max(cards, key=cards.get)
            except ValueError:
                max_key = "A"
                cards["A"] = 0
            cards[max_key] += 1
    if part_two:
        # breakpoint()
        pass
    if len(cards) == 1:
        hand_rank = 7
    elif len(cards) == 2:
        for key in cards:
            if cards[key] == 4:
                hand_rank = 6
                break
            elif cards[key] == 3:
                hand_rank = 5
                break
    elif len(cards) == 3:
        for key in cards:
            if cards[key] == 3:
                hand_rank = 3
                break
            elif cards[key] == 2:
                hand_rank = 2
                break
    elif len(cards) == 4:
        hand_rank = 1
    else:
        hand_rank = 0
    value += 10**12 * hand_rank
    return Hand(value=value, bet=bet, cards=cards, cards_str=line.split()[0])


if __name__ == "__main__":
    file = read_file("files/7")
    # file = read_file("tests/test_inputs/input_7_1")
    logger.info(solve_task1_1(file))
    logger.info(solve_task1_2(file))
