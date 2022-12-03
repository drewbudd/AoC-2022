def itemToPriority(item: str) -> int:
    if len(item) != 1:
        return -1

    if item.isupper():
        return ord(item) - 38
    elif item.islower():
        return ord(item) - 96
    else:
        return -1


def main():
    input = open('input.txt', 'r')
    lines = input.readlines()

    priority_total = 0

    for line in lines:
        rucksack_one, rucksack_two = line[:len(line)//2], line[len(line)//2:]

        for item in rucksack_one:
            if rucksack_two.count(item) > 0:
                priority_total += itemToPriority(item)
                break

    print(f'{priority_total}')


if __name__ == '__main__':
    main()
