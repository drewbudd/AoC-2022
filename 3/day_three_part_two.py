'''Advent of Code 2022 Day Three'''


def item_to_priority(item: str) -> int:
    '''helper method that converts a char to corresponding priorty'''
    if len(item) != 1:
        return -1

    if item.isupper():
        return ord(item) - 38
    if item.islower():
        return ord(item) - 96
    return -1


def main():
    '''https://adventofcode.com/2022/day/3#part2'''
    with open('input.txt', 'r', encoding="utf8") as input_file:
        priority_total = 0
        while True:
            rucksack_one = input_file.readline()
            rucksack_two = input_file.readline()
            rucksack_three = input_file.readline()

            if not rucksack_one:
                break

            for item in rucksack_one:
                if (rucksack_two.count(item) > 0
                   and rucksack_three.count(item) > 0):
                    priority_total += item_to_priority(item)
                    break

        print(f'{priority_total}')


if __name__ == '__main__':
    main()
