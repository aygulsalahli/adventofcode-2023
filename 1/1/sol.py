with open("../input") as f:

    sum = 0
    lines = f.readlines()

    for line in lines:
        first = -1
        last = -1
        for char in line:
            if char.isnumeric():
                if first == -1:
                    first = char
                last = char

        calibration_value = int(f"{first}{last}")
        sum += calibration_value

    print(f"sum of the calibration value: {sum}")
