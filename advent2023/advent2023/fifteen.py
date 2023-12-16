from collections import defaultdict
from dataclasses import dataclass
from advent2023.read import read_file
from loguru import logger


def solve_1(input_list: list[str]) -> int:
    answer = 0
    for val in parse_file(input_list):
        answer += hash_word(val)
    return answer


def hash_char(char: str, num: int) -> str:
    ascii = ord(char) + num
    return (ascii * 17) % 256


def hash_word(word: str) -> int:
    val = 0
    for char in word:
        val = hash_char(char, val)
    return val


def solve_2(input_list: list[str]) -> int:
    lenses = parse_file_2(input_list)
    boxes = {}
    for lens in lenses:
        if lens.operation == "-":
            try:
                for element in boxes[lens.hash_label]:
                    if lens.label in element:
                        boxes[lens.hash_label].remove(element)
            except (ValueError, KeyError):
                pass
        else:
            # if "gnhn" in lens.label and lens.focal == 5:
            #     breakpoint()
            try:
                if len(boxes[lens.hash_label]) == 0:
                    boxes[lens.hash_label].append(f"{lens.label} {lens.focal}")
                else:
                    for element in boxes[lens.hash_label]:
                        found = False
                        if lens.label in element:
                            index = boxes[lens.hash_label].index(element)
                            boxes[lens.hash_label].pop(index)
                            boxes[lens.hash_label].insert(
                                index, f"{lens.label} {lens.focal}"
                            )
                            found = True
                            break
                    if not found:
                        boxes[lens.hash_label].append(f"{lens.label} {lens.focal}")
            except KeyError:
                boxes[lens.hash_label] = [f"{lens.label} {lens.focal}"]
        # print(boxes, lens)
        # breakpoint()
    answer = 0
    print(boxes)
    for key, box in boxes.items():
        box_power = 0
        for j, element in enumerate(box):
            lens = int(element.split(" ")[1])
            box_power += (key + 1) * (j + 1) * lens
        answer += box_power
    return answer


def parse_file(file: list[str]) -> list[str]:
    return file[0].split(",")


@dataclass
class Lens:
    label: str
    operation: str
    focal: int

    @property
    def hash_label(
        self,
    ) -> int:
        return hash_word(self.label)


def parse_file_2(file: list[str]) -> list[str]:
    elements = file[0].split(",")
    lenses = []
    for element in elements:
        if "=" in element:
            label, box = element.split("=")
            operation = "="
            lenses.append(Lens(label, operation, int(box)))
        else:
            label = element.split("-")
            operation = "-"
            lenses.append(Lens(label[0], operation, 0))
    return lenses


if __name__ == "__main__":
    file = read_file("files/15")
    logger.info(solve_1(file))
    logger.info(solve_2(file))
