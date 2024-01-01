#!/usr/bin/env python3

import pprint
import re
import sys

from aoc_lib import *

MIN_VALUE = 1
MAX_VALUE = 4000

def update_category(interval, min_value, max_value):
    new_min_value = interval[0]
    new_max_value = interval[1]

    if min_value > new_min_value:
        if min_value > new_max_value:
            print("HOUSTON WE HAVE A PROBLEM!")
            sys.exit(1)
        new_min_value = min_value

    if max_value < new_max_value:
        if max_value < new_min_value:
            print("HOUSTON WE HAVE A PROBLEM!")
            sys.exit(1)
        new_max_value = max_value
    
    return (new_min_value, new_max_value)

def update_constraints(constraints, history, new_category, new_operation, new_value):
    new_constraints = constraints.copy()

    if history:
        for rule in history:
            group = re.match(r"^([xmas])([><])([0-9]+):([ARa-z]+)$", rule)
            category = group[1]
            operation = group[2]
            value = int(group[3])

            # We need to inverse the rule
            if operation == "<":
                if category in new_constraints:
                    new_constraints[category] = update_category(new_constraints[category], value, MAX_VALUE)
                else:
                    new_constraints[category] = (value, MAX_VALUE)
            else:
                if category in new_constraints:
                    new_constraints[category] = update_category(new_constraints[category], MIN_VALUE, value)
                else:
                    new_constraints[category] = (MIN_VALUE, value)

    if new_category != None:
        if new_operation == "<":
            if new_category in new_constraints:
                new_constraints[new_category] = update_category(new_constraints[new_category], MIN_VALUE, new_value - 1)
            else:
                new_constraints[new_category] = (MIN_VALUE, new_value - 1)
        else:
            if new_category in new_constraints:
                new_constraints[new_category] = update_category(new_constraints[new_category], new_value + 1, MAX_VALUE)
            else:
                new_constraints[new_category] = (new_value + 1, MAX_VALUE)

    return new_constraints

def compute_combinations(constraints):
    combinations = 1
    print("combinations = 1 ", end="")
    for category in ['x', 'm', 'a', 's']:
        if category in constraints:
            items = constraints[category][1] - constraints[category][0] + 1
            print(f"* {items} ", end="")
            combinations *= items
        else:
            print(f"* {MAX_VALUE} ", end="")
            combinations *= MAX_VALUE
    print(f"= {combinations:,} ")

    return combinations

def compute_accepted_combinations(workflow, constraints):
    total_combinations = 0
    history = []
    for rule in workflows[workflow]:
        group = re.match(r"^([xmas])([><])([0-9]+):([ARa-z]+)$", rule)
        if group == None:
            if rule == "A":
                new_constraints = update_constraints(constraints, history, None, None, None)
                total_combinations += compute_combinations(new_constraints)
            elif rule != "R":
                new_constraints = update_constraints(constraints, history, None, None, None)
                total_combinations += compute_accepted_combinations(rule, new_constraints)
        else:
            category = group[1]
            operation = group[2]
            value = int(group[3])
            new_workflow = group[4]

            new_constraints = update_constraints(constraints, history, category, operation, value)
            if new_workflow == 'A':
                total_combinations += compute_combinations(new_constraints)
            elif new_workflow != 'R':
                total_combinations += compute_accepted_combinations(new_workflow, new_constraints)
            history.append(rule)

    return total_combinations

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

# Computing accepted combinations
combinations = compute_accepted_combinations("in", {})
print("=====")
print(f"Accepted distinct combinations of ratings: {combinations:,} => {combinations}")

stop_timer(timer)
sys.exit(0)
