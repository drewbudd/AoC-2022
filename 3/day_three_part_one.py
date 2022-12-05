'''Advent of Code 2022 Day Three'''


def item_to_priority(item: str) -> int:
    '''helper method that converts a char to corresponding priorty'''
    if len(item) != 1:
        return -1

    if item.isupper():
        return ord(item) - 38
    elif item.islower():
        return ord(item) - 96
    else:
        return -1


def main():
    '''https://adventofcode.com/2022/day/3'''
    with open('input.txt', 'r', encoding="utf8") as input_file:
        lines = input_file.readlines()

        priority_total = 0

        for line in lines:
            rucksack_one, rucksack_two = (line[:len(line)//2],
                                          line[len(line)//2:])

            for item in rucksack_one:
                if rucksack_two.count(item) > 0:
                    priority_total += item_to_priority(item)
                    break

        print(f'{priority_total}')


if __name__ == '__main__':
    main()
