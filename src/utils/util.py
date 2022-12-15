from typing import List


def recode_string(s: str) -> str:
    result = s.replace("\n", "")
    return result


def read_file(filename: str):
    for line in open(file=filename, mode="r"):
        result = list(recode_string(line))
        yield result


def get_line_length(filename: str) -> int:
    f = open(file=filename, mode="r")
    line = f.readline()
    result = len(list(recode_string(line)))
    f.close()

    return result


def get_zero_row(length: int) -> List[str]:
    if length <= 0:
        raise ValueError("[get_zero_row]: length shoud be more then 0.")
    return list("0" * length)
