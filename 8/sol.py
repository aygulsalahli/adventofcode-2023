from itertools import cycle
import re


with open("input") as f:
    lines = f.readlines()

    lr_instructions = ""
    network = {}

    for line in lines:
        line = line.replace(" ", "").replace("\n", "")
        if not lr_instructions:
            lr_instructions = line
            continue

        if not line:
            continue

        key, lr = line.strip().split("=")
        left, right = lr.replace("(", "").replace(")", "").split(",")
        network[key] = (left, right)

    current_point_in_map = "AAA"
    destination = "ZZZ"
    current_point_in_instructions = 0
    steps = 0
    while current_point_in_map != destination:
        position = lr_instructions[current_point_in_instructions % len(lr_instructions)]
        index = 0 if position == "L" else 1
        current_point_in_map = network[current_point_in_map][index]
        current_point_in_instructions += 1
        steps += 1

    print(f"Steps: {steps}")


