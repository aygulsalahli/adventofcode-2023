with open("input") as f:
    lines = f.readlines()

    sum = 0
    for line in lines:
        stack = []
        numbers = [int(n) for n in line.strip().split(" ")]
        stack.append(numbers)

        while True:
            diff_array_between_consecutive_numbers = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
            stack.append(diff_array_between_consecutive_numbers)

            if all(v == 0 for v in diff_array_between_consecutive_numbers):
                break
            else:
                numbers = diff_array_between_consecutive_numbers

        last_number = 0
        while len(stack) > 0:
            processing_array = stack.pop()
            last_number = processing_array[0] - last_number

        sum += last_number

    print("Sum:", sum)





