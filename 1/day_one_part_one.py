input = open('input.txt', 'r')
lines = input.readlines()

best_stocked_elf = (0, 0)
current_elf = (1, 0)

for line in lines:
    if line.strip() == '':
        if current_elf[1] > best_stocked_elf[1]:
            best_stocked_elf = current_elf
        current_elf = (current_elf[0] + 1, 0)
    else:
        current_elf = (current_elf[0], current_elf[1] + int(line))

print(f'Elf #{best_stocked_elf[0]} is carrying {best_stocked_elf[1]} calories')