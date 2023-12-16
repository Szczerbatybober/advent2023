from advent2023.fifth import subtract_ranges


def test_subtract():
    range_1 = range(74, 88)
    overlaps = [range(74, 77), range(77, 88)]
    assert subtract_ranges(range_1, overlaps) == []
    assert len(range_1) - len(overlaps[0]) - len(overlaps[1]) == 0


def test_subtract():
    range_1 = range(74, 88)
    overlaps = [range(77, 88), range(74, 77)]
    assert subtract_ranges(range_1, overlaps) == []
    assert len(range_1) - len(overlaps[0]) - len(overlaps[1]) == 0


def test_subtract_1():
    range_1 = range(0, 10)
    overlaps = [range(2, 8)]
    assert subtract_ranges(range_1, overlaps) == [range(0, 2), range(8, 10)]


def test_subtract_2():
    range_1 = range(0, 10)
    overlaps = [range(2, 3), range(6, 8)]
    expected = [
        range(0, 2),
        range(3, 6),
        range(8, 10),
    ]
    assert subtract_ranges(range_1, overlaps) == expected
    assert len(range_1) - len(overlaps[0]) - len(overlaps[1]) == len(expected[0]) + len(
        expected[1]
    ) + len(expected[2])


def test_subtract_3():
    range_1 = range(0, 10)
    overlaps = [range(2, 3), range(6, 10)]
    expected = [
        range(0, 2),
        range(3, 6),
    ]
    assert subtract_ranges(range_1, overlaps) == expected
    assert len(range_1) - len(overlaps[0]) - len(overlaps[1]) == len(expected[0]) + len(
        expected[1]
    )
