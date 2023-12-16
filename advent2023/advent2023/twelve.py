import re
from advent2023.read import read_file
from loguru import logger
from functools import lru_cache


def solve_1(input_list: list[str]) -> int:
    parsed = parse_file(input_list)
    answer = 0
    for line in parsed:
        answer += solve_line(line)
    return answer


def solve_line(line: list[str]) -> int:
    answer = 0
    no_of_questions = line[0].count("?")
    for combination in range(2**no_of_questions):
        chars = (
            bin(combination)[2:]
            .zfill(no_of_questions)
            .replace("0", ".")
            .replace("1", "#")
        )
        current = 0
        new_line = ""
        for char in line[0]:
            if char == "?":
                new_line += chars[current]
                current += 1
            else:
                new_line += char
        answer = answer + 1 if check_answer(new_line, line[1]) else answer
    return answer


def check_answer(line: list[str], placements) -> bool:
    output_string = re.sub(r"\.{2,}", ".", line)
    output = tuple(len(el) for el in output_string.split(".") if el != "")
    return output == placements


def solve_2(input_list: list[str]) -> int:
    parsed = parse_file_2(input_list)
    answer = 0
    for line in parsed:
        part = result(line[0], line[1])
        print(part, line[0], line[1])
        answer += part
    return answer


@lru_cache(maxsize=None)
def result(line, groups) -> int:
    unmod_result = 0
    mod_result = 0
    res = 0
    new_lines = []
    new_groups = []
    if len(groups) == 0 and "#" not in line:
        res += 1
    elif sum(groups) < line.count("#"):
        pass
    elif sum(groups) + len(groups) - 1 > len(line):
        pass
    elif len(line) == 0:
        pass
    elif line[0] == "?":
        new_lines.append(line[1:])
        new_groups.append(groups)

        new_lines.append("#" + line[1:])
        new_groups.append(groups)

    elif line[: groups[0]] == "#" * groups[0]:
        if len(line) != sum(groups):
            if line[groups[0]] == "#":
                pass
            else:
                new_lines.append(line[groups[0] + 1 :])
                new_groups.append(groups[1:])
        else:
            new_lines.append(line[groups[0] :])
            new_groups.append(groups[1:])
    elif line[0] == "#":
        first_question = line.find("?")
        if first_question != -1:
            new_lines.append(line[:first_question] + "#" + line[first_question + 1 :])
            line = line[:first_question] + "#" + line[first_question + 1 :]
            new_groups.append(groups)
    elif line[0] == ".":
        new_lines.append(line[1:])
        new_groups.append(groups)
    for new_line, new_group in zip(new_lines, new_groups):
        res += result(new_line, new_group)
    return res


def trim_line(line: str) -> str:
    while True and line[1]:
        longest = max(line[1])
        no = line[1].count(longest)
        searched = "#" * longest
        found = line[0].count(searched)
        if found == no:
            line = [
                line[0].replace(searched, "."),
                [el for el in line[1] if el != longest],
            ]
        else:
            break
    splitted = re.sub(r"\.{2,}", ".", line[0]).replace(".", " ").strip().split()
    if len(splitted[0]) < line[1][0]:
        splitted = splitted[1:]
        line[1] = line[1][1:]
    if len(splitted[-1]) < line[1][-1]:
        splitted = splitted[:-1]
        line[1] = line[1][:-1]
    line = [".".join(splitted), line[1]]
    # min_len = sum(line[1]) + len(line[1]) - 1
    # print("Min len:", min_len, len(line[0]))
    return line


def parse_file_2(file: list[str]) -> list[str]:
    results = []
    for line in file:
        spring = list_to_5(line)
        placement = groups_to_5(line)
        results.append([spring, placement])
    return results


def list_to_5(line: list[str]) -> list[str]:
    new_line = (line.split()[0] + "?") * 5
    return new_line[:-1]


def groups_to_5(line: list[str]) -> list[str]:
    return tuple(int(el) for el in line.split()[1].split(",")) * 5


def parse_file(file: list[str]) -> list[str]:
    results = []
    for line in file:
        spring = line.split()[0]
        placement = [int(el) for el in line.split()[1].split(",")]
        results.append([spring, placement])
    return results


if __name__ == "__main__":
    file = read_file("files/12")
    # logger.info(solve_1(file))
    logger.info(solve_2(file))
