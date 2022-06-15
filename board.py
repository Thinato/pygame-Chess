class Board:
	def __init__(self):
		self.board = [[None for x in range(8)] for y in range(8)]
		self.width, self.height = 512, 512
		self.square_size = 64

	def add_piece(self, piece, pos):
		self.board[pos[1]][pos[0]] = piece


	def __str__(self):
		res = ""
		for i in range(len(self.board)):
			res += '\n'
			for j in range(len(self.board[i])):
				if self.board[i][j] is None:
					res += '  ' + ' | '
					continue
				res += str(self.board[i][j]) + ' | '
		return res