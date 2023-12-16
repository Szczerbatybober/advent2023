from dataclasses import dataclass
from advent2023.read import read_file
from loguru import logger


@dataclass
class Race:
    time_traveled: int
    distance: int
    ways: int = 0


def solve_task1_1(input_list: list[str]) -> int:
    races = parse_file(input_list)
    for race in races:
        speed = 0
        for time in range(race.time_traveled):
            # breakpoint()
            if (race.time_traveled - time) * speed > race.distance:
                race.ways += 1
            speed += 1
    result = 1
    for race in races:
        result *= race.ways
    return result


def solve_task1_2(input_list: list[str]) -> int:
    races = parse_file_2(input_list)
    for i, race in enumerate(races):
        if i % 10_000 == 0:
            logger.info(f"i: {i}")
        speed = 0
        for time in range(race.time_traveled):
            # breakpoint()
            if (race.time_traveled - time) * speed > race.distance:
                race.ways += 1
            speed += 1
    result = 1
    for race in races:
        result *= race.ways
    return result


def parse_file(input_list: list[str]) -> list[list[str]]:
    races = []
    print(input_list[0].split())
    for i in range(1, len(input_list[0].split())):
        races.append(
            Race(
                time_traveled=int(input_list[0].split()[i]),
                distance=int(input_list[1].split()[i]),
            )
        )
    return races


def parse_file_2(input_list: list[str]) -> list[list[str]]:
    races = []
    print(input_list[0].split())
    races.append(
        Race(
            time_traveled=int(input_list[0].replace("Time:", "").replace(" ", "")),
            distance=int(input_list[1].replace("Distance:", "").replace(" ", "")),
        )
    )
    return races


if __name__ == "__main__":
    file = read_file("files/6")
    logger.info(solve_task1_1(file))
    logger.info(solve_task1_2(file))
