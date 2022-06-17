import pygame as pg
from board import *
from piece import *
from utils.colors import *
import sys

class Game:
	def __init__(self, debug:bool=False):
		pg.init()
		self.WIDTH, self.HEIGHT = 600,600
		self.SCREEN = pg.display.set_mode((self.WIDTH, self.HEIGHT))
		self.FPS = 60
		self.CLOCK = pg.time.Clock()
		self.font = pg.font.SysFont('Consolas', 50)
		self.running = True
		self.board = Board()
		self.x_offset = self.WIDTH//2-self.board.width//2
		self.y_offset = self.HEIGHT//2-self.board.height//2
		self.moves = []
		self.selected_piece = None

	def draw(self, screen):
		screen.fill(BLACK)
		# print(pg.mouse.get_pos())
		pg.draw.rect(screen, L_SQUARE, pg.Rect(self.x_offset,self.y_offset,self.board.width,self.board.height))
		
		for i in range(len(self.board.board)):
			for j in range(len(self.board.board[i])):
				if j % 2 == 1 and i % 2 == 0 or j % 2 == 0  and i % 2 == 1:
					pg.draw.rect(screen, D_SQUARE, pg.Rect(self.x_offset + (j*self.board.square_size), self.y_offset + (i*self.board.square_size), self.board.square_size, self.board.square_size))
				

		for i in range(len(self.board.board)):
			for j in range(len(self.board.board[i])):
				if self.board.board[i][j] is not None:
					self.board.board[i][j].draw(screen, pg.mouse.get_pos())
					self.board.board[i][j].draw_moves(screen, pg.mouse.get_pos())
		pg.display.flip()

	def set_pieces(self):
		for i in range(8): 
			self.board.add_piece(Peon(False, (self.x_offset + (i*self.board.square_size), self.y_offset + (1*self.board.square_size)),(i,1)), (i,1))
			self.board.add_piece(Peon(True, (self.x_offset + (i*self.board.square_size), self.y_offset + (6*self.board.square_size)),(i,6)), (i,6))
		
	def handle_event(self, event):
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			for i in range(len(self.board.board)):
				for j in range(len(self.board.board[i])):

					if self.board.board[i][j] is not None:
						self.board.board[i][j].selected = False

						if self.board.board[i][j].hover:
							self.board.board[i][j].click(self.SCREEN)
							self.selected_piece = self.board.board[i][j]
							self.moves = self.board.board[i][j].moves
					
			for i in range(len(self.board.board)):
				for j in range(len(self.board.board[i])):
					if self.board.board[i][j] is None:
						for k in range(len(self.moves)):
							if self.selected_piece.selected_move == k and self.moves[k] == [i, j]:
								self.selected_piece.board_x = j
								self.selected_piece.board_y = i
								self.selected_piece.selected_move = -1





	def start(self):
		self.set_pieces()
		while self.running:
			self.CLOCK.tick(self.FPS)
			self.draw(self.SCREEN)
			for event in pg.event.get():
				self.handle_event(event)
