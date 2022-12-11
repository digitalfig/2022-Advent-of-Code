## Advent of Code 2022 -- Day XX:
''' <description>
'''

def import_file( test ):
	if test.upper() == 'TEST':
		fn = 'test.txt'
	else:
		fn = 'input.txt'
	with open(fn) as f:
		lines = f.read().splitlines()
	return lines

lines = import_file("Test")