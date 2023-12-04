with open("../input") as f:
    sum = 0
    lines = f.readlines()

    available = {"blue": 14, "red": 12, "green": 13}

    for line in lines:
        info, sets = line.replace("\n", "").split(": ")
        id = info.split(" ")[1]
        is_possible = True

        for set in sets.split("; "):
            for cube in set.split(", "):
                size, color = cube.split(" ")
                if int(size) > available[color]:
                    is_possible = False
                    break

        if is_possible:
            sum += int(id)

    print(f"Sum: {sum}")
