## Advent of Code 2022 -- Day 02:
'''Day 2: Rock Paper Scissors

The input file is your full tournament, and has each match on a line. Your opponent's hand-shape is first (A, B or C) and your response is represented in second (X, Y or Z). In each match you score 1 for throwing Rock, 2 for Paper or 3 for Sissors, and you also score an added 6 for winning, 3 for a draw or 0 for losing the match.
'''

## READ INPUT FILE:
def import_file( test ):
	if test.upper() == 'TEST':
		fn = 'test.txt'
	else:
		fn = 'input.txt'
	with open(fn) as f:
		lines = f.read().splitlines()
	return [l.replace(" ", "") for l in lines]

lines = import_file("T")
#print(lines)

def score_it(lines, score_array):
	score = 0
	for l in lines:
		score += 1 + score_array.index(l)
	return score

'''PART 1: Your response X, Y or Z represents respectively the Rock, Paper or Scissors hand-shape you show in each match.'''
#Rock    =  A, X  =  1
#Paper   =  B, Y  =  2
#Sissors =  C, Z  =  3
#win =  {"AY": 6 + 2, "BZ": 6 + 3, "CX": 6 + 1}
#draw = {"AX": 3 + 1, "BY": 3 + 2, "CZ": 3 + 3}
#lose = {"AZ": 0 + 3, "BX": 0 + 1, "CY": 0 + 2}
score_array = ["BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]
score = score_it(lines, score_array)
print("Score Part 1:", score)

'''PART 2: Your response (X, Y or Z) represents if you lose, draw or win the match, respectively.'''
#lose = X = 0 +    "AX": 3, "BX": 1, "CX": 2
#draw = Y = 3 +    "AY": 1, "BY": 2, "CY": 3
#win  = Z = 6 +    "AZ": 2, "BZ": 3, "CZ": 1
score_array = ["BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]
score = score_it(lines, score_array)
print("Score Part 2:", score)
