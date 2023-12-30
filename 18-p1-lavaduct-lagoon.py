#!/usr/bin/env python3

import pprint
import re
import sys

from aoc_lib import *

TRENCH = "#"
GROUND = '.'

def get_field_size(lines):
    min_x = 1000000
    max_x = -1000000
    min_y = 1000000
    max_y = -1000000
    x = 0
    y = 0
    for line in lines:
        words = line.split()
        direction = words[0]
        length = int(words[1])
        if direction == 'R':
            x += length
            if x > max_x:
                max_x = x
        elif direction == 'D':
            y += length
            if y > max_y:
                max_y = y
        elif direction == 'L':
            x -= length
            if x < min_x:
                min_x = x
        elif direction == 'U':
            y -= length
            if y < min_y:
                min_y = y
    return min_x, max_x, min_y, max_y

def init_field(min_x, max_x, min_y, max_y):
    return [ GROUND * (max_x - min_x + 1) for j in range(max_y - min_y + 1) ]

def print_field(field, current_x, current_y):
    for j in range(len(field)):
        if j == current_y:
            for i in range(len(field[j])):
                if i == current_x:
                    print("X", end="")
                else:
                    print(field[j][i], end="")
            print()
        else:
            print(field[j])
    print()

def dig_trench(field, x, y):
    field[y] = field[y][:x] + TRENCH + field[y][x+1:]
    for line in lines:
        words = line.split()
        direction = words[0]
        length = int(words[1])
        #color = words[2]

        #print(f"'{direction}' * {length}")
        if direction == 'R':
            field[y] = field[y][:x+1] + (TRENCH * length) + field[y][x+1+length:]
            x += length
        elif direction == 'D':
            for new_y in range(y + 1, y + length + 1):
                field[new_y] = field[new_y][:x] + TRENCH + field[new_y][x+1:]
                y += 1
        elif direction == 'L':
            field[y] = field[y][:x-length] + (TRENCH * length) + field[y][x:]
            x -= length
        elif direction == 'U':
            for new_y in range(y - 1, y - length - 1, -1):
                field[new_y] = field[new_y][:x] + TRENCH + field[new_y][x+1:]
                y -= 1
        #print_field(field, x, y)
        #input(">")

    return field

def dig_interior(field, x, y):
    if field[y+1][x+1] != GROUND:
        print(f"ERROR: south east character from position is not a ground character!", file=sys.stderr)
        sys.exit(1)

    sys.setrecursionlimit(100000)
    return flood_fill(field, y+1, x+1, GROUND, TRENCH)

def count_lagoon_capacity(field):
    capacity = 0
    for line in field:
        capacity += line.count(TRENCH)
    return capacity

lines = read_input_file()
timer = start_timer()

# Processing the input file
min_x, max_x, min_y, max_y = get_field_size(lines)
field = init_field(min_x, max_x, min_y, max_y)
x = - min_x
y = - min_y
field = dig_trench(field, x, y)
print_field(field, x, y)
field = dig_interior(field, x, y)
print_field(field, x, y)
print(f"Lava lagoon capacity: {count_lagoon_capacity(field)}")

stop_timer(timer)
sys.exit(0)
