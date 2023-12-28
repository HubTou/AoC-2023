#!/usr/bin/env python3

import pprint

from aoc_lib import *

lines = read_input_file()
timer = start_timer()

# Processing the input file
pprint.pprint(lines)
print()

inverted_table = invert_strings_table(lines)
#pprint.pprint(inverted_table)
#print()

collapsed_inverted_table = []
for line in inverted_table:
    while '.O' in line:
        line = line.replace('.O', 'O.')
    collapsed_inverted_table.append(line)
#pprint.pprint(collapsed_inverted_table)
#print()

table = invert_strings_table(collapsed_inverted_table)
pprint.pprint(table)
print()

total_load = 0
weight = len(table)
for line in table:
    load = line.count('O') * weight
    total_load += load
    weight -= 1
print(f"Total load on the north support beams: {total_load}")

stop_timer(timer)
sys.exit(0)
