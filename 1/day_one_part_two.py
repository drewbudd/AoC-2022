def carriedCalories(elf):
    return elf[0]

def main():
    input = open('input.txt', 'r')
    lines = input.readlines()

    current_elf = (0, 1)
    top_three_elves = []

    for line in lines:
        if line.strip() == '':
            top_three_elves.append(current_elf)
            if len(top_three_elves) > 3:
                top_three_elves.sort(reverse=True, key=carriedCalories)
                top_three_elves.pop(3)
            current_elf = (0, current_elf[1] + 1)
        else:
            current_elf = (current_elf[0] + int(line), current_elf[1])

    top_three_elves_calories = top_three_elves[0][0] + top_three_elves[1][0] + top_three_elves[2][0]

    print(f'The top 3 elves are carrying {top_three_elves_calories} calories')

if __name__ == '__main__':
    main()