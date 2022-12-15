"""
Module for testing main.py
"""
import pytest
from utils.algo import is_start_island, it_belongs_to_island, fill_back

@pytest.mark.parametrize(
    "pos, curr_line, prev_line, length, expected",
    [
        (1, ["0", "1", "1", "0"], ["0", "0", "0", "0"], 4, False),
        (2, ["0", "1", "1", "0"], ["0", "0", "0", "0"], 4, True),
        (2, ["0", "0", "1", "0"], ["0", "0", "0", "0"], 4, True),
        (0, ["1", "0", "1", "0"], ["0", "0", "0", "0"], 4, True),
        (1, ["1", "1", "1", "0"], ["0", "0", "0", "0"], 4, False),
        (2, ["0", "0", "1", "0"], ["0", "1", "0", "0"], 4, False),
        (2, ["0", "0", "1", "0"], ["0", "0", "1", "0"], 4, False),
        (2, ["0", "0", "1", "0"], ["0", "0", "0", "1"], 4, False),
        (2, ["0", "0", "1", "1"], ["0", "0", "0", "0"], 4, False),
    ]
)
def test_is_start_island(pos, curr_line, prev_line, length, expected):
    assert is_start_island(pos, curr_line, prev_line, length) == expected


@pytest.mark.parametrize(
    "pos, curr_line, prev_line, length, expected",
    [
        (1, ["0", "1", "1", "0"], ["0", "7", "0", "0"], 4, "7"),
        (2, ["0", "1", "1", "0"], ["0", "8", "0", "0"], 4, "8"),
        (2, ["0", "0", "1", "0"], ["0", "0", "0", "9"], 4, "9"),
        (0, ["1", "0", "1", "0"], ["55", "0", "0", "0"], 4, "55"),
        (2, ["0", "0", "0", "1"], ["0", "0", "0", "7"], 4, "7"),
        (2, ["0", "0", "0", "1"], ["0", "0", "7", "7"], 4, "7"),
        (2, ["0", "0", "0", "1"], ["0", "7", "7", "7"], 4, "7"),
    ]
)
def test_it_belongs_to_island(pos, curr_line, prev_line, length, expected):
    assert it_belongs_to_island(pos, curr_line, prev_line, length) == expected

@pytest.mark.parametrize(
    "pos, curr_line, expected",
    [ 
        (3, ["0", "1", "1", "5", "0"], ["0", "5", "5", "5", "0"]),
        (3, ["0", "1", "0", "5", "0"], ["0", "1", "0", "5", "0"]),
        (2, ["0", "1", "5", "1", "0"], ["0", "5", "5", "1", "0"]),
    ]
)
def test_fill_back(pos, curr_line, expected):
    fill_back(pos, curr_line)
    assert curr_line == expected
