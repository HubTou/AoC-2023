#!/usr/bin/env python3

import pprint
import sys

from aoc_lib import *

lines = read_input_file()
timer = start_timer()

# First, find the starting position
start_line = start_char = -1
for start_line in range(len(lines)):
    start_char = lines[start_line].find("S")
    if start_char != -1:
        break

# Second, determine the starting position pipe type
connected_to_north = False
connected_to_east = False
connected_to_south = False
connected_to_west = False
if start_line != 0 and lines[start_line - 1][start_char] in ["F", "|", "7"]:
    connected_to_north = True
if start_char != len(lines[start_line]) - 1 and lines[start_line][start_char + 1] in ["7", "-", "J"]:
    connected_to_east = True
if start_line != len(lines) - 1 and lines[start_line + 1][start_char] in ["L", "|", "J"]:
    connected_to_south = True
if start_char != 0 and lines[start_line][start_char - 1] in ["F", "-", "L"]:
    connected_to_west = True

if connected_to_north and connected_to_south:
    start_type = "|"
elif connected_to_east and connected_to_west:
    start_type = "-"
elif connected_to_north and connected_to_east:
    start_type = "L"
elif connected_to_north and connected_to_west:
    start_type = "J"
elif connected_to_south and connected_to_west:
    start_type = "7"
elif connected_to_south and connected_to_east:
    start_type = "F"

# Third follow the path till we go back to starting position
path = []
l = start_line
c = start_char
t = start_type
if t == "|":
    direction = "South"
elif t == "-":
    direction = "East"
else:
    direction = "?"
while True:
    print(l, c, t)
    if t == "|":
        if direction == "South":
            l += 1
        else:
            l -= 1
    elif t == "-":
        if direction == "East":
            c += 1
        else:
            c -= 1
    elif t == "L":
        if direction == "West":
            l -= 1
            direction = "North"
        else:
            c += 1
            direction = "East"
    elif t == "J":
        if direction == "South":
            c -= 1
            direction = "West"
        else:
            l -= 1
            direction = "North"
    elif t == "7":
        if direction == "East":
            l += 1
            direction = "South"
        else:
            c -= 1
            direction = "West"
    elif t == "F":
        if direction == "North":
            c += 1
            direction = "East"
        else:
            l += 1
            direction = "South"

    t = lines[l][c]
    if t == "S":
        break
    path.append([l, c])

print(path) 
print("=====")
print(f"Steps to the farthest point: {1 + len(path) // 2}")

stop_timer(timer)
sys.exit(0)
