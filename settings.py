# screen
window_size = (1280,720)
game_caption = 'Chess'

# colors
back_ground_color = (96, 108, 56) # dark grass green 
chess_board_color = (188, 108, 37) # wood like
light_tile_color = (212, 163, 115) # light wood like
dark_tile_color = (188, 108, 37) # wood like
BLACK = (0, 0, 0)
restart_text = (242,232,207) # malkat
light_tile_color_h = (255, 163, 115) # light wood like HIGHLIGHT
dark_tile_color_h = (255, 108, 37) # wood like HIGHLIGHT
chess_piece_bg = (163, 177, 138) # light grey green

chess_board_size = (window_size[1]*0.95,window_size[1]*0.95)
chess_board_pos = (window_size[0]*0.5 - chess_board_size[0]*0.5,
					window_size[1]*0.5 - chess_board_size[1]*0.5)

play_board_size = (window_size[1]*0.875,window_size[1]*0.875)
play_board_pos = (window_size[0]*0.5 - play_board_size[0]*0.5,
					window_size[1]*0.5 - play_board_size[1]*0.5)



tile_layout = [
	[0,1,0,1,0,1,0,1],
	[1,0,1,0,1,0,1,0],
	[0,1,0,1,0,1,0,1],
	[1,0,1,0,1,0,1,0],
	[0,1,0,1,0,1,0,1],
	[1,0,1,0,1,0,1,0],
	[0,1,0,1,0,1,0,1],
	[1,0,1,0,1,0,1,0],
]


# borders

inner_borders_thickness = 1

piece_init_pos = [
	['1_rook','1_knight','1_bishop','1_queen','1_king','1_bishop','1_knight','1_rook'],
	['1_pawn','1_pawn','1_pawn','1_pawn','1_pawn','1_pawn','1_pawn','1_pawn'],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	['0_pawn','0_pawn','0_pawn','0_pawn','0_pawn','0_pawn','0_pawn','0_pawn'],
	['0_rook','0_knight','0_bishop','0_queen','0_king','0_bishop','0_knight','0_rook'],
]

# piece_init_pos = [
# 	['1_rook','1_knight','1_bishop','1_queen','1_king','1_bishop','1_knight',0],
# 	['1_pawn','1_pawn','1_pawn','1_pawn','1_pawn','1_pawn','1_pawn','0_pawn'],
# 	[0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0],
# 	['0_pawn','0_pawn','0_pawn','0_pawn','0_pawn','0_pawn','0_pawn','0_pawn'],
# 	['0_rook','0_knight','0_bishop','0_queen','0_king','0_bishop','0_knight','0_rook'],
# ]

chess_pieces = {'pawn' : [] ,
				'rook' : [] ,
				'knight' : [] ,
				'bishop' : [] ,
				'queen' : [] ,
				'king' : [] ,
				}

selct_piece = {	0 : 'pawn' ,
				1 : 'rook',
				2 : 'knight',
				3 : 'bishop',
				4 : 'queen',
				}

letters = ['A','B','C','D','E','F','G','H']