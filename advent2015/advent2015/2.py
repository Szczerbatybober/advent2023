from pathlib import Path


def solve_1():
    path = Path("files/2")
    with path.open() as file:
        summ = 0
        for line in file.readlines():
            dim = [int(num) for num in line.split("x")]
            paper = (
                2 * dim[0] * dim[1]
                + 2 * dim[1] * dim[2]
                + 2 * dim[0] * dim[2]
                + min(dim[0] * dim[1], dim[1] * dim[2], dim[0] * dim[2])
            )
            summ += paper
        print(summ)


def solve_2():
    path = Path("files/2")
    with path.open() as file:
        summ = 0
        for line in file.readlines():
            dim = [int(num) for num in line.split("x")]
            ribbon = (
                dim[0] * dim[1] * dim[2]
                + 2 * dim[0]
                + 2 * dim[1]
                + 2 * dim[2]
                - 2 * max(dim)
            )
            print(dim, ribbon)
            summ += ribbon
        print(summ)


if __name__ == "__main__":
    solve_1()
    solve_2()
