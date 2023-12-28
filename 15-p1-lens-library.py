#!/usr/bin/env python3

import pprint

from aoc_lib import *

def HASH(step):
    current_value = 0
    for character in step:
        current_value += ord(character)
        current_value *= 17
        current_value = current_value % 256

    return current_value

lines = read_input_file()
timer = start_timer()

# Processing the input file
sum_of_the_results =0
for line in lines:
    for step in line.split(','):
        hash_value = HASH(step)
        sum_of_the_results += hash_value
        print(f"{step}: {hash_value}")

print("=====")
print(f"Sum of the results: {sum_of_the_results}")

stop_timer(timer)
sys.exit(0)
