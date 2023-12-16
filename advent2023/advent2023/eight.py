from advent2023.read import read_file
from loguru import logger


def solve_1(input_list: list[str]) -> int:
    answer = 0
    dirs, nodes = parse_file(input_list)
    key = "AAA"
    target = "ZZZ"
    while True:
        for direction in dirs:
            answer += 1
            if direction == "L":
                key = nodes[key]["L"]
            elif direction == "R":
                key = nodes[key]["R"]
            if key == target:
                return answer


def solve_2(input_list: list[str]) -> int:
    answer = 0
    dirs, nodes = parse_file(input_list)
    keys = [key for key in nodes.keys() if key.endswith("A")]
    print(len(keys))
    targets = [key for key in nodes.keys() if key.endswith("Z")]
    print(len(targets))
    print(len(dirs))
    to_decide = [len(dirs)]
    for key in keys:
        answer = 0
        while True:
            for direction in dirs:
                answer += 1
                if direction == "L":
                    key = nodes[key]["L"]
                elif direction == "R":
                    key = nodes[key]["R"]
                if key in targets:
                    to_decide.append(answer)
                    break
            else:
                continue
            break

    from math import lcm

    print(to_decide)
    result = lcm(*to_decide)
    print(result)


def parse_file(input_list: list[str]) -> list[list[str]]:
    dirs = input_list[0]
    nodes = {}
    for line in input_list[2:]:
        sanitized = (
            line.replace("=", "").replace("(", "").replace(")", "").replace(",", " ")
        )
        nodes[sanitized.split()[0]] = {
            "L": sanitized.split()[1],
            "R": sanitized.split()[2],
        }
    return dirs, nodes


if __name__ == "__main__":
    file = read_file("files/8")
    # file = read_file("tests/test_inputs/input_8_2")
    # logger.info(solve_1(file))
    logger.info(solve_2(file))
