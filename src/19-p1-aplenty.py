#!/usr/bin/env python3

import pprint
import re
import sys

from aoc_lib import *

lines = read_input_file()
timer = start_timer()

# Processing input file
in_workflows = True
workflows = {}
parts = []
for line in lines:
    if line:
        if in_workflows:
            name = re.sub(r"{.*", "", line)
            rules = re.sub(r"^[a-z]*{", "", line)
            rules = re.sub(r"}$", "", rules)

            workflows[name] = []
            for rule in rules.split(","):
                workflows[name].append(rule)
        else: # in parts
            group = re.match(r"{x=([0-9]*),m=([0-9]*),a=([0-9]*),s=([0-9]*)}", line)
            parts.append({'x':int(group[1]), 'm':int(group[2]), 'a':int(group[3]), 's':int(group[4])})
    else:
        in_workflows = False

pprint.pprint(workflows)
print()
#pprint.pprint(parts)

# Processing parts through workflows
accepted = []
rejected = []
ratings_sum = 0
for part in parts:
    print(f"{part}: ", end="")
    workflow = "in"
    processing = True
    while processing:
        print(f"{workflow} -> ", end="")
        for rule in workflows[workflow]:
            group = re.match(r"^([xmas])([><])([0-9]+):([ARa-z]+)$", rule)
            if group == None:
                if rule == "A":
                    print("A")
                    accepted.append(part)
                    ratings_sum += part['x'] + part['m'] + part['a'] + part['s']
                    processing = False
                    break
                elif rule == "R":
                    print("R")
                    rejected.append(part)
                    processing = False
                    break
                else:
                    workflow = rule
                    break
            else:
                category = group[1]
                operation = group[2]
                value = int(group[3])
                new_workflow = group[4]

                if (operation == ">" and part[category] > value) or (operation == "<" and part[category] < value):
                    if new_workflow == "A":
                        print("A")
                        accepted.append(part)
                        ratings_sum += part['x'] + part['m'] + part['a'] + part['s']
                        processing = False
                        break
                    elif new_workflow == "R":
                        print("R")
                        rejected.append(part)
                        processing = False
                        break
                    else:
                        workflow = new_workflow
                        break

print("=====")
print(f"Sum of the ratings of accepted parts: {ratings_sum}")

stop_timer(timer)
sys.exit(0)
