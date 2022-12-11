## Advent of Code 2022 -- Day 01:
## Day 1: Calorie Counting

## READ FILE:

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


## PART 1 ------------ :

elf_calories = [0]
elf_index = 0
for l in lines:
	if l == "":
		elf_calories.append(0)
		elf_index += 1
	else:
		elf_calories[elf_index] += int(l)
print("Max calories held:", max(elf_calories))


## PART 2 ------------ :

elf_calories.sort(reverse = True)
#print(elf_calories)
top3 = elf_calories[0] + elf_calories[1] + elf_calories[2]
print("Top 3 calories totaled:", top3)
