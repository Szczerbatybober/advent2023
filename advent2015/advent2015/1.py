from pathlib import Path


def solve_1():
    path = Path("files/1")
    with path.open() as file:
        floor = 0
        for char in file.read():
            floor = floor + 1 if char == "(" else floor - 1
        print(floor)


def solve_2():
    path = Path("files/1")
    with path.open() as file:
        floor = 0
        for i, char in enumerate(file.read()):
            floor = floor + 1 if char == "(" else floor - 1
            if floor < 0:
                print(i + 1)
                break


if __name__ == "__main__":
    solve_1()
    solve_2()
