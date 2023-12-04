with open("../input") as f:
    schema = []
    lines = f.readlines()
    sum = 0
    for index, line in enumerate(lines):
        line = line.rstrip()
        schema.append([x for x in line])

    rows = len(schema)
    columns = len(schema[0])

    SYMBOLS = "*/-+&=@$%#"

    for row in range(rows):
        num = ""
        is_adjacent = False
        for column in range(columns):
            if not schema[row][column].isnumeric():
                if num != "" and is_adjacent:
                    # print(f"Adding {num} to sum {sum}")
                    sum += int(num)
                num = ""
                is_adjacent = False
                continue

            num += schema[row][column]

            if column == columns - 1:
                if num != "" and is_adjacent:
                    # print(f"Adding {num} to sum {sum}")
                    sum += int(num)
                    num = ""
                    is_adjacent = False

            if num != "" and is_adjacent:
                # print(f"moving on as {num} is adjacent")
                continue

            # top left
            if row > 0 and column > 0:
                if schema[row - 1][column - 1] in SYMBOLS:
                    is_adjacent = True

            # top
            if row > 0:
                if schema[row - 1][column] in SYMBOLS:
                    is_adjacent = True

            # top right
            if row > 0 and column < columns - 1:
                if schema[row - 1][column + 1] in SYMBOLS:
                    is_adjacent = True

            # left
            if column > 0:
                if schema[row][column - 1] in SYMBOLS:
                    is_adjacent = True

            # right
            if column < columns - 1:
                if schema[row][column + 1] in SYMBOLS:
                    is_adjacent = True

            # bottom left
            if row < rows - 1 and column > 0:
                if schema[row + 1][column - 1] in SYMBOLS:
                    is_adjacent = True

            # bottom
            if row < rows - 1:
                if schema[row + 1][column] in SYMBOLS:
                    is_adjacent = True

            # bottom right
            if row < rows - 1 and column < columns - 1:
                if schema[row + 1][column + 1] in SYMBOLS:
                    is_adjacent = True

    print(sum)
