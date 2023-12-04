with open("../input") as f:
    sum = 0
    lines = f.readlines()

    copies = {}
    for line in lines:
        info, sets = line.replace("\n", "").split(": ")

        id = int(info.split(" ")[-1])
        available = copies.get(id, 0) + 1
        winners = [x for x in sets.split("|")[0].strip().split(" ") if x]
        elf_numbers = [x for x in sets.split("|")[1].strip().split(" ") if x]

        matching_numbers = 0
        for elf_number in elf_numbers:
            if elf_number in winners:
                matching_numbers += 1

        for mn in range(id + 1, id + matching_numbers + 1):
            if mn in copies:
                copies[mn] += available
            else:
                copies[mn] = available

        sum += available

    print(sum)
