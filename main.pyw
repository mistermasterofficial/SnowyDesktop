import pygame as pg
import json
from vector import *
from random import randrange
from transparent import *

pg.init()

displayInfo = pg.display.Info()

screen_size = (displayInfo.current_w, displayInfo.current_h)
screen = pg.display.set_mode(screen_size, pg.NOFRAME)

pg.display.set_caption("Snow by Mister_Master 2022")

icon = pg.Surface((256, 256));pg.draw.circle(icon, (255, 255, 255), (128, 128), 128);icon.set_colorkey((0,0,0));pg.display.set_icon(icon)
create_transparent_window((0,0,0))
topmost()

clock = pg.time.Clock()

run = True

def load_settings():
	global vector
	global dispersion
	global speed
	global radius
	global snow_num

	with open("settings.json", "r") as f:
		data = json.load(f)

	vector = data["vector"]
	dispersion = data["dispersion"]
	speed = data["speed"]
	radius = data["radius"]
	snow_num = data["snow_num"]

load_settings()

class Cell():
	cells = []
	def __init__(self, name, pos=Vec(0), vec=Vec(1, 0)):
		self.name = name
		self.pos = pos
		self.vec = vec

		self.cells.append(self)
	
	def update(self):
		self.pos.x += self.vec.x; self.pos.y += self.vec.y

[Cell("snow", pos=Vec(randrange(screen_size[0]), randrange(screen_size[1])), vec=norm(Vec(randrange(-dispersion+vector,dispersion+1+vector), randrange(5,25)))) for _ in range(snow_num)]

for c in Cell.cells:
	c.vec.x*=speed
	c.vec.y*=speed

while run:
	clock.tick(60)

	events = pg.event.get()
	for e in events:
		if e.type == pg.QUIT:
			run = False
	
	screen.fill((0, 0, 0))

	for c in Cell.cells:
		if c.pos.x>=screen_size[0]:
			c.pos.x = 0
		else:
			c.update()
			c.pos.x %= screen_size[0]

		if c.pos.y>=screen_size[1]:
			c.pos.y = 0
		else:
			c.update()
			c.pos.y %= screen_size[1]
		
		pg.draw.circle(screen, (255,255,255), (c.pos.x, c.pos.y), radius)

	pg.display.update()

pg.quit()