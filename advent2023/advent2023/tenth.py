from advent2023.read import read_file
from loguru import logger
from rich import print


def solve_1(input_list: list[str]) -> int:
    answer = 1
    for i, line in enumerate(input_list):
        index = line.find("S")
        print(index)
        if index != -1:
            start = [i, index]
            break
    y = start[0]
    x = index - 1
    vector = "L"
    in_path = [[start], [y, x]]
    while input_list[y][x] != "S":
        if input_list[y][x] == "-" and vector == "L":
            vector = "L"
        if input_list[y][x] == "-" and vector == "R":
            vector = "R"
        elif input_list[y][x] == "|" and vector == "U":
            vector = "U"
        elif input_list[y][x] == "|" and vector == "D":
            vector = "D"
        elif input_list[y][x] == "L" and vector == "L":
            vector = "U"
        elif input_list[y][x] == "L" and vector == "D":
            vector = "R"
        elif input_list[y][x] == "J" and vector == "R":
            vector = "U"
        elif input_list[y][x] == "J" and vector == "D":
            vector = "L"
        elif input_list[y][x] == "7" and vector == "U":
            vector = "L"
        elif input_list[y][x] == "7" and vector == "R":
            vector = "D"
        elif input_list[y][x] == "F" and vector == "U":
            vector = "R"
        elif input_list[y][x] == "F" and vector == "L":
            vector = "D"
        if vector == "D":
            y += 1
        elif vector == "U":
            y -= 1
        elif vector == "L":
            x -= 1
        elif vector == "R":
            x += 1
        answer += 1
        in_path.append([y, x])
    greens = 0
    for y, line in enumerate(input_list):
        reds = 0
        for x, char in enumerate(
            line.replace("-", "━").replace("|", "┃").replace("L", "┛")
        ):
            if char == "S":
                print("[blue]" + "━" + "[/blue]", sep="", end="")
                # reds += 1
            elif [y, x] not in in_path:
                if reds % 2 == 0:
                    print("[grey]" + "." + "[/grey]", sep="", end="")
                else:
                    print("[green]" + char + "[/green]", sep="", end="")
                    greens += 1
            elif [y, x] in in_path:
                print("[red]" + char + "[/red]", sep="", end="")
                if char in [
                    "┃",
                    "┛",
                    "┗",
                ]:
                    reds += 1
        print("")
    print(greens)
    return answer / 2


def solve_2(input_list: list[str]) -> int:
    answer = 0
    return answer


if __name__ == "__main__":
    file = read_file("files/10")
    file = read_file("tests/test_inputs/10_vis")
    logger.info(solve_1(file))
    logger.info(solve_2(file))
