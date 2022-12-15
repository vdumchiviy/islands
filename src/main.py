""" Main module """
import sys
from typing import List, Optional

from utils.util import get_line_length, get_zero_row, read_file
from utils.algo import is_start_island, it_belongs_to_island, fill_back
       
def get_file_name_from_command_line() -> Optional[str]:
    args = sys.argv
    result = None
    if len(args) == 1:
        print('Please provide any island file')
    else:
        result = args[1]
    return result

def main(file_name: str):
    length = get_line_length(file_name)
    prev_line = get_zero_row(length)
    islands = 2
    line_number = 0
    for curr_line in read_file(file_name):
        line_number += 1
        pos = 0
        while pos < length:
            if curr_line[pos] == "1":
                if is_start_island(pos, curr_line, prev_line, length):
                    islands += 1
                    curr_line[pos] = str(islands)
                else:
                    island = it_belongs_to_island(
                                        pos, curr_line, prev_line, length
                                    )
                    if island:
                        curr_line[pos] = island
                fill_back(pos, curr_line)
            pos += 1
        prev_line = curr_line

    print(islands - 2)

file_name = get_file_name_from_command_line()
if file_name:
    main(file_name)
