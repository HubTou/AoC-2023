#!/usr/bin/env python3

import pprint
import sys

from aoc_lib import *

START = "S"
GARDEN = "."
ROCKS = "#"
REACHABLE_TILE = "O"

STEPS = 64

def print_reachable_map(text_map, stepped_tiles):
    for y, line in enumerate(text_map):
        for x, character in enumerate(line):
            if (y, x) in stepped_tiles:
                print(REACHABLE_TILE, end="")
            else:
                print(character, end="")
        print()

lines = read_input_file()
timer = start_timer()

# 1) Find the starting position and change it to a garden plot
start_y, start_x = find_starting_position(lines, START)
text_map = replace_character(lines, start_y, start_x, GARDEN)
height = len(text_map)
width = len(text_map[0])

# 2) Make the required number of steps
step = 0
stepped_tiles = [(start_y, start_x)]
while step != STEPS:
    reachable_tiles = []
    for tile in stepped_tiles:
        y = tile[0]
        x = tile[1]
        if y > 0 and text_map[y - 1][x] == GARDEN:
            if (y - 1, x) not in reachable_tiles:
                reachable_tiles.append((y - 1, x))
        if x > 0 and text_map[y][x - 1] == GARDEN:
            if (y, x - 1) not in reachable_tiles:
                reachable_tiles.append((y, x - 1))
        if y < height - 1 and text_map[y + 1][x] == GARDEN:
            if (y + 1, x) not in reachable_tiles:
                reachable_tiles.append((y + 1, x))
        if x < width - 1 and text_map[y][x + 1] == GARDEN:
            if (y, x + 1) not in reachable_tiles:
                reachable_tiles.append((y, x + 1))
    step += 1
    stepped_tiles = reachable_tiles.copy()

print_reachable_map(text_map, stepped_tiles)
print()
print(f"Reachable garden plots in {STEPS} steps: {len(stepped_tiles)}")

stop_timer(timer)
sys.exit(0)
