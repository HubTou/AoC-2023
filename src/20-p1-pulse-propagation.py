#!/usr/bin/env python3

import pprint
import queue
import re
import sys

from aoc_lib import *

BUTTON_PRESSES = 1000

def load_modules(lines):
    modules = {}
    referers = {}
    for line in lines:
        group = re.match(r"([%&]?)([a-z]+) -> ([a-z, ]+)", line)
        if group == None:
            print(f"ERROR: unexpected format for line '{line}'", file=sys.stderr)
            sys.exit(1)
        prefix = group[1]
        name = group[2]
        destinations = group[3].split(", ")

        if prefix == "%":
            modules[name] = {"type": "flip-flop", "dest": destinations, "state": 0} 
        elif prefix == "&":
            modules[name] = {"type": "conjunction", "dest": destinations, "inputs": {}} 
        elif name == "broadcaster":
            modules[name] = {"type": "broadcast", "dest": destinations} 
        else:
            modules[name] = {"type": "untyped", "dest": destinations}
    
        for module in destinations:
            if module in referers:
                referers[module].append(name)
            else:
                referers[module] = [name]
 
    # let's not assume that all inputs of a conjunction module
    # will appear before it
    for name, details in modules.items():
        if details["type"] == "conjunction":
            for module in referers[name]:
                modules[name]["inputs"][module] = "low"
 
    # also handle the unspecified untyped modules case of example 2
    for name in referers:
        if name not in modules:
            modules[name] = {"type": "untyped", "dest": []}
 
    #print("Modules:")
    #pprint.pprint(modules)
    #print()
 
    return modules

def push_button(modules, todo):
    high_pulses = 0
    todo.put("button low broadcaster")
    low_pulses = 1
    while todo.qsize():
        src_module, pulse, target = todo.get().split()
        print(f"{src_module} -{pulse}-> {target}")

        dst_module = modules[target]
        if dst_module["type"] == "broadcast":
            for destination in dst_module["dest"]:
                todo.put(f"{target} {pulse} {destination}")
                if pulse == "high":
                    high_pulses += 1
                else:
                    low_pulses += 1
        elif dst_module["type"] == "flip-flop":
            if pulse == "low":
                if dst_module["state"]:
                    dst_module["state"] = 0
                    for destination in dst_module["dest"]:
                        todo.put(f"{target} low {destination}")
                        low_pulses += 1
                else:
                    dst_module["state"] = 1
                    for destination in dst_module["dest"]:
                        todo.put(f"{target} high {destination}")
                        high_pulses += 1
        elif dst_module["type"] == "conjunction":
            dst_module["inputs"][src_module] = pulse
            all_high = True
            for input_module, input_memory in dst_module["inputs"].items():
                if input_memory == "low":
                    all_high = False
                    for destination in dst_module["dest"]:
                        todo.put(f"{target} high {destination}")
                        high_pulses += 1
                    break
            if all_high:
                for destination in dst_module["dest"]:
                    todo.put(f"{target} low {destination}")
                    low_pulses += 1
        elif dst_module["type"] == "untyped":
            pass
    print()

    return modules, todo, high_pulses, low_pulses

def states_all_off(modules):
    for value in modules.values():
        if value["type"] == "flip-flop":
            if value["state"] != 0:
                return False

    return True

lines = read_input_file()
timer = start_timer()

# 1) Get the modules dictionary
modules = load_modules(lines)

# 2) Find the cycle length
todo = queue.SimpleQueue()
modules, todo, high_pulses, low_pulses = push_button(modules, todo)
button_presses = 1
while not states_all_off(modules):
    modules, todo, hp, lp = push_button(modules, todo)
    high_pulses += hp
    low_pulses += lp
    button_presses += 1
    if button_presses == BUTTON_PRESSES:
        break

if button_presses == BUTTON_PRESSES:
    print(f"No cycle found after {BUTTON_PRESSES} button presses")
else:
    print(f"Cycle length = {button_presses} button presses")
print(f"  with {low_pulses} low pulses sent")
print(f"  and {high_pulses} high pulses sent")

print()
print(f"Result for {BUTTON_PRESSES} button presses is: {((BUTTON_PRESSES//button_presses)**2) * high_pulses * low_pulses}")

stop_timer(timer)
sys.exit(0)
