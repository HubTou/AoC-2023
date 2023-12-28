#!/usr/bin/env python3

import pprint

from aoc_lib import *

#CYCLES = 1
#CYCLES = 2
CYCLES = 3
#CYCLES = 1000000000

PROGRESS_DOT = 1000000

def roll_north(table):
    collapsed_inverted_table = []
    for line in invert_strings_table(table):
        while '.O' in line:
            line = line.replace('.O', 'O.')
        collapsed_inverted_table.append(line)

    return invert_strings_table(collapsed_inverted_table)

def roll_east(table):
    new_table = []
    for line in table:
        while 'O.' in line:
            line = line.replace('O.', '.O')
        new_table.append(line)

    return new_table

def roll_south(table):
    collapsed_inverted_table = []
    for line in invert_strings_table(table):
        while 'O.' in line:
            line = line.replace('O.', '.O')
        collapsed_inverted_table.append(line)

    return invert_strings_table(collapsed_inverted_table)

def roll_west(table):
    new_table = []
    for line in table:
        while '.O' in line:
            line = line.replace('.O', 'O.')
        new_table.append(line)

    return new_table

def spin_cycle(table):
    return roll_east(roll_south(roll_west(roll_north(table))))

def measure_load(table):
    total_load = 0
    weight = len(table)
    for line in table:
        load = line.count('O') * weight
        total_load += load
        weight -= 1

    return total_load

lines = read_input_file()
timer = start_timer()

# Processing the input file
pprint.pprint(lines)
print()

table = lines
for c in range(1, CYCLES + 1):
    table = spin_cycle(table)
    if not (c % PROGRESS_DOT):
        print(".", end="")
print()
pprint.pprint(table)
print()

print(f"Total load on the north support beams after {CYCLES} cycles: {measure_load(table)}")

stop_timer(timer)
sys.exit(0)
