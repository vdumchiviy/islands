import pytest
from utils import get_zero_row, get_line_length, read_file, recode_string

def test_get_zero_row():
    actual = get_zero_row(5)
    assert actual == ['0', '0', '0', '0', '0']

    with pytest.raises(ValueError) as e:
        get_zero_row(0)
        assert str(e) == "[get_zero_row]: length shoud be more then 0."

def test_get_line_length():
    assert get_line_length("src/samples/island01.txt") == 9

    with pytest.raises(FileNotFoundError):
        get_line_length("fooboo")

def test_read_file():
    expected = 8
    actual = 0
    for t in read_file("src/samples/island01.txt"):
        actual += 1
    assert actual == expected

    with pytest.raises(FileNotFoundError):
        for t in read_file("fooboo"):
            actual += 1


def test_recode_string():
    assert recode_string("0123\n") == "0123"
    assert recode_string("0123") == "0123"
    assert recode_string("") == ""
