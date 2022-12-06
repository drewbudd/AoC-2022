'''Advent of Code 2022 Day Five'''


def prepare_stacks():
    '''helper method that prepares part of the problem input'''
    return [
        ['R', 'N', 'P', 'G'],
        ['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'],
        ['T', 'D', 'B', 'M', 'N', 'L'],
        ['R', 'V', 'P', 'S', 'B'],
        ['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H'],
        ['W', 'Q', 'S', 'C', 'D', 'B', 'J'],
        ['F', 'Q', 'L'],
        ['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'],
        ['L', 'P', 'B', 'V', 'M', 'J', 'F']
    ]


def main():
    '''https://adventofcode.com/2022/day/5'''
    with open('input.txt', 'r', encoding="utf8") as input_file:
        lines = input_file.readlines()

        stacks = prepare_stacks()

        for line in lines:
            line = line.split()

            order = int(line[1])
            source = int(line[3]) - 1
            target = int(line[5]) - 1

            while order > 0:
                stacks[target].append(stacks[source].pop())
                order -= 1

        for stack in stacks:
            print(f'{stack[-1]}')


if __name__ == '__main__':
    main()
