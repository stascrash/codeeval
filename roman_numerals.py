# https://www.codeeval.com/open_challenges/106/
import sys
from collections import namedtuple
test_cases = open(sys.argv[1], 'r')
# test_cases = open('roman_numerals.txt', 'r')
test_lines = (line.rstrip() for line in test_cases)


def num_to_components(num):
	num_comp = namedtuple('NumComponents', ('thousands', 'hundreds', 'tens', 'singles'))
	thousands = int(num/1000)
	hundreds = int((num - 1000*thousands)/100)
	tens = int((num - 1000*thousands - 100*hundreds)/10)
	singles = int(num - 1000*thousands - 100*hundreds - 10*tens)
	return num_comp(thousands=thousands, hundreds=hundreds, tens=tens, singles=singles)

def to_roman(num_components):
	r_thousands = 'M'*num_components.thousands
	r_hundreds = ''
	r_tens = ''
	r_singles = ''
	# for hundreds
	if num_components.hundreds == 4:
		r_hundreds = 'CD'
	elif num_components.hundreds == 9:
		r_hundreds = 'CM'
	elif num_components.hundreds == 5:
		r_hundreds = 'D'
	elif num_components.hundreds <= 3:
		r_hundreds = 'C'*num_components.hundreds
	elif num_components.hundreds in range(6, 9):
		r_hundreds = 'D' + 'C' * (num_components.hundreds - 5)

	# for Tens
	if num_components.tens == 4:
		r_tens = 'XL'
	elif num_components.tens == 9:
		r_tens = 'XC'
	elif num_components.tens == 5:
		r_tens = 'L'
	elif num_components.tens <= 3:
		r_tens = 'X'*num_components.tens
	elif num_components.tens in range(6, 9):
		r_tens = 'L' + 'X' * (num_components.tens - 5)

	# for singles
	if num_components.singles == 4:
		r_singles = 'IV'
	elif num_components.singles == 9:
		r_singles = 'IX'
	elif num_components.singles == 5:
		r_singles = 'V'
	elif num_components.singles <= 3:
		r_singles = 'I'*num_components.singles
	elif num_components.singles in range(6, 9):
		r_singles = 'V' + 'I' * (num_components.singles - 5)

	roman_num = r_thousands + r_hundreds + r_tens + r_singles
	print(roman_num)


if __name__ == '__main__':
	for test in test_lines:
		components = num_to_components(int(test))
		to_roman(components)
	test_cases.close()
