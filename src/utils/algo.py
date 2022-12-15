
from typing import List, Optional


def is_start_island(
    pos: int,
    curr_line: List[str],
    prev_line: List[str],
    length: int
) -> bool:
    """
    Need to check start island:

    000  000
    0x0  1x0
    """
    if pos > 0:
        if (curr_line[pos-1] != "0" and curr_line[pos-1] != "1") or (
            prev_line[pos-1] != "0"
        ):
            return False

    if prev_line[pos] != "0":
        return False

    if pos < length-1:
        if curr_line[pos+1] != "0" or prev_line[pos+1] != "0":
            return False

    return True


def it_belongs_to_island(
    pos: int,
    curr_line: List[str],
    prev_line: List[str],
    length: int,
) -> Optional[str]:
    """Need to chack what island is owner of this 1"""

    if pos > 0:
        if curr_line[pos-1] != "0" and curr_line[pos-1] != "1":
            return curr_line[pos-1]

        if prev_line[pos-1] != "0":
            return prev_line[pos-1]

    if prev_line[pos] != "0":
        return prev_line[pos]

    if pos < length-1:
        if prev_line[pos+1] != "0":
            return prev_line[pos+1]

        if curr_line[pos+1] != "0" and curr_line[pos+1] != "1":
            return curr_line[pos+1]
    return None

def fill_back(
    pos: int,
    curr_line: List[str]
) -> None:

    while pos > 0 and curr_line[pos-1] == "1":
        curr_line[pos-1] = curr_line[pos]
        pos -= 1
 