import pygame as pg
from settings import *
from move_validation import MoveValidation
import sys
import os
# D:\__proj\games\pygame_test\g6_2_player_chess\game_assets\graphics\chess_peices\0\pawn.png
class Level():
	def __init__(self):
		self.screen = pg.display.get_surface()
		self.chess_board = pg.Rect(chess_board_pos[0],chess_board_pos[1], 
									chess_board_size[0],chess_board_size[1])
		self.tile_selected = None
		self.chess_piece_state = piece_init_pos.copy()
		self.chess_pieces = chess_pieces
		self.import_assets()
		self.validation = MoveValidation()
		self.old_state = None
		self.pause = False
		self.pawn_tobe_promoted = False
		self.color_of_pawn = None
		self.pos_of_pawn = None

	def import_assets(self):
		for chess_piece in self.chess_pieces.keys():
			rel_animation_path_0 = os.path.join('game_assets','graphics','chess_pieces','0',chess_piece+'.png')
			rel_animation_path_1 = os.path.join('game_assets','graphics','chess_pieces','1',chess_piece+'.png')
			self.chess_pieces[chess_piece] = [pg.image.load(rel_animation_path_0).convert_alpha(),
												pg.image.load(rel_animation_path_1).convert_alpha()]

	def draw_tiles(self):
		i = 0
		while i<len(tile_layout):
			j = 0
			while j < len(tile_layout[i]):
				 
				tile_pos = (play_board_pos[0]+play_board_size[0]*j/8,
									play_board_pos[1]+play_board_size[0]*i/8)
				tile_rect = pg.Rect(tile_pos[0],tile_pos[1],
									play_board_size[0]/8+1,play_board_size[1]/8+1)
				if tile_layout[i][j]==1:
					if (i,j) in self.validation.valid_tiiles:
						pg.draw.rect(self.screen, dark_tile_color_h, tile_rect)
					else:
						pg.draw.rect(self.screen, dark_tile_color, tile_rect)
				else:
					if (i,j) in self.validation.valid_tiiles:
						pg.draw.rect(self.screen, light_tile_color_h, tile_rect)
					else:
						pg.draw.rect(self.screen, light_tile_color, tile_rect)
				j += 1
			i += 1

	def draw_borders(self):
		# draw inner border
		# top
		inner_border_rect_t = pg.Rect(play_board_pos[0],play_board_pos[1],
											play_board_size[0],inner_borders_thickness)
		pg.draw.rect(self.screen, 'black', inner_border_rect_t)
		# bot
		inner_border_rect_b = pg.Rect(play_board_pos[0],play_board_pos[1]+play_board_size[1],
											play_board_size[0],inner_borders_thickness)
		pg.draw.rect(self.screen, 'black', inner_border_rect_b)
		# right
		inner_border_rect_r = pg.Rect(play_board_pos[0]+play_board_size[0],play_board_pos[1],
											inner_borders_thickness, play_board_size[1])
		pg.draw.rect(self.screen, 'black', inner_border_rect_r)
		# left
		inner_border_rect_l = pg.Rect(play_board_pos[0]-inner_borders_thickness,play_board_pos[1],
											inner_borders_thickness, play_board_size[1])
		pg.draw.rect(self.screen, 'black', inner_border_rect_l)

	def draw_markers(self):
		font = pg.font.SysFont(None, 24)
		text_surface = font.render('TO RESTART GAME PRESS "F2"!', True, restart_text)
		text_rect = text_surface.get_rect()
		text_rect.topleft = (5,5)
		self.screen.blit(text_surface, text_rect)
		i = 0
		font = pg.font.SysFont(None, 36)
		while i < len(letters):
			text_surface = font.render(letters[i], True, BLACK)
			text_rect = text_surface.get_rect()
			x1 = chess_board_pos[0] + 12
			x2 = chess_board_pos[0] + chess_board_size[0] - 12
			y = play_board_pos[1] + play_board_size[1] - play_board_size[0]*(i/8+ 1/16)
			text_rect.center = (x1,y)
			self.screen.blit(text_surface, text_rect)
			text_rect.center = (x2,y)
			self.screen.blit(text_surface, text_rect)



			text_surface = font.render(str(i+1), True, BLACK)
			text_rect = text_surface.get_rect()
			y1 = chess_board_pos[1] + 12
			y2 = chess_board_pos[1] + chess_board_size[1] - 12
			x = play_board_pos[0] + play_board_size[0] - play_board_size[0]*(i/8+ 1/16)
			text_rect.center = (x,y1)
			self.screen.blit(text_surface, text_rect)
			text_rect.center = (x,y2)
			self.screen.blit(text_surface, text_rect)

			i += 1
	
	def draw_peice_selection(self,color):
		i = 0
		for chess_piece, path in self.chess_pieces.items():
			if chess_piece == 'king':
				continue
			chess_piece_pos = (play_board_pos[0]+play_board_size[0]*1.2,
									play_board_pos[1]+play_board_size[0]*(i/8+ 1/16))

			piece_img = path[int(color)]
			pos_rect = piece_img.get_rect(center = chess_piece_pos)
			self.screen.blit(piece_img, pos_rect)
			pg.draw.rect(self.screen, chess_piece_bg, pos_rect, 2)
			i += 1

	def select_piece_to_replace(self, click_pos):
		x1 = play_board_pos[0]+play_board_size[0]*1.2 - play_board_size[0]*(1/16) - 10
		x2 = play_board_pos[0]+play_board_size[0]*1.2 + play_board_size[0]*(1/16) + 10
		if x1 < click_pos[0] < x2:
			y =	click_pos[1] - play_board_pos[1]
			val = y//(play_board_size[1]/8)
			if val < 5:
				self.chess_piece_state[self.pos_of_pawn[0]][self.pos_of_pawn[1]] = self.color_of_pawn + '_' + selct_piece[val]
				self.pos_of_pawn = None
				self.pawn_tobe_promoted = False
				self.color_of_pawn = None

	def cal_piece_move(self):
		keys = pg.key.get_pressed()
		for event in pg.event.get():
			if event.type == pg.QUIT:
				print('QUITING')
				pg.quit()
				sys.exit()

			if event.type == pg.MOUSEBUTTONDOWN and not self.pause:
				print('drawing')
				# Check if the event is a mouse button click
				if event.button == 1:  # Left mouse button clicked
					click_pos = pg.mouse.get_pos()  # Get the mouse click position
					j = int((click_pos[0]-play_board_pos[0])//(play_board_size[0]/8))
					i = int((click_pos[1]-play_board_pos[1])//(play_board_size[1]/8))

					if self.pawn_tobe_promoted:
						self.select_piece_to_replace(click_pos)
						return None
  
					if i>7 or i<0 or j>7 or j<0:
						return None

					if not self.tile_selected and self.chess_piece_state[i][j] != 0:
						self.validation.calculate_valid_moves(self.chess_piece_state,(i,j))
						if self.validation.can_select:
							self.tile_selected = (i,j)

					elif self.tile_selected:
						if (i,j) in self.validation.valid_tiiles:
							self.chess_piece_state[i][j] = self.chess_piece_state[self.tile_selected[0]][self.tile_selected[1]]
							self.chess_piece_state[self.tile_selected[0]][self.tile_selected[1]] = 0
							if self.chess_piece_state[i][j].split('_')[1]=='pawn' and i in [0,7]:
								self.pawn_tobe_promoted = True
								self.color_of_pawn = self.chess_piece_state[i][j].split('_')[0]
								self.pos_of_pawn = (i,j)
							self.tile_selected = None
							self.validation.change_turn_color()
							self.validation.king_check = False
							self.validation.valid_tiiles = []
						else:
							print('not a valid move')
							if self.chess_piece_state[i][j] != 0:
								self.validation.calculate_valid_moves(self.chess_piece_state,(i,j))
								if self.validation.can_select:
									self.tile_selected = (i,j)

	def draw_chess_peices(self):
		i = 0
		while i<len(self.chess_piece_state):
			j = 0
			while j < len(self.chess_piece_state[i]):
				if self.chess_piece_state[i][j] == 0:
					pass
				else:
					color, piece = self.chess_piece_state[i][j].split('_')

					chess_piece_pos = (play_board_pos[0]+play_board_size[0]*(j/8+ 1/16),
											play_board_pos[1]+play_board_size[0]*(i/8+ 1/16))

					piece_img = self.chess_pieces[piece][int(color)]
					pos_rect = piece_img.get_rect(center = chess_piece_pos)
					self.screen.blit(piece_img, pos_rect)

				j += 1
			i += 1

	def draw_chess_board(self):
		pg.draw.rect(self.screen, chess_board_color, self.chess_board)
		self.draw_tiles()
		self.draw_borders()
		self.draw_markers()
		self.cal_piece_move()
		self.draw_chess_peices()
		if self.pawn_tobe_promoted:
			self.draw_peice_selection(self.color_of_pawn)

	def draw_background(self):
		self.screen.fill(back_ground_color)

	def draw(self):
		self.draw_background()
		self.draw_chess_board()

	def run(self,dt):
		self.draw()