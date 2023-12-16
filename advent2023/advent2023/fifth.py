from dataclasses import dataclass
from advent2023.read import read_file
from loguru import logger


def parse_file(lines: list[str]) -> (list[int], dict[str, list[dict]]):
    map_of_maps = {}
    seeds = []
    for line in lines:
        if line.startswith("seeds: "):
            seeds = [int(seed) for seed in line.split()[1:]]
        elif line.endswith("map:"):
            key = line.split(" ")[0]
            map_of_maps[key] = []
        elif len(line.split()) == 3:
            map_of_maps[key].append(
                {
                    "destination": int(line.split()[0]),
                    "source": int(line.split()[1]),
                    "lenght": int(line.split()[2]),
                    "difference": int(line.split()[0]) - int(line.split()[1]),
                }
            )
    return seeds, map_of_maps


def parse_file_2(lines: list[str]) -> (list[int], dict[str, list[dict]]):
    map_of_maps = {}
    seeds = []
    for line in lines:
        if line.startswith("seeds: "):
            seeds = [int(seed) for seed in line.split()[1:]]
            actual_seeds = []
            for i, seed in enumerate(seeds):
                if i % 2 == 0:
                    actual_seeds.append(range(seed, seed + seeds[i + 1]))
        elif line.endswith("map:"):
            key = line.split(" ")[0]
            map_of_maps[key] = []
        elif len(line.split()) == 3:
            map_of_maps[key].append(
                {
                    "destination": int(line.split()[0]),
                    "source": int(line.split()[1]),
                    "lenght": int(line.split()[2]),
                    "difference": int(line.split()[0]) - int(line.split()[1]),
                    "range": range(
                        int(line.split()[1]),
                        int(line.split()[1]) + int(line.split()[2]),
                    ),
                }
            )
    return (
        actual_seeds,
        map_of_maps,
    )


def solve_task1_1(input_list: list[str]) -> int:
    answer = 0
    seeds, map_of_maps = parse_file(input_list)
    seeds_map = {seed: [seed] for seed in seeds}
    for seed in seeds:
        for key, ranges in map_of_maps.items():
            for map_range in ranges:
                if (
                    seeds_map[seed][-1] >= map_range["source"]
                    and seeds_map[seed][-1] <= map_range["source"] + map_range["lenght"]
                ):
                    seeds_map[seed].append(
                        seeds_map[seed][-1] + map_range["difference"]
                    )
                    break
            else:
                seeds_map[seed].append(seeds_map[seed][-1])
    locations = []
    print(seeds_map)
    for seed, values in seeds_map.items():
        locations.append(values[-1])
    return min(locations)


def translate_ranges(input: list[range], maps: list[dict], key: str) -> list[range]:
    result = []
    for input_range in input:
        overlaps = []
        for map_map in maps:
            overlap = range(
                max(input_range[0], map_map["range"][0]),
                min(input_range[-1], map_map["range"][-1]) + 1,
            )
            if len(overlap) > 0:
                translated = range(
                    overlap[0] + map_map["difference"],
                    overlap[-1] + map_map["difference"] + 1,
                )
                result.append(translated)
            if len(overlap) > 0:
                overlaps.append(overlap)
        result.extend(subtract_ranges(input_range, overlaps))
    return result


def subtract_ranges(main_range: range, subtracting_ranges: list[range]) -> list[range]:
    result = []

    current_start = main_range[0]
    subtracting_ranges = sorted(subtracting_ranges, key=lambda x: x.start)
    for subtracting_range in subtracting_ranges:
        if subtracting_range.start > current_start:
            result.append(range(current_start, subtracting_range.start))

        current_start = max(current_start, subtracting_range.stop)

    if current_start < main_range.stop:
        result.append(range(current_start, main_range.stop))

    return result


def solve_task5_2(input_list: list[str]) -> int:
    ranges, map_of_maps = parse_file_2(input_list)
    for key in [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]:
        ranges = translate_ranges(ranges, map_of_maps[key], key)
        print(ranges, key)
        print(sum([len(_range) for _range in ranges]))

    # print(location_ranges)
    return int(min(loc_range[0] for loc_range in ranges))


if __name__ == "__main__":
    file = read_file("files/5")
    file = read_file("tests/test_inputs/input_5_1")
    logger.info(solve_task5_2(file))
    file = read_file("files/5")
    logger.info(solve_task5_2(file))
    # logger.info(solve_task1_1(file))
    # logger.info(solve_task5_2_2(file))
