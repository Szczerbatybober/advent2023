from dataclasses import dataclass
from advent2023.read import read_file
from loguru import logger


@dataclass
class Number:
    value: int
    x: int
    x_end: int
    y: int


@dataclass
class Gear:
    x: int
    y: int


def get_numbers(lines: list[str]) -> list[Number]:
    numbers = []
    for row, line in enumerate(lines):
        current_number = ""
        for column, char in enumerate(line):
            if char.isdigit():
                if current_number == "":
                    x = column
                current_number += char
            else:
                if current_number:
                    numbers.append(
                        Number(
                            value=int(current_number),
                            x=x,
                            y=row,
                            x_end=x + len(current_number),
                        )
                    )
                current_number = ""
        if current_number:  # so we don't skip if number ends the line
            numbers.append(
                Number(
                    value=int(current_number),
                    x=x,
                    y=row,
                    x_end=x + len(current_number),
                )
            )
    return numbers


def get_gears(lines: list[str]) -> int:
    gears = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "*":
                gears.append(Gear(x=x, y=y))
    return gears


def find_adjacent(gear: Gear, numbers: list[Number]):
    adjacents = []
    for number in numbers:
        if number.y == gear.y:
            if number.x == gear.x + 1 or number.x_end == gear.x:
                adjacents.append(number)
        elif number.y == gear.y + 1:
            if gear.x in range(number.x - 1, number.x_end + 1):
                adjacents.append(number)
        elif number.y == gear.y - 1:
            if gear.x in range(number.x - 1, number.x_end + 1):
                adjacents.append(number)
    return adjacents


def solve_2_1(lines: list[str]) -> int:
    numbers = get_numbers(lines)
    rel_numbers = []
    for number in numbers:
        for y in range(max(number.y - 1, 0), min(number.y + 2, len(lines))):
            for x in range(
                max(number.x - 1, 0),
                min(number.x_end + 1, len(lines[0])),
            ):
                if not lines[y][x].isdigit() and lines[y][x] != ".":
                    rel_numbers.append(number)
    return sum([number.value for number in rel_numbers])


def solve_2_2(lines: list[str]) -> int:
    gears = get_gears(lines)
    numbers = get_numbers(lines)
    result = 0
    for gear in gears:
        adjacents = find_adjacent(gear, numbers)
        if len(adjacents) == 2:
            result += adjacents[0].value * adjacents[1].value
    return result


if __name__ == "__main__":
    file = read_file("files/3")
    file = read_file("files/3")
    logger.info(solve_2_1(file))
    logger.info(solve_2_2(file))
