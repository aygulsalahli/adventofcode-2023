from math import lcm

with open("input") as f:
    lines = f.readlines()

    lr_instructions = ""
    network = {}
    starting_points = []

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

        if key.endswith("A"):
            starting_points.append(key)

    current_point_in_instructions = 0
    cycles = []
    for starting_point in starting_points:
        steps = 0
        while True:
            position = lr_instructions[current_point_in_instructions % len(lr_instructions)]
            index = 0 if position == "L" else 1
            starting_point = network[starting_point][index]
            current_point_in_instructions += 1
            steps += 1
            if starting_point.endswith("Z"):
                cycles.append(steps)
                break

    total = lcm(*cycles)

    print(f"Total steps: {total}")


