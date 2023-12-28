#!/usr/bin/env python3

import pprint

from aoc_lib import *

def print_energized_tiles(x, y):
    for j in range(height):
        for i in range(width):
            if energized_tiles[j][i]:
                if j == y and i == x:
                    print('X', end="")
                else:
                    print('#', end="")
            else:
                print('.', end="")
        print()

def beam(x, y, direction):
    while True:
        if direction == "up":
            if y < height:
                if up_done[y][x]:
                    break
                up_done[y][x] = True
            y -= 1
            if y < 0:
                break
            energized_tiles[y][x] = True
            #pprint.pprint(contraption)
            #print_energized_tiles(x, y)
            #input(">")
            if contraption[y][x] == "/":
                direction = "right"
            elif contraption[y][x] == "\\":
                direction = "left"
            elif contraption[y][x] == "-":
                beam(x, y, "left")
                beam(x, y, "right")
                break

        elif direction == "right":
            if x >= 0:
                if right_done[y][x]:
                    break
                right_done[y][x] = True
            x += 1
            if x == width:
                break
            energized_tiles[y][x] = True
            #pprint.pprint(contraption)
            #print_energized_tiles(x, y)
            #input(">")
            if contraption[y][x] == "/":
                direction = "up"
            elif contraption[y][x] == "\\":
                direction = "down"
            elif contraption[y][x] == "|":
                beam(x, y, "up")
                beam(x, y, "down")
                break

        elif direction == "down":
            if y >= 0:
                if down_done[y][x]:
                    break
                down_done[y][x] = True
            y += 1
            if y == height:
                break
            energized_tiles[y][x] = True
            #pprint.pprint(contraption)
            #print_energized_tiles(x, y)
            #input(">")
            if contraption[y][x] == "/":
                direction = "left"
            elif contraption[y][x] == "\\":
                direction = "right"
            elif contraption[y][x] == "-":
                beam(x, y, "left")
                beam(x, y, "right")
                break

        elif direction == "left":
            if x < width:
                if left_done[y][x]:
                    break
                left_done[y][x] = True
            x -= 1
            if x < 0:
                break
            energized_tiles[y][x] = True
            #pprint.pprint(contraption)
            #print_energized_tiles(x, y)
            #input(">")
            if contraption[y][x] == "/":
                direction = "down"
            elif contraption[y][x] == "\\":
                direction = "up"
            elif contraption[y][x] == "|":
                beam(x, y, "up")
                beam(x, y, "down")
                break

def get_energized_tiles(x, y, direction):
    beam(x, y, direction)

    total_energized_tiles = 0
    for y in range(height):
        for x in range(width):
            if energized_tiles[y][x]:
                total_energized_tiles += 1

    return total_energized_tiles

contraption = read_input_file()
timer = start_timer()

# Processing the input file
height = len(contraption)
width = len(contraption[0])
energized_tiles = [ [ False for i in range(width) ] for j in range(height) ]
up_done = [ [ False for i in range(width) ] for j in range(height) ]
right_done = [ [ False for i in range(width) ] for j in range(height) ]
down_done = [ [ False for i in range(width) ] for j in range(height) ]
left_done = [ [ False for i in range(width) ] for j in range(height) ]

best_total_energized_tiles = 0
best_x = None
best_y = None
best_direction = None

for x in range(width):
    energized_tiles = [ [ False for i in range(width) ] for j in range(height) ]
    up_done = [ [ False for i in range(width) ] for j in range(height) ]
    right_done = [ [ False for i in range(width) ] for j in range(height) ]
    down_done = [ [ False for i in range(width) ] for j in range(height) ]
    left_done = [ [ False for i in range(width) ] for j in range(height) ]
    y = -1
    direction = "down"
    total = get_energized_tiles(x, y, direction)
    if total > best_total_energized_tiles:
        best_total_energized_tiles = total
        best_x = x
        best_y = y
        best_direction = direction

    energized_tiles = [ [ False for i in range(width) ] for j in range(height) ]
    up_done = [ [ False for i in range(width) ] for j in range(height) ]
    right_done = [ [ False for i in range(width) ] for j in range(height) ]
    down_done = [ [ False for i in range(width) ] for j in range(height) ]
    left_done = [ [ False for i in range(width) ] for j in range(height) ]
    y = height
    direction = "up"
    total = get_energized_tiles(x, y, direction)
    if total > best_total_energized_tiles:
        best_total_energized_tiles = total
        best_x = x
        best_y = y
        best_direction = direction

for y in range(height):
    energized_tiles = [ [ False for i in range(width) ] for j in range(height) ]
    up_done = [ [ False for i in range(width) ] for j in range(height) ]
    right_done = [ [ False for i in range(width) ] for j in range(height) ]
    down_done = [ [ False for i in range(width) ] for j in range(height) ]
    left_done = [ [ False for i in range(width) ] for j in range(height) ]
    x = -1
    direction = "right"
    total = get_energized_tiles(x, y, direction)
    if total > best_total_energized_tiles:
        best_total_energized_tiles = total
        best_x = x
        best_y = y
        best_direction = direction

    energized_tiles = [ [ False for i in range(width) ] for j in range(height) ]
    up_done = [ [ False for i in range(width) ] for j in range(height) ]
    right_done = [ [ False for i in range(width) ] for j in range(height) ]
    down_done = [ [ False for i in range(width) ] for j in range(height) ]
    left_done = [ [ False for i in range(width) ] for j in range(height) ]
    x = width
    direction = "left"
    total = get_energized_tiles(x, y, direction)
    if total > best_total_energized_tiles:
        best_total_energized_tiles = total
        best_x = x
        best_y = y
        best_direction = direction

print()
print(f"Best energized tiles: {best_total_energized_tiles}")
print(f"From y: {best_y} x: {best_x} direction: '{best_direction}'")

stop_timer(timer)
sys.exit(0)
