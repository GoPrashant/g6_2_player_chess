import pygame as pg

from settings import *


class MoveValidation():
	def __init__(self):
		self.chase_pieces = chess_pieces
		self.turn_color = '0'
		self.can_select = False
		self.valid_tiiles = []
		self.king_check = False
		self.check_from = None
	
	############ for PAWN ################
	def call_pawn(self, tile_selected, chess_piece_state, king = False):
		if self.turn_color == '0':
			if tile_selected[0] == 6:
				if chess_piece_state[tile_selected[0]-1][tile_selected[1]] == 0:
					self.valid_tiiles += [(tile_selected[0]-1,tile_selected[1])]
					if chess_piece_state[tile_selected[0]-2][tile_selected[1]] == 0:
						self.valid_tiiles += [(tile_selected[0]-2,tile_selected[1])]
			else:
				if chess_piece_state[tile_selected[0]-1][tile_selected[1]] == 0:
					self.valid_tiiles = [(tile_selected[0]-1,tile_selected[1])]
			
			if king:
				self.valid_tiiles += [(tile_selected[0]-1,tile_selected[1]+1)]
				self.valid_tiiles += [(tile_selected[0]-1,tile_selected[1]-1)]
			else:
				if tile_selected[1]<7 and chess_piece_state[tile_selected[0]-1][tile_selected[1]+1] != 0 and chess_piece_state[tile_selected[0]-1][tile_selected[1]+1].split('_')[0] == '1':
					self.valid_tiiles += [(tile_selected[0]-1,tile_selected[1]+1)]
				if tile_selected[1]>0 and chess_piece_state[tile_selected[0]-1][tile_selected[1]-1] != 0 and chess_piece_state[tile_selected[0]-1][tile_selected[1]-1].split('_')[0] == '1':
					self.valid_tiiles += [(tile_selected[0]-1,tile_selected[1]-1)]

		elif self.turn_color == '1':
			if tile_selected[0] == 1:
				if chess_piece_state[tile_selected[0]+1][tile_selected[1]] == 0:
					self.valid_tiiles += [(tile_selected[0]+1,tile_selected[1])]
					if chess_piece_state[tile_selected[0]+2][tile_selected[1]] == 0:
						self.valid_tiiles += [(tile_selected[0]+2,tile_selected[1])]
			else:
				if chess_piece_state[tile_selected[0]+1][tile_selected[1]] == 0:
					self.valid_tiiles = [(tile_selected[0]+1,tile_selected[1])]
			if king:
				self.valid_tiiles += [(tile_selected[0]+1,tile_selected[1]+1)]
				self.valid_tiiles += [(tile_selected[0]+1,tile_selected[1]-1)]
			else:
				if tile_selected[1]<7 and chess_piece_state[tile_selected[0]+1][tile_selected[1]+1] != 0 and chess_piece_state[tile_selected[0]+1][tile_selected[1]+1].split('_')[0] == '0':
					self.valid_tiiles += [(tile_selected[0]+1,tile_selected[1]+1)]
				if tile_selected[1]>0 and chess_piece_state[tile_selected[0]+1][tile_selected[1]-1] != 0 and chess_piece_state[tile_selected[0]+1][tile_selected[1]-1].split('_')[0] == '0':
					self.valid_tiiles += [(tile_selected[0]+1,tile_selected[1]-1)]
	
	############ for ROOK ################
	def call_rook(self,tile_selected, chess_piece_state, king = False):
		if self.turn_color == '0':
			check = '1'
		elif self.turn_color == '1':
			check = '0'
		# going up
		i = tile_selected[0] - 1
		while i >= 0:
			if chess_piece_state[i][tile_selected[1]] == 0:
				self.valid_tiiles += [(i,tile_selected[1])]
			elif chess_piece_state[i][tile_selected[1]].split('_')[0] == check:
				self.valid_tiiles += [(i,tile_selected[1])]
				if king and chess_piece_state[i][tile_selected[1]].split('_')[1] == 'king':
					i -= 1
					continue
				break

			elif chess_piece_state[i][tile_selected[1]].split('_')[0] == self.turn_color:
				if king:
					self.valid_tiiles += [(i,tile_selected[1])]
				break
			i -= 1
		# going down
		i = tile_selected[0] + 1
		while i < 8:
			if chess_piece_state[i][tile_selected[1]] == 0:
				self.valid_tiiles += [(i,tile_selected[1])]
			elif chess_piece_state[i][tile_selected[1]].split('_')[0] == check:
				self.valid_tiiles += [(i,tile_selected[1])]
				if king and chess_piece_state[i][tile_selected[1]].split('_')[1] == 'king':
					i += 1	
					continue
				break
			elif chess_piece_state[i][tile_selected[1]].split('_')[0] == self.turn_color:
				if king:
					self.valid_tiiles += [(i,tile_selected[1])]
				break
			i += 1
		# going right
		i = tile_selected[1] + 1
		while i < 8:
			if chess_piece_state[tile_selected[0]][i] == 0:
				self.valid_tiiles += [(tile_selected[0],i)]
			elif chess_piece_state[tile_selected[0]][i].split('_')[0] == check:
				self.valid_tiiles += [(tile_selected[0],i)]
				if king and chess_piece_state[tile_selected[0]][i].split('_')[1] == 'king':
					i += 1	
					continue
				break
			elif chess_piece_state[tile_selected[0]][i].split('_')[0] == self.turn_color:
				if king:
					self.valid_tiiles += [(tile_selected[0],i)]
				break
			i += 1
		# going left
		i = tile_selected[1] - 1
		while i >= 0:
			if chess_piece_state[tile_selected[0]][i] == 0:
				self.valid_tiiles += [(tile_selected[0],i)]
			elif chess_piece_state[tile_selected[0]][i].split('_')[0] == check:
				self.valid_tiiles += [(tile_selected[0],i)]
				if king and chess_piece_state[tile_selected[0]][i].split('_')[1] == 'king':
					i -= 1
					continue
				break
			elif chess_piece_state[tile_selected[0]][i].split('_')[0] == self.turn_color:
				if king:
					self.valid_tiiles += [(tile_selected[0],i)]
				break
			i -= 1

	############ for kNIGHT ################
	def call_knight(self,tile_selected, chess_piece_state, king = False):
		if self.turn_color == '0':
			check = '1'
		elif self.turn_color == '1':
			check = '0'
		
		# going up
		if tile_selected[0]-2 >=0:
			if tile_selected[1]-1 >=0:
				l_top_piece = chess_piece_state[tile_selected[0]-2][tile_selected[1]-1]
				if l_top_piece == 0 or l_top_piece.split('_')[0] == check:
					self.valid_tiiles += [(tile_selected[0]-2,tile_selected[1]-1)]
				else:
					if king:
						self.valid_tiiles += [(tile_selected[0]-2,tile_selected[1]-1)]

			if tile_selected[1]+1 <=7:
				r_top_piece = chess_piece_state[tile_selected[0]-2][tile_selected[1]+1]
				if r_top_piece == 0 or r_top_piece.split('_')[0] == check:
					self.valid_tiiles += [(tile_selected[0]-2,tile_selected[1]+1)]
				else:
					if king:
						self.valid_tiiles += [(tile_selected[0]-2,tile_selected[1]+1)]
		# going dowm
		if tile_selected[0]+2 <=7:
			if tile_selected[1]-1 >=0:
				l_bot_piece = chess_piece_state[tile_selected[0]+2][tile_selected[1]-1]
				if l_bot_piece == 0 or l_bot_piece.split('_')[0] == check:
					self.valid_tiiles += [(tile_selected[0]+2,tile_selected[1]-1)]
				else:
					if king:
						self.valid_tiiles += [(tile_selected[0]+2,tile_selected[1]-1)]

			if tile_selected[1]+1 <=7:
				r_bot_piece = chess_piece_state[tile_selected[0]+2][tile_selected[1]+1]
				if r_bot_piece == 0 or r_bot_piece.split('_')[0] == check:
					self.valid_tiiles += [(tile_selected[0]+2,tile_selected[1]+1)]
				else:
					if king:
						self.valid_tiiles += [(tile_selected[0]+2,tile_selected[1]+1)]

		# going left
		if tile_selected[1]-2 >=0:
			if tile_selected[0]-1 >=0:
				l_top_piece = chess_piece_state[tile_selected[0]-1][tile_selected[1]-2]
				if l_top_piece == 0 or l_top_piece.split('_')[0] == check:
					self.valid_tiiles += [(tile_selected[0]-1,tile_selected[1]-2)]
				else:
					if king:
						self.valid_tiiles += [(tile_selected[0]-1,tile_selected[1]-2)]
			if tile_selected[0]+1 <=7:
				r_top_piece = chess_piece_state[tile_selected[0]+1][tile_selected[1]-2]
				if r_top_piece == 0 or r_top_piece.split('_')[0] == check:
					self.valid_tiiles += [(tile_selected[0]+1,tile_selected[1]-2)]
				else:
					if king:
						self.valid_tiiles += [(tile_selected[0]+1,tile_selected[1]-2)]
		# going right
		if tile_selected[1]+2 <=7:
			if tile_selected[0]-1 >=0:
				l_bot_piece = chess_piece_state[tile_selected[0]-1][tile_selected[1]+2]
				if l_bot_piece == 0 or l_bot_piece.split('_')[0] == check:
					self.valid_tiiles += [(tile_selected[0]-1,tile_selected[1]+2)]
				else:
					if king:
						self.valid_tiiles += [(tile_selected[0]-1,tile_selected[1]+2)]

			if tile_selected[0]+1 <=7:
				r_bot_piece = chess_piece_state[tile_selected[0]+1][tile_selected[1]+2]
				if r_bot_piece == 0 or r_bot_piece.split('_')[0] == check:
					self.valid_tiiles += [(tile_selected[0]+1,tile_selected[1]+2)]
				else:
					if king:
						self.valid_tiiles += [(tile_selected[0]+1,tile_selected[1]+2)]

	############ for BISHOP ################
	def call_bishop(self,tile_selected, chess_piece_state, king = False):
		if self.turn_color == '0':
			check = '1'
		elif self.turn_color == '1':
			check = '0'
		# going bot right
		i = 1
		while tile_selected[0]+i<8 and tile_selected[1]+i<8:
			piece = chess_piece_state[tile_selected[0]+i][tile_selected[1]+i]
			if piece == 0:
				self.valid_tiiles += [(tile_selected[0]+i,tile_selected[1]+i)]
			elif piece.split('_')[0] == check:
				self.valid_tiiles += [(tile_selected[0]+i,tile_selected[1]+i)]
				if king and piece.split('_')[1] == 'king':
					i +=1
					continue
				break
			elif piece.split('_')[0] == self.turn_color:
				break
			i +=1 
		# going top left
		i = -1
		while tile_selected[0]+i>=0 and tile_selected[1]+i>=0:
			piece = chess_piece_state[tile_selected[0]+i][tile_selected[1]+i]
			if piece == 0:
				self.valid_tiiles += [(tile_selected[0]+i,tile_selected[1]+i)]
			elif piece.split('_')[0] == check:
				self.valid_tiiles += [(tile_selected[0]+i,tile_selected[1]+i)]
				if king and piece.split('_')[1] == 'king':
					i -=1
					continue
				break
			elif piece.split('_')[0] == self.turn_color:
				break
			i -=1
			
		# going bot left
		i = 1
		while tile_selected[0]+i<8 and tile_selected[1]-i>=0:
			piece = chess_piece_state[tile_selected[0]+i][tile_selected[1]-i]
			if piece == 0:
				self.valid_tiiles += [(tile_selected[0]+i,tile_selected[1]-i)]
			elif piece.split('_')[0] == check:
				self.valid_tiiles += [(tile_selected[0]+i,tile_selected[1]-i)]
				if king and piece.split('_')[1] == 'king':
					i +=1
					continue
				break
			elif piece.split('_')[0] == self.turn_color:
				break
			i +=1
		# going top right
		i = 1
		while tile_selected[0]-i>=0 and tile_selected[1]+i<8:
			piece = chess_piece_state[tile_selected[0]-i][tile_selected[1]+i]
			if piece == 0:
				self.valid_tiiles += [(tile_selected[0]-i,tile_selected[1]+i)]
			elif piece.split('_')[0] == check:
				self.valid_tiiles += [(tile_selected[0]-i,tile_selected[1]+i)]
				if king and piece.split('_')[1] == 'king':
					i +=1
					continue
				break
			elif piece.split('_')[0] == self.turn_color:
				break
			i +=1 

	############ for QUEEN ################
	def call_queen(self,tile_selected, chess_piece_state, king = False):
		self.call_rook(tile_selected, chess_piece_state, king)
		self.call_bishop(tile_selected, chess_piece_state, king)

	def call_all_oppo(self,tile_selected, chess_piece_state, is_check = False):
		print('wwwwwwwwwwww TRUE')
		selected_chess_piece = chess_piece_state[tile_selected[0]][tile_selected[1]]
		if selected_chess_piece.split('_')[1]=='pawn':
			self.call_pawn(tile_selected, chess_piece_state, True)
		elif selected_chess_piece.split('_')[1]=='rook':
			self.call_rook(tile_selected, chess_piece_state, True)
		elif selected_chess_piece.split('_')[1]=='knight':
			self.call_knight(tile_selected, chess_piece_state, True)
		elif selected_chess_piece.split('_')[1]=='bishop':
			self.call_bishop(tile_selected, chess_piece_state, True)
		elif selected_chess_piece.split('_')[1]=='queen':
			self.call_queen(tile_selected, chess_piece_state, True)
		if is_check:
			if selected_chess_piece.split('_')[1]=='king':
				self.call_queen(tile_selected, chess_piece_state, True)

	############ for KING ################
	def call_king(self,tile_selected, chess_piece_state):
		if self.turn_color == '0':
			self.turn_color = '1'
			check = '1'
		elif self.turn_color == '1':
			self.turn_color = '0'
			check = '0'

		not_valid = []
		i = 0
		while i<len(tile_layout):
			j = 0
			while j < len(tile_layout[i]):
				if chess_piece_state[i][j] !=0 and chess_piece_state[i][j].split('_')[0]==check:
					self.call_all_oppo((i,j), chess_piece_state)
					not_valid = not_valid + self.valid_tiiles
					self.valid_tiiles = []
				j += 1
			i += 1

		if self.turn_color == '0':
			self.turn_color = '1'
		elif self.turn_color == '1':
			self.turn_color = '0'

		i = -1
		while i <= 1:
			if 0 <= tile_selected[0] + i <=7:
				j = -1
				while j <= 1:
					if 0 <= tile_selected[1] + j <=7:
						if i == 0 and j == 0:
							j += 1
							continue

						if (tile_selected[0] + i,tile_selected[1]+j) not in not_valid:
							if chess_piece_state[tile_selected[0] + i][tile_selected[1] + j] == 0 or chess_piece_state[tile_selected[0] + i][tile_selected[1] + j].split('_')[0] == check:
								self.valid_tiiles += [(tile_selected[0] + i,tile_selected[1] + j)]
					j += 1
			i += 1
		print('valid_tiiles ====== ',self.valid_tiiles)
  
	def find_valid_check_path(self, check_from, location_of_turn_king):
		chek_path_tiles = []
		if check_from[1][0] == location_of_turn_king[0]:
			if check_from[1][1] > location_of_turn_king[1]:
				x = check_from[1][1]
				while x > location_of_turn_king[1]:
					chek_path_tiles += [(location_of_turn_king[0],x)]
					x -= 1
			else:
				x = check_from[1][1]
				while x < location_of_turn_king[1]:
					chek_path_tiles += [(location_of_turn_king[0],x)]
					x += 1

		elif check_from[1][1] == location_of_turn_king[1]:
			if check_from[1][0] > location_of_turn_king[0]:
				x = check_from[1][0]
				while x > location_of_turn_king[0]:
					chek_path_tiles += [(x,location_of_turn_king[1])]
					x -= 1
			else:
				x = check_from[1][0]
				while x < location_of_turn_king[0]:
					chek_path_tiles += [(x,location_of_turn_king[1])]
					x += 1

		elif check_from[1][0] > location_of_turn_king[0]:
			y = check_from[1][0]
			if check_from[1][1] > location_of_turn_king[1]:
				x = check_from[1][1]
				while x > location_of_turn_king[1]:
					chek_path_tiles += [(y,x)]
					x -= 1
					y -= 1
			else:
				x = check_from[1][1]
				while x < location_of_turn_king[1]:
					chek_path_tiles += [(y,x)]
					x += 1
					y += 1

		elif check_from[1][0] < location_of_turn_king[0]:
			y = check_from[1][0]
			if check_from[1][0] > location_of_turn_king[0]:
				x = check_from[1][0]
				while x > location_of_turn_king[0]:
					chek_path_tiles += [(y,x)]
					x -= 1
					y -= 1
			else:
				x = check_from[1][0]
				while x < location_of_turn_king[0]:
					chek_path_tiles += [(y,x)]
					x += 1
					y += 1

		return chek_path_tiles


	def is_king_checked(self, tile_selected, chess_piece_state):
		if self.turn_color == '0':
			self.turn_color = '1'
			check = '0'
		elif self.turn_color == '1':
			self.turn_color = '0'
			check = '1'

		not_valid = []
		i = 0
		location_of_turn_king = ()
		while i<len(tile_layout):
			j = 0
			while j < len(tile_layout[i]):
				if chess_piece_state[i][j] !=0 and chess_piece_state[i][j].split('_')[1] == 'king':
					if chess_piece_state[i][j].split('_')[0] == check:
						location_of_turn_king = (i,j)
						break
				j += 1
			i += 1
		i = 0
		while i<len(tile_layout):
			j = 0
			while j < len(tile_layout[i]):
				if chess_piece_state[i][j] !=0 and chess_piece_state[i][j].split('_')[0]==self.turn_color:
					self.call_all_oppo((i,j), chess_piece_state, True)
					if location_of_turn_king in self.valid_tiiles:
						not_valid = not_valid + self.valid_tiiles + [(i,j)]
						check_from = [chess_piece_state[i][j].split('_')[1], [i,j]]
						
					self.valid_tiiles = []
				j += 1
			i += 1
		print('location_of_turn_king',location_of_turn_king)
		print(not_valid,'not_valid')

		if self.turn_color == '0':
			self.turn_color = '1'
		elif self.turn_color == '1':
			self.turn_color = '0'


		if location_of_turn_king in not_valid:
			self.king_check = True
			not_valid = self.find_valid_check_path(check_from, location_of_turn_king)
		else:
			self.king_check = False


		return not_valid

	def calculate_valid_moves(self, chess_piece_state, tile_selected):
		selected_chess_piece = chess_piece_state[tile_selected[0]][tile_selected[1]]

		if selected_chess_piece.split('_')[0] == self.turn_color:
			self.can_select = True
		else:
			self.can_select = False

		if not self.can_select:
			return None

		print('selected piece',selected_chess_piece.split('_')[1])
		path_to_block =self.is_king_checked(tile_selected, chess_piece_state)


		self.valid_tiiles = []
		if selected_chess_piece.split('_')[1]=='pawn':
			self.call_pawn(tile_selected, chess_piece_state)
		elif selected_chess_piece.split('_')[1]=='rook':
			self.call_rook(tile_selected, chess_piece_state)
		elif selected_chess_piece.split('_')[1]=='knight':
			self.call_knight(tile_selected, chess_piece_state)
		elif selected_chess_piece.split('_')[1]=='bishop':
			self.call_bishop(tile_selected, chess_piece_state)
		elif selected_chess_piece.split('_')[1]=='queen':
			self.call_queen(tile_selected, chess_piece_state)
		elif selected_chess_piece.split('_')[1]=='king':
			self.call_king(tile_selected, chess_piece_state)

		print('self.king_check',self.king_check)
		if self.king_check and selected_chess_piece.split('_')[1] != 'king':
			new_valid_tiles = []
			for tile in self.valid_tiiles:
				if tile in path_to_block:
					new_valid_tiles.append(tile)
			self.valid_tiiles = new_valid_tiles

		print('valid_tiiles',self.valid_tiiles)
	def change_turn_color(self):
		if self.turn_color == '0':
			self.turn_color = '1'
		else:
			self.turn_color = '0'
		self.can_select = False