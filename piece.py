import os
import pygame as pg
from utils.colors import *

class Piece:
	def __init__(self):
		self.is_white = True
		self.x, self.y = 0,0
		self.board_pos = (0,0)
		self.board_x, self.board_y = self.board_pos
		self.pos = (self.x, self.y)
		self.texture = None
		self.rect = pg.Rect(self.pos, (64,64))
		self.moves = []
		self.moves_rect = []
		self.selected = False
		self.hover = False
		self.selection_circle = pg.Surface((64,64))
		self.selection_circle.set_colorkey(BLACK)
		self.selection_circle.set_alpha(128)
		self.selected_move = -1


	def draw(self, screen, mousepos):
		self.hover = False
		self.rect.x = (screen.get_size()[0]-512)//2 + (64 * self.board_x)
		self.rect.y = (screen.get_size()[1]-512)//2 + (64 * self.board_y)
		screen.blit(self.texture, (self.rect.x, self.rect.y))
		if self.rect.collidepoint(mousepos):
			self.hover = True
			pg.draw.circle(self.selection_circle, SELECT, (32,32), 16)
			screen.blit(self.selection_circle, (self.rect.x, self.rect.y))

# (screen.get_size()[0]-512)//2 + (64 * move[1]) , (screen.get_size()[1]-512)//2 + (64 * move[0])

	def draw_moves(self, screen, mousepos):
		self.selected_move = -1
		if self.selected:
			for move in self.moves:
				pg.draw.circle(self.selection_circle, SELECT, (32,32), 16)
				screen.blit(self.selection_circle, ((screen.get_size()[0]-512)//2 + (64 * move[1]) , (screen.get_size()[1]-512)//2 + (64 * move[0])))
			for i in range(len(self.moves_rect)):
				if self.moves_rect[i].collidepoint(mousepos):
					self.selected_move = i


	def click(self, screen):
		self.moves_rect = []
		print(self.board_x, self.board_y)
		self.selected = True

		if self.__str__() == 'bP': # Black Peon
			self.moves = [[self.board_y+1, self.board_x]]
			if self.board_y == 1:
				self.moves += [[self.board_y+2, self.board_x]]
		elif self.__str__() == 'wP': # White Peon
			self.moves = [[self.board_y-1, self.board_x]]
			if self.board_y == 6:
				self.moves += [[self.board_y-2, self.board_x]]
		elif self.__str__()[1] == 'K': # Knight
			pass

		for move in self.moves:
			self.moves_rect += [pg.Rect(((screen.get_size()[0]-512)//2 + (64 * move[1]) , (screen.get_size()[1]-512)//2 + (64 * move[0])), (64,64))]
		print(self.moves_rect)
		


class Peon(Piece):
	def __init__(self, is_white, pos, board_pos):
		super().__init__()
		self.is_white = is_white
		self.x, self.y = pos[1], pos[0]
		self.board_x, self.board_y = board_pos[0], board_pos[1]
		self.pos = pos
		self.rect = pg.Rect(self.pos, (64,64))
		if is_white:
			self.texture = pg.image.load(os.path.join('assets', 'img', 'wPeon.png'))
			self.moves = None
		else:
			self.texture = pg.image.load(os.path.join('assets', 'img', 'bPeon.png'))


	def __str__(self):
		if self.is_white:
			return 'wP'
		return 'bP'