from advent2023.read import read_file
from loguru import logger


def solve_1(input_list: list[str]) -> int:
    answer = 0
    patterns = parse_file(input_list)
    for pattern in patterns:
        answer += find_reflections(pattern)
    return answer


def find_reflections(pattern: list[str]) -> int:
    rows = len(pattern)
    transposed = list(map("".join, zip(*pattern)))
    trows = len(transposed)
    answer = 0
    for i, row in enumerate(pattern):
        try:
            for j in range(rows):
                if j > i:
                    answer += (i + 1) * 100
                    break
                if pattern[i - j] != pattern[i + j + 1] or j > i:
                    break
        except IndexError:
            if i != len(pattern) - 1:
                answer += (i + 1) * 100
    for i, row in enumerate(transposed):
        try:
            for j in range(trows):
                if j > i:
                    answer += i + 1
                    break
                if transposed[i - j] != transposed[i + j + 1]:
                    break
        except IndexError:
            if i != len(transposed) - 1:
                answer += i + 1
    print(answer)
    return answer


def find_reflections_2(pattern: list[str]) -> int:
    rows = len(pattern)
    transposed = list(map("".join, zip(*pattern)))
    trows = len(transposed)
    answer = 0
    for i, row in enumerate(pattern):
        differences = 0
        try:
            for j in range(rows):
                if j > i:
                    if differences == 1:
                        answer += (i + 1) * 100
                    break
                differences += no_of_diff(pattern[i - j], pattern[i + j + 1])
                if differences > 1:
                    break
        except IndexError:
            if i != len(pattern) - 1 and differences == 1:
                answer += (i + 1) * 100
    for i, row in enumerate(transposed):
        differences = 0
        try:
            for j in range(trows):
                if j > i:
                    if differences == 1:
                        answer += i + 1
                    break
                differences += no_of_diff(transposed[i - j], transposed[i + j + 1])
                if differences > 1:
                    break
        except IndexError:
            if i != len(transposed) - 1 and differences == 1:
                answer += i + 1
    print(answer)
    return answer


def no_of_diff(first: str, second: str) -> int:
    answer = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            answer += 1
    return answer


def solve_2(input_list: list[str]) -> int:
    answer = 0
    patterns = parse_file(input_list)
    for pattern in patterns:
        answer += find_reflections_2(pattern)
    return answer


def parse_file(file: list[str]) -> list[str]:
    patterns = []
    pattern = []
    for line in file:
        if line:
            pattern.append(line)
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)
    return patterns


if __name__ == "__main__":
    file = read_file("files/13")
    # logger.info(solve_1(file))
    logger.info(solve_2(file))
