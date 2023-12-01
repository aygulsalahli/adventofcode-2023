with open("../input") as f:

    sum = 0
    lines = f.readlines()

    numbers = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }

    for line in lines:
        first = -1
        last = -1
        word = ""
        for char in line:
            if char.isnumeric():
                if first == -1:
                    first = char
                last = char
                word = ""
            else:
                word += char
                is_word = False

                # Check if the word contains a number
                for key in numbers:
                    if key in word:
                        is_word = True
                        break

                # If the word contains a number, then we need to reset the first and last
                if is_word:
                    if first == -1:
                        first = numbers[key]
                    last = numbers[key]

                    # Reset the word to begin from this character
                    word = char

        calibration_value = int(f"{first}{last}")
        sum += calibration_value

    print(f"sum of the calibration value: {sum}")
