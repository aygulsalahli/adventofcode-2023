with open("input") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip().replace("\n", "")

        if line.startswith("Time:"):
            time = [int(x) for x in line.split(" ")[1:] if x != ""]

        if line.startswith("Distance:"):
            distance = [int(x) for x in line.split(" ")[1:] if x != ""]

    total = 1
    for i in range(len(time)):
        min = 1

        while min * (time[i] - min) <= distance[i]:
            min += 1

        max = time[i] - 1
        while max * (time[i] - max) <= distance[i]:
            max -= 1

        times = max - min + 1
        total *= times

    print(f"Total: {total}")


