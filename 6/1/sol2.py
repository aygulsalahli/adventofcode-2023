with open("input") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip().replace("\n", "")

        if line.startswith("Time:"):
            time = int(line.replace("Time: ", "").replace(" ", ""))
            print(f"Time: {time}")

        if line.startswith("Distance:"):
            distance = int(line.replace("Distance: ", "").replace(" ", ""))
            print(f"Distance: {distance}")

    min = 1
    while min * (time - min) <= distance:
        min += 1
    max = time - 1
    while max * (time - max) <= distance:
        max -= 1

    total = max - min + 1

    print(f"Total: {total}")


