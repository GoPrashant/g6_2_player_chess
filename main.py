import pygame as pg
import sys
from settings import *
from level import Level

class Game():
	def __init__(self):
		self.screen = pg.display.set_mode(window_size)
		pg.display.set_caption(game_caption)
		self.clock = pg.time.Clock()
		self.level = Level()
		
		pg.init()
 
	def run(self):
		while True:
			dt = self.clock.tick()/1000
			self.level.run(dt)
			pg.display.update()


if __name__ == "__main__":
	game = Game()
	game.run()

