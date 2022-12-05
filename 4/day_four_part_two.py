'''Advent of Code 2022 Day Four'''

def main():
    '''https://adventofcode.com/2022/day/4#part2'''
    with open('input.txt', 'r', encoding="utf8") as input_file:
        lines = input_file.readlines()

        total_overlaps = 0

        for line in lines:
            assignment_one, assignment_two = line.strip().split(',')
            assignment_one = assignment_one.split('-')
            assignment_two = assignment_two.split('-')

            set_assignment_one = set(range(int(assignment_one[0]), int(assignment_one[1]) + 1))
            set_assignment_two = set(range(int(assignment_two[0]), int(assignment_two[1]) + 1))

            if len(set_assignment_one.intersection(set_assignment_two)) > 0:
                total_overlaps += 1
        print(f'Total overlaps={total_overlaps}')


if __name__ == '__main__':
    main()
