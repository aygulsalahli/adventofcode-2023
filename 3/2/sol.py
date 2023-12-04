with open("../input") as f:
    schema = []
    lines = f.readlines()
    sum = 0
    for index, line in enumerate(lines):
        line = line.rstrip()
        schema.append([x for x in line])

    rows = len(schema)
    columns = len(schema[0])

    for row in range(rows):
        num = ""
        is_adjacent = False
        for column in range(columns):
            numbers = []
            if schema[row][column] != "*":
                continue

            skip_top = False
            skip_top_right = False
            # top left
            if row > 0 and column > 0:
                if schema[row - 1][column - 1].isnumeric():
                    top_left = schema[row - 1][column - 1]
                    r = row - 1
                    c = column - 2
                    while c >= 0 and schema[r][c].isnumeric():
                        top_left = schema[r][c] + top_left
                        c -= 1
                    c = column
                    while c < columns and schema[r][c].isnumeric():
                        top_left += schema[r][c]
                        skip_top = True
                        c += 1
                    numbers.append(int(top_left))

            # top
            if row > 0 and not skip_top:
                if schema[row - 1][column].isnumeric():
                    top = schema[row - 1][column]
                    r = row - 1
                    c = column - 1
                    while c >= 0 and schema[r][c].isnumeric():
                        top = schema[r][c] + top
                        c -= 1
                    c = column + 1
                    while c < columns and schema[r][c].isnumeric():
                        top += schema[r][c]
                        skip_top_right = True
                        c += 1
                    numbers.append(int(top))

            # top right
            if row > 0 and column < columns - 1 and not skip_top and not skip_top_right:
                if schema[row - 1][column + 1].isnumeric():
                    top_right = schema[row - 1][column + 1]
                    r = row - 1
                    c = column
                    while c >= 0 and schema[r][c].isnumeric():
                        top_right = schema[r][c] + top_right
                        c -= 1
                    c = column + 2
                    while c < columns and schema[r][c].isnumeric():
                        top_right += schema[r][c]
                        c += 1
                    numbers.append(int(top_right))

            # left
            if column > 0:
                if schema[row][column - 1].isnumeric():
                    left = schema[row][column - 1]
                    r = row
                    c = column - 2
                    while c >= 0 and schema[r][c].isnumeric():
                        left = schema[r][c] + left
                        c -= 1
                    c = column
                    while c < columns and schema[r][c].isnumeric():
                        left += schema[r][c]
                        c += 1
                    numbers.append(int(left))

            # right
            if column < columns - 1:
                if schema[row][column + 1].isnumeric():
                    right = schema[row][column + 1]
                    r = row
                    c = column
                    while c >= 0 and schema[r][c].isnumeric():
                        right = schema[r][c] + right
                        c -= 1
                    c = column + 2
                    while c < columns and schema[r][c].isnumeric():
                        right += schema[r][c]
                        c += 1
                    numbers.append(int(right))

            skip_bottom = False
            skip_bottom_right = False

            # bottom left
            if row < rows - 1 and column > 0:
                if schema[row + 1][column - 1].isnumeric():
                    bottom_left = schema[row + 1][column - 1]
                    r = row + 1
                    c = column - 2
                    while c >= 0 and schema[r][c].isnumeric():
                        bottom_left = schema[r][c] + bottom_left
                        c -= 1
                    c = column
                    while c < columns and schema[r][c].isnumeric():
                        bottom_left += schema[r][c]
                        skip_bottom = True
                        c += 1
                    numbers.append(int(bottom_left))

            # bottom
            if row < rows - 1 and not skip_bottom:
                if schema[row + 1][column].isnumeric():
                    bottom = schema[row + 1][column]
                    r = row + 1
                    c = column - 1
                    while c >= 0 and schema[r][c].isnumeric():
                        bottom = schema[r][c] + bottom
                        c -= 1
                    c = column + 1
                    while c < columns and schema[r][c].isnumeric():
                        bottom += schema[r][c]
                        skip_bottom_right = True
                        c += 1
                    numbers.append(int(bottom))

            # bottom right
            if (
                row < rows - 1
                and column < columns - 1
                and not skip_bottom
                and not skip_bottom_right
            ):
                if schema[row + 1][column + 1].isnumeric():
                    bottom_right = schema[row + 1][column + 1]
                    r = row + 1
                    c = column
                    while c >= 0 and schema[r][c].isnumeric():
                        bottom_right = schema[r][c] + bottom_right
                        c -= 1
                    c = column + 2
                    while c < columns and schema[r][c].isnumeric():
                        bottom_right += schema[r][c]
                        c += 1
                    numbers.append(int(bottom_right))

            if len(numbers) == 2:
                sum += numbers[0] * numbers[1]

    print(sum)
