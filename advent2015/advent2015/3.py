from pathlib import Path


def solve_1():
    path = Path("files/3")
    with path.open() as file:
        visited = [(0, 0)]
        for line in file.readlines():
            current = [0, 0]
            for char in line:
                if char == ">":
                    current[1] += 1
                elif char == "<":
                    current[1] -= 1
                elif char == "^":
                    current[0] += 1
                elif char == "v":
                    current[0] -= 1
                # print(char, current)
                visited.append(tuple(current))
                # print(visited)
        print(len(set(visited)))


def solve_2():
    path = Path("files/3")
    with path.open() as file:
        visited = [(0, 0), (0, 0)]
        for line in file.readlines():
            current = [0, 0]
            currentr = [0, 0]
            for i, char in enumerate(line):
                if i % 2 == 0:
                    if char == ">":
                        current[1] += 1
                    elif char == "<":
                        current[1] -= 1
                    elif char == "^":
                        current[0] += 1
                    elif char == "v":
                        current[0] -= 1
                    visited.append(tuple(current))
                else:
                    if char == ">":
                        currentr[1] += 1
                    elif char == "<":
                        currentr[1] -= 1
                    elif char == "^":
                        currentr[0] += 1
                    elif char == "v":
                        currentr[0] -= 1
                    # print(char, current)
                    visited.append(tuple(currentr))
                # print(visited)
        print(len(set(visited)))


if __name__ == "__main__":
    solve_1()
    solve_2()
