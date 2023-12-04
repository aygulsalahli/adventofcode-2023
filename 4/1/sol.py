with open("../input") as f:
    sum = 0
    lines = f.readlines()


    for line in lines:
        info, sets = line.replace("\n", "").split(": ")

        winners = [x for x in sets.split("|")[0].strip().split(" ") if x]
        elf_numbers =[x for x in sets.split("|")[1].strip().split(" ") if x]

        point = 0
        for elf_number in elf_numbers:
            if elf_number in winners:
                if point == 0:
                    point = 1
                else:
                    point *= 2

        sum += point

    print(sum)
