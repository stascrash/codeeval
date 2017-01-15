# https://www.codeeval.com/open_challenges/87/
import sys

def set_col(*args):
	i, x = map(int, args)
	for j in range(len(BOARD[i])):
		BOARD[i][j] = x


def set_row(*args):
	j, x = map(int, args)
	for i in range(len(BOARD)):
		BOARD[i][j] = x

def query_col(*args):
	i = int(args[0])
	print(sum(BOARD[i]))

def query_row(*args):
	j = int(args[0])
	vals = list()
	for i in range(len(BOARD)):
		vals.append(BOARD[i][j])
	print(sum(vals))


def build_board(m,n):
	board = list()
	for i in range(m):
		col = list()
		for j in range(n):
			col.append(0)
		board.append(col)
	return board

if __name__ == '__main__':
	BOARD_CONTROL = dict(SetCol=set_col, SetRow=set_row, QueryCol=query_col, QueryRow=query_row)
	BOARD = build_board(256, 256)

	test_cases = open(sys.argv[1], 'r')
	# test_cases = open('query_board.txt', 'r')
	test_lines = (line.rstrip() for line in test_cases)

	for test in test_lines:
		try:
			operation, param1, param2 = test.split(' ')
		except ValueError:
			operation, param1 = test.split(' ')
			param2 = None
		BOARD_CONTROL[operation](param1, param2)
	test_cases.close()






