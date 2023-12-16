from advent2023.read import read_file
from advent2023.seventh import check_hand


def test_len():
    lines = read_file("files/7")
    for line in lines:
        lenght = 0
        for key, val in check_hand(line).cards.items():
            lenght += val
        assert lenght == 5
