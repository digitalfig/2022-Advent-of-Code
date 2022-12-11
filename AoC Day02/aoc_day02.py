## Advent of Code 2022 -- Day 02:
## Day 2: Rock Paper Scissors

def import_file( test ):
	if test.upper() == 'TEST':
		fn = 'test.txt'
	else:
		fn = 'input.txt'
	with open(fn) as f:
		lines = f.read().splitlines()
	return [l.replace(" ", "") for l in lines]

lines = import_file("T")
print(lines)

def score_it(lines, score_array):
	score = 0
	for l in lines:
		score += 1 + score_array.index(l)
	return score

# PART 1: --------------
#Rock    =  A, X  =  1
#Paper   =  B, Y  =  2
#Sissors =  C, Z  =  3
#win =  ["AY": 6 + 2, "BZ": 6 + 3, "CX": 6 + 1]
#draw = ["AX": 3 + 1, "BY": 3 + 2, "CZ": 3 + 3]
#lose = ["AZ": 0 + 3, "BX": 0 + 1, "CY": 0 + 2]
score_array = ["BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]
score = score_it(lines, score_array)
print("Score Part 1:", score)

# PART 2: ---------------
#lose = X = 0 +    "AX": 3, "BX": 1, "CX": 2
#draw = Y = 3 +    "AY": 1, "BY": 2, "CY": 3
#win  = Z = 6 +    "AZ": 2, "BZ": 3, "CZ": 1
score_array = ["BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]
score = score_it(lines, score_array)
print("Score Part 2:", score)


