from advent2023.read import read_file
from loguru import logger


def solve_1(input_list: list[str]) -> int:
    lines = parse_file(input_list)
    answer = 0
    for line in lines:
        answer += solve_line_1(line)
    return answer


def solve_2(input_list: list[str]) -> int:
    lines = parse_file(input_list)
    answer = 0
    for line in lines:
        answer += solve_line_2(line)
    return answer


def solve_line_1(line: list[str]) -> int:
    differences = [line]
    new_line = []
    j = 0
    while any(val != 0 for val in differences[j]):
        for i, val in enumerate(differences[j]):
            if i > 0:
                new_line.append(val - differences[j][i - 1])
        differences.append(new_line.copy())
        new_line = []
        j += 1
    differences.reverse()
    for i, res in enumerate(differences):
        if i > 0:
            res.append(differences[i][-1] + differences[i - 1][-1])
        else:
            res.append(0)
    return differences[-1][-1]


def solve_line_2(line: list[str]) -> int:
    differences = [line]
    new_line = []
    j = 0
    while any(val != 0 for val in differences[j]):
        for i, val in enumerate(differences[j]):
            if i > 0:
                new_line.append(val - differences[j][i - 1])
        differences.append(new_line.copy())
        new_line = []
        j += 1
    differences.reverse()
    for el in differences:
        el.insert(0, 0)
    for i, res in enumerate(differences):
        if i > 0:
            res[0] = differences[i][1] - differences[i - 1][0]
        else:
            pass
    return differences[-1][0]


def parse_file(file: list[str]):
    return [list(map(int, line.split())) for line in file]


if __name__ == "__main__":
    file = read_file("files/9")
    logger.info(solve_1(file))
    logger.info(solve_2(file))
