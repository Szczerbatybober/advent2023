from dataclasses import dataclass
from advent2023.read import read_file
from loguru import logger
from functools import lru_cache


@dataclass(frozen=True)
class Field:
    y: int
    x: int
    direction: (0, 1)


@lru_cache(maxsize=None)
def solve_field(field: Field, input_list: list[str]) -> tuple[int]:
    char = input_list[field.y][field.x]
    to_return = []
    if char == "\\":
        to_return.append(
            Field(
                field.y + field.direction[1],
                field.x + field.direction[0],
                (field.direction[1], field.direction[0]),
            )
        )
    elif char == "/":
        to_return.append(
            Field(
                field.y - field.direction[1],
                field.x - field.direction[0],
                (-field.direction[1], -field.direction[0]),
            )
        )
    elif char == ".":
        to_return.append(
            Field(
                field.y + field.direction[0],
                field.x + field.direction[1],
                field.direction,
            )
        )
    elif char == "|":
        if field.direction[0] != 0:
            to_return.append(
                Field(
                    field.y + field.direction[0],
                    field.x + field.direction[1],
                    field.direction,
                )
            )
        else:
            to_return.extend(
                [
                    Field(field.y + 1, field.x, (1, 0)),
                    Field(field.y - 1, field.x, (-1, 0)),
                ]
            )
    elif char == "-":
        if field.direction[1] != 0:
            to_return.append(
                Field(
                    field.y + field.direction[0],
                    field.x + field.direction[1],
                    field.direction,
                )
            )
        else:
            to_return.extend(
                [
                    Field(field.y, field.x - 1, (0, -1)),
                    Field(field.y, field.x + 1, (0, 1)),
                ]
            )
    return [
        el
        for el in to_return
        if el.x >= 0
        and el.y >= 0
        and el.x < len(input_list[0])
        and el.y < len(input_list)
    ]


def pprint(lightened: str, input_list: list[str]) -> None:
    for y in range(len(input_list)):
        for x in range(len(input_list[0])):
            if (y, x) in lightened:
                print("#", end="")
            else:
                print(input_list[y][x], end="")
        print("")


def solve_1(input_list: list[str]) -> int:
    lightened = []
    current = [Field(0, 0, (0, 1))]
    i = 1200
    j = 0
    while len(current) > 0 and j < i:
        j += 1
        old_current = current.copy()
        current = []
        for field in old_current:
            lightened.append((field.y, field.x))
            current.extend(solve_field(field, input_list))
        print(len(set(lightened)), j)
    return len(set(lightened))


def solve_2(input_list: list[str]) -> int:
    attempts = (
        [Field(0, x, (1, 0)) for x in range(len(input_list[0]))]
        + [Field(y, 0, (0, 1)) for y in range(len(input_list))]
        + [Field(len(input_list) - 1, x, (-1, 0)) for x in range(len(input_list[0]))]
        + [Field(y, len(input_list[0]) - 1, (0, -1)) for y in range(len(input_list))]
    )
    attempts = [[attempt] for attempt in attempts]
    results = []
    for current in attempts:
        results.append(solve_attempt(current, input_list))
    return max(results)


def solve_attempt(
    current,
    input_list,
    maximum: int = 0,
) -> int:
    lightened = set()
    i = 900
    j = 0
    while len(current) > 0 and j < i:
        j += 1
        old_current = current.copy()
        current = set()
        for field in set(old_current):
            lightened.add((field.y, field.x))
            for element in solve_field(field, input_list):
                current.add(element)
        if j % 100 == 0:
            print(j, len(lightened))
    if len(set(lightened)) > maximum:
        maximum = len(set(lightened))
    return maximum


def parse_file(file: list[str]) -> list[str]:
    pass


if __name__ == "__main__":
    file = read_file("files/16")
    # logger.info(solve_1(file))
    logger.info(solve_2(file))
