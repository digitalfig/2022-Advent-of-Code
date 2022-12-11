## Advent of Code 2022 -- Day 01:
'''Day 1: Calorie Counting

Elves carry various food items of different calories. The input file lists the calories per food item on each line and blank lines seperate groups for each elf's carried food supply.
'''

## READ INPUT FILE:
def import_file( test ):
	if test.upper() == 'TEST':
		fn = 'test.txt'
	else:
		fn = 'input.txt'
	with open(fn) as f:
		lines = f.read().splitlines()
	return lines

lines = import_file("I")
#print(lines)


'''Part 1: How many calories is the elf with the most calories hold?'''
elf_calories = [0]
elf_index = 0
for l in lines:
	if l == "":
		elf_calories.append(0)
		elf_index += 1
	else:
		elf_calories[elf_index] += int(l)
print("Max calories held:", max(elf_calories))


'''Part 2: Total the top 3 elf calorie holders together.'''
elf_calories.sort(reverse = True)
#print(elf_calories)
top3 = elf_calories[0] + elf_calories[1] + elf_calories[2]
print("Top 3 calories totaled:", top3)
