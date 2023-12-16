from advent2023.read import read_file
from loguru import logger
from rich import print


def solve_1(input_list: list[str]) -> int:
    answer = 0
    parsed_file = parse_file(input_list)
    for line in parsed_file:
        curr_line = roll_line(line)
        for i, char in enumerate(reversed(curr_line)):
            if char == "O":
                answer += i + 1
    return answer


def roll_line(line: str) -> str:
    splitted = line.split("#")
    rollpart = ""
    for part in splitted:
        circles = part.count("O")
        dots = part.count(".")
        output = circles * "O" + dots * "."
        rollpart += output
    result = ""
    i = 0
    for char in line:
        if char == "#":
            result += "#"
        else:
            result += rollpart[i]
            i += 1
    return result


def north_roll(parsed_file: list[str]) -> list[str]:
    parsed_file = list(map("".join, zip(*parsed_file)))
    roll = []
    for line in parsed_file:
        roll.append(roll_line(line))
    return list(map("".join, zip(*roll)))


def south_roll(parsed_file: list[str]) -> list[str]:
    parsed_file = list(map("".join, zip(*parsed_file)))
    roll = []
    for line in parsed_file:
        roll.append(roll_line(line[::-1])[::-1])
    return list(map("".join, zip(*roll)))


def west_roll(parsed_file: list[str]) -> list[str]:
    roll = []
    for line in parsed_file:
        roll.append(roll_line(line))
    return roll


def east_roll(parsed_file: list[str]) -> list[str]:
    roll = []
    for line in parsed_file:
        roll.append(roll_line(line[::-1])[::-1])

    return roll


def pproll(parsed_file: list[str]) -> list[str]:
    for line in parsed_file:
        print(line)
    print("\n")


def solve_2(input_list: list[str]) -> int:
    answer = 0
    prev_rolls = [input_list]
    cycle = 0
    rolls = 122
    for no in range(rolls):
        # print(no)
        roll = north_roll(prev_rolls[-1])
        roll = west_roll(roll)
        roll = south_roll(roll)
        roll = east_roll(roll)
        # pproll(roll)
        if roll in prev_rolls:
            duplicate = roll
        prev_rolls.append(roll)
    print(cycle)
    indexes = find_occurrences(prev_rolls, duplicate)
    print(indexes)
    roll = list(map("".join, zip(*roll)))
    offset = (1_000_000_000 - 115) % 7
    last_roll = prev_rolls[prev_rolls.index(duplicate) + offset]
    for line in list(map("".join, zip(*last_roll))):
        for i, char in enumerate(reversed(line)):
            if char == "O":
                answer += i + 1
    return answer


def find_occurrences(lst, roll):
    occurrences = [i for i, x in enumerate(lst) if x == roll]
    return occurrences[:10]


def parse_file(file: list[str]) -> list[str]:
    return list(map("".join, zip(*file)))


if __name__ == "__main__":
    file = read_file("files/14")
    logger.info(solve_1(file))
    logger.info(solve_2(file))
