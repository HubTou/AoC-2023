#!/usr/bin/env python3

import sys
import textwrap
import time

####################################################################################################

def read_input_file():
    """ Returns an input file as a table of strings """
    # Managing the command line
    if len(sys.argv) != 2:
        print(f"USAGE: {sys.argv[0]} filename", file=sys.stderr)
        sys.exit(1)

    # Reading the input file
    try:
        with open(sys.argv[1]) as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        print("ERROR: Filename doesn't exist", file=sys.stderr)
        sys.exit(1)

    return lines

####################################################################################################

def start_timer():
    """ Starts measuring execution time and returns a timer """
    return time.perf_counter()

def stop_timer(t1):
    """ Stops measuring execution time and prints it """
    t2 = time.perf_counter()
    print(f"\nINFO: Processed in {t2 - t1:.2f} seconds", file=sys.stderr)

####################################################################################################

def invert_strings_table(table):
    """
    table = ['abcd', 'efgh', 'ijkl']
    print(invert_strings_table(table))
    ['aei', 'bfj', 'cgk', 'dhl']
    """
    return ["".join(list(x)) for x in zip(*table)]

####################################################################################################

def hash_line(line, special_char):
    """
    hash_line('##.#.', '#') will return 11 (1+2+8)
    """
    value = 0
    multiplier = 1
    for character in line:
        if character == special_char:
            value += multiplier
        multiplier *= 2

    return value

def hash_lines(lines, special_char):
    """
    hash_line(['##.#.', '.#.#.'], '#') will return [11 , 10] (11 (1+2+8), 10 (2 + 8))
    """
    values = []
    for line in lines:
        values.append(hash_line(line, special_char))
    return values

def hash_table(lines, special_char):
    """
    hash_line(['##.#.', '.#.#.'], '#') will return 331 (11 + 10 * 32)
    """
    value = 0
    multiplier = 1
    for line in lines:
        value += hash_line(line, special_char) * multiplier
        multiplier *= 2 ** len(line)
    return value

def get_line_from_hash(hash_value, line_length, hit_char, miss_char):
    """
    get_line_from_hash(11, 5, '#', '.') will return '##.#.'
    """
    line = f'{hash_value:0{line_length}b}'.replace('0', miss_char).replace('1', hit_char)
    line_as_list = list(line)
    line_as_list.reverse()

    return "".join(line_as_list)

def get_table_from_hash(hash_value, line_length, hit_char, miss_char):
    """
    get_table_from_hash(331, 5, '#', '.') will return ['##.#.', '.#.#.']
    """
    return textwrap.wrap(get_line_from_hash(hash_value, line_length, hit_char, miss_char), line_length)

####################################################################################################

def flood_fill(text_map, y, x, from_char, to_char):
    """
    Starting at (x,y) position, will recursively change any adjacent character that matches from_char to to_char
    Adapted from http://inventwithpython.com/blog/2011/08/11/recursion-explained-with-the-flood-fill-algorithm-and-zombies-and-cats/
    You have to set sys.setrecursionlimit(n) with n > 1000 if you hit the recursion limit
    """
    height = len(text_map)
    width = len(text_map[0])

    if text_map[y][x] != from_char:
        return text_map

    text_map[y] = text_map[y][:x] + to_char + text_map[y][x+1:]

    if x > 0:
        text_map = flood_fill(text_map, y, x - 1,  from_char, to_char)
    if x < width - 1:
        text_map = flood_fill(text_map, y, x + 1,  from_char, to_char)
    if y > 0:
        text_map = flood_fill(text_map, y - 1, x, from_char, to_char)
    if y < height - 1:
        text_map = flood_fill(text_map, y + 1, x, from_char, to_char)

    return text_map
