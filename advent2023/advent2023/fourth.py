from dataclasses import dataclass
import re
from advent2023.read import read_file
from loguru import logger


@dataclass
class Card:
    number: int
    winning_numbers: list[int]
    your_numbers: list[int]


def parse_cards(input_list: list[str]):
    cards = []
    for line in input_list:
        output_string = re.sub(r"\s+", " ", line)
        first_part, your_part = output_string.split("|")
        card_no, winning_part = first_part.split(":")
        card_number = card_no.split(" ")[1].strip()
        winning_numbers = winning_part.strip().split(" ")
        your_numbers = your_part.strip().split(" ")
        cards.append(Card(int(card_number), winning_numbers, your_numbers))
    return cards


def solve_task1_1(input_list: list[str]) -> int:
    result = 0
    cards = parse_cards(input_list)
    for card in cards:
        no = 0
        for winning_number in card.winning_numbers:
            if winning_number in card.your_numbers:
                no += 1
        if no > 0:
            result += 2 ** (no - 1)
    return result


def solve_task1_2(input_list: list[str]) -> int:
    result = 0
    cards = parse_cards(input_list)
    original_cards = cards.copy()
    new_cards = cards
    while True:
        result += len(new_cards)
        cards = new_cards.copy()
        new_cards = []
        if len(cards) == 0:
            break
        for card in cards:
            no = 0
            for winning_number in card.winning_numbers:
                if winning_number in card.your_numbers:
                    no += 1
            if no > 0:
                for i in range(0, no):
                    try:
                        new_cards.append(original_cards[card.number + i])
                    except IndexError:
                        pass
    return result


if __name__ == "__main__":
    # file = read_file("files/4")
    file = read_file("files/4")
    logger.info(solve_task1_1(file))
    logger.info(solve_task1_2(file))
