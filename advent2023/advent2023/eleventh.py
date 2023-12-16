from dataclasses import dataclass
from advent2023.read import read_file
from loguru import logger

# from rich import print


def solve_1(input_list: list[str]) -> int:
    answer = 0
    file = fix_file(input_list)
    galaxies = locage_galaxies(file)
    for i, galaxy in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            distance = abs(galaxy.x - galaxies[j].x) + abs(galaxy.y - galaxies[j].y)
            print(i, galaxy, j, galaxies[j], distance, sep=", ")
            answer += distance
    return answer


def fix_file(file: list[str]) -> list[str]:
    new_file = []
    for line in file:
        if line.find("#") == -1:
            new_file.append(line)
            new_file.append(line)
        else:
            new_file.append(line)
    for line in new_file:
        print(line)
    transposed = list(map("".join, zip(*new_file)))
    for line in transposed:
        print(line)
    newer_file = []
    for line in transposed:
        if line.find("#") == -1:
            newer_file.append(line)
            newer_file.append(line)
        else:
            newer_file.append(line)
    return list(map(list, zip(*newer_file)))


def rows(file: list[str], x_start, x_stop) -> list[str]:
    result = 0
    for line in file[min(x_start, x_stop) : (max(x_stop, x_start))]:
        if line.find("#") == -1:
            result += 1
        else:
            pass
    return result


def columns(file: list[str], x_start, x_stop) -> list[str]:
    transposed = list(map("".join, zip(*file)))
    result = 0
    for line in transposed[min(x_start, x_stop) : (max(x_stop, x_start))]:
        if line.find("#") == -1:
            result += 1
        else:
            pass
    return result


@dataclass
class Galaxy:
    y: int
    x: int


def locage_galaxies(file: list[str]) -> list[Galaxy]:
    galaxies = []
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append(Galaxy(y, x))
    return galaxies


def solve_2(input_list: list[str]) -> int:
    expand = 999999
    answer = 0
    galaxies = locage_galaxies(file)
    for i, galaxy in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            distance = (
                abs(galaxy.x - galaxies[j].x)
                + abs(galaxy.y - galaxies[j].y)
                + rows(file, galaxy.y, galaxies[j].y) * expand
                + columns(file, galaxy.x, galaxies[j].x) * expand
            )
            print(
                i,
                galaxy,
                j,
                galaxies[j],
                distance,
                rows(file, galaxy.y, galaxies[j].y) * expand,
                columns(file, galaxy.x, galaxies[j].x) * expand,
                sep=", ",
            )
            answer += distance
    return answer


if __name__ == "__main__":
    file = read_file("files/11")
    # file = read_file("tests/test_inputs/11")
    logger.info(solve_1(file))
    logger.info(solve_2(file))
