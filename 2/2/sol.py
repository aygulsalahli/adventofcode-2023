with open("../input") as f:
    sum = 0
    lines = f.readlines()

    for line in lines:
        possible_set = {"blue": 0, "red": 0, "green": 0}
        info, sets = line.replace("\n", "").split(": ")
        id = info.split(" ")[1]

        for set in sets.split("; "):
            for cube in set.split(", "):
                size, color = cube.split(" ")
                if int(size) > possible_set[color]:
                    possible_set[color] = int(size)

        power = possible_set["blue"] * possible_set["red"] * possible_set["green"]
        sum += power

    print(f"Sum: {sum}")
