#!/usr/bin/env python3

import pprint
import sys

from aoc_lib import *

lines = read_input_file()
timer = start_timer()

# 1) find the starting position
start_line = start_char = -1
for start_line in range(len(lines)):
    start_char = lines[start_line].find("S")
    if start_char != -1:
        break

# 2) determine the starting position pipe type
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

# 3) follow the path till we go back to starting position
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


# 4) order the results
northerner_line = southerner_line = start_line
table = {}
table[start_line] = [start_char]
for pipe in path:
    if pipe[0] < northerner_line:
        northerner_line = pipe[0]
    if pipe[0] > southerner_line:
        southerner_line = pipe[0]
    if pipe[0] in table:
        table[pipe[0]].append(pipe[1])
    else:
        table[pipe[0]] = [pipe[1]]
for key, value in table.items():
    table[key] = sorted(value)

# 5) clear everything that's not in the path
height = len(lines)
width = len(lines[0])
landscape = []
enhanced_text = {"F": "┌", "-": "─", "7": "┐", "|": "│", "L": "└", "J": "┘"}
for ln in range(height):
    if ln in table:
        row = ""
        for cn in range(width):
            if cn in table[ln]:
                border_type = lines[ln][cn]
                if border_type == "S":
                    border_type = start_type
                row += enhanced_text[border_type]
            else:
                row += "."
        landscape.append(row)
    else:
        landscape.append("." * width)

pprint.pprint(landscape)
print()

# 6) determine what's inside the loop
tiles_enclosed = 0
for ln in range(height):
    inside = False
    half = ""
    for cn in range(width):
        character = landscape[ln][cn]
        if inside:
            if character == ".":
                tiles_enclosed += 1
                character = "I"
                half = ""
            elif character == "│":
                inside = False
                half = ""
            elif character == "┌":
                if half == "┘":
                    inside = False
                    half = ""
                else:
                    half = "┌"
            elif character == "┐":
                if half == "└":
                    inside = False
                    half = ""
                elif half == "┌":
                    half = ""
                else:
                    half = "┐"
            elif character == "└":
                if half == "┐":
                    inside = False
                    half = ""
                else:
                    half = "└"
            elif character == "┘":
                if half == "┌":
                    inside = False
                    half = ""
                elif half == "└":
                    half = ""
                else:
                    half = "┘"

        else: # outside
            if character == ".":
                half = ""
            elif character == "│":
                inside = True
                half = ""
            elif character == "┌":
                if half == "┘":
                    inside = True
                    half = ""
                else:
                    half = "┌"
            elif character == "┐":
                if half == "└":
                    inside = True
                    half = ""
                elif half == "┌":
                    half = ""
                else:
                    half = "┐"
            elif character == "└":
                if half == "┐":
                    inside = True
                    half = ""
                else:
                    half = "└"
            elif character == "┘":
                if half == "┌":
                    inside = True
                    half = ""
                elif half == "└":
                    half = ""
                else:
                    half = "┘"

        print(character, end="")
    print()

print()
print(f"{tiles_enclosed} tile(s) are enclosed by the loop")

stop_timer(timer)
sys.exit(0)
