#!/usr/bin/env python3

import pprint

from aoc_lib import *

#CYCLES = 1
#CYCLES = 2
#CYCLES = 3
CYCLES = 1000000000

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
table = lines
pprint.pprint(table)
print()
table_hash = hash_table(table, 'O')
table_hashes = [table_hash]
for c in range(1, CYCLES + 1):
    table = spin_cycle(table)
    table_hash = hash_table(table, 'O')
    if table_hash in table_hashes:
        cycle_start = table_hashes.index(table_hash)
        cycle_length = c - cycle_start
        print(f"Found same hash after {c} cycles, starting at {cycle_start} with length of {cycle_length}")
        target_table_hash = table_hashes[((CYCLES - c) % cycle_length) + cycle_start]
        target_table = get_table_from_hash(target_table_hash, len(lines[0]), 'O', '.')
        pprint.pprint(target_table)
        print()
        print(f"Total load on the north support beams: {measure_load(target_table)}")
        break
    table_hashes.append(table_hash)

stop_timer(timer)
sys.exit(0)
