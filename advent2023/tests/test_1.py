import pytest
from advent2023.first import (
    get_first,
    get_last,
    number_to_int,
    solve_line,
    solve_line_2,
    solve_task1_1,
    solve_task1_2,
)


def test_first():
    input = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    assert solve_task1_1(input) == 142


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ),
)
def test_line(line, expected):
    assert solve_line(line) == expected


def test_first_2():
    input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert solve_task1_2(input) == 281


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("zeightvh9", 89),
        ("nine", 99),
        ("1", 11),
        ("seventhree4seven", 77),
    ),
)
def test_line_2(line, expected):
    assert solve_line_2(line) == expected


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("two1nine", 2),
        ("eightwothree", 8),
        ("abcone2threexyz", 1),
        ("xtwone3four", 2),
        ("4nineeightseven2", 4),
        ("zoneight234", 1),
        ("7pqrstsixteen", 7),
        ("zeightvh9", 8),
        ("nine", 9),
        ("1", 1),
        ("seventhree4seven", 7),
    ),
)
def test_get_first(line, expected):
    assert get_first(line) == expected


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("two1nine", 9),
        ("eightwothree", 3),
        ("abcone2threexyz", 3),
        ("xtwone3four", 4),
        ("4nineeightseven2", 2),
        ("zoneight234", 4),
        ("7pqrstsixteen", 6),
        ("zeightvh9", 9),
        ("nine", 9),
        ("1", 1),
        ("seventhree4seven", 7),
    ),
)
def test_get_last(line, expected):
    assert get_last(line) == expected


@pytest.mark.parametrize(
    ("number", "expected"), (("one", 1), ("two", 2), (3, 3), ("nine", 9))
)
def test_number_to_int(number, expected):
    assert number_to_int(number) == expected
