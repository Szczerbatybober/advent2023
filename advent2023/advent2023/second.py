from dataclasses import dataclass, field
from advent2023.read import read_file
from loguru import logger


@dataclass
class Pull:
    red: int = 0
    blue: int = 0
    green: int = 0


@dataclass
class Game:
    game_id: int
    pulls: list[Pull] = field(default_factory=list)

    @classmethod
    def from_str(cls, line: str):
        game_no = line.split(":")[0].split(" ")[1]
        game = Game(game_id=int(game_no))
        pulls = line.split(":")[1].split(";")
        for pull in pulls:
            cubes = pull.split(",")
            pull = Pull()
            for cube in cubes:
                cube_info = cube.strip().split(" ")
                if cube_info[1] == "red":
                    pull.red = int(cube_info[0])
                if cube_info[1] == "blue":
                    pull.blue = int(cube_info[0])
                if cube_info[1] == "green":
                    pull.green = int(cube_info[0])
            game.pulls.append(pull)
        return game


def parse_file(lines: list[str]):
    games = []
    for line in lines:
        game = Game.from_str(line)
        games.append(game)
    return games


def game_possible(game: Game, available_cubes: Pull) -> bool:
    for pull in game.pulls:
        if (
            pull.red > available_cubes.red
            or pull.blue > available_cubes.blue
            or pull.green > available_cubes.green
        ):
            return False
    return True


def solve_2_1(lines: list[str], available_cubes: Pull) -> int:
    games = parse_file(file)
    result = 0
    for game in games:
        if game_possible(game, available_cubes=available_cubes):
            result += game.game_id
    return result


def solve_2_2(lines: list[str]) -> int:
    games = parse_file(file)
    result = 0
    for game in games:
        red = max([pull.red for pull in game.pulls])
        green = max([pull.green for pull in game.pulls])
        blue = max([pull.blue for pull in game.pulls])
        result += red * blue * green
    return result


if __name__ == "__main__":
    file = read_file("files/2")
    logger.info(solve_2_1(file, Pull(red=12, green=13, blue=14)))
    logger.info(solve_2_2(file))
