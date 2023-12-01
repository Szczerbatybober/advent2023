from time import perf_counter
from advent2023.read import read_file
from loguru import logger

digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]


def solve_task1_1(input_list: list[str]) -> int:
    answer = 0
    for line in input_list:
        answer += solve_line(line)
    return answer


def solve_task1_2(input_list: list[str]) -> int:
    answer = 0
    for line in input_list:
        answer += solve_line_2(line)
    return answer


def solve_line(line: str) -> int:
    number = [0, 0]
    for char in line:
        if char.isdigit():
            number[0] = int(char)
            break
    for char in reversed(line):
        if char.isdigit():
            number[1] = int(char)
            break
    return 10 * number[0] + number[1]


def get_first(line: str) -> int:
    min_index = len(line)
    min_len = 1
    for digit in digits:
        try:
            index = line.index(digit)
            if index < min_index:
                min_index = index
                min_len = len(str(digit))
        except ValueError:
            continue
    return number_to_int(line[min_index : min_index + min_len])


def get_last(line: str) -> int:
    reversed_line = line[::-1]
    min_index = len(line)
    min_len = 1
    for digit in digits:
        try:
            reversed_digit = digit[::-1]
            index = reversed_line.index(reversed_digit)
            if index < min_index:
                min_index = index
                min_len = len(str(reversed_digit))
        except ValueError:
            continue
    return number_to_int(reversed_line[min_index : min_index + min_len][::-1])


def solve_line_2(line: str) -> int:
    first = get_first(line)
    last = get_last(line)
    return first * 10 + last


def number_to_int(number: str) -> int:
    try:
        return int(number)
    except:
        match number:
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9


if __name__ == "__main__":
    file = read_file("files/1")
    logger.info(solve_task1_1(file))
    start_time = perf_counter()
    logger.info(solve_task1_2(file))
    logger.info(f"Time: {(perf_counter() - start_time) * 1000}")
