from advent2023.read import read_file


def test_read_file():
    assert read_file("tests/input_1_1") == [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
