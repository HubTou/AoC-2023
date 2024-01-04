#!/usr/bin/env python3

import pprint
import re
import sys

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
box_labels = {}
box_focals = {}
for line in lines:
    for step in line.split(','):
        label = re.sub(r"[-=0-9]", "", step)
        operation = re.sub(r"[a-z0-9]", "", step)
        if operation == '=':
            focal_length = int(re.sub(r"[-=a-z]", "", step))
        else:
            focal_length = -1
        box4step = HASH(label)
        print(f"step: '{step}' label: '{label}' operation: '{operation}' focal length: {focal_length} box: {box4step}")
        if operation == '=':
            if box4step in box_labels:
                if label in box_labels[box4step]:
                    i = box_labels[box4step].index(label)
                    box_focals[box4step][i] = focal_length
                else:
                    box_labels[box4step].append(label)
                    box_focals[box4step].append(focal_length)
            else:
                box_labels[box4step] = [label]
                box_focals[box4step] = [focal_length]
        else: # operation == '-'
            if box4step in box_labels:
                if label in box_labels[box4step]:
                    i = box_labels[box4step].index(label)
                    del box_labels[box4step][i]
                    del box_focals[box4step][i]

pprint.pprint(box_labels)
pprint.pprint(box_focals)
print()

total_focusing_power = 0
for box_number in range(256):
    if box_number in box_labels:
        for slot in range(len(box_labels[box_number])):
            focusing_power = (box_number + 1) * (slot + 1) * box_focals[box_number][slot]
            print(f"{box_labels[box_number][slot]}: {box_number + 1} * {slot + 1} * {box_focals[box_number][slot]} = {focusing_power}")
            total_focusing_power += focusing_power

print("=====")
print(f"Focusing power: {total_focusing_power}")

stop_timer(timer)
sys.exit(0)
