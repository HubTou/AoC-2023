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

beam(-1, 0, "right")
print_energized_tiles(0, 0)

total_energized_tiles = 0
for y in range(height):
    for x in range(width):
        if energized_tiles[y][x]:
            total_energized_tiles += 1
print()
print(f"Energized tiles: {total_energized_tiles}")

stop_timer(timer)
sys.exit(0)
