import turtle
from os import system, name

#creates a visual escape room

#use main.py as a sample


#create the variables to track the user's position
player_x=-1
player_y=-1
player_is_ready=False
map = []
cell_size = 30
cell_render_callback = None
current_map_name = ''
def load_map(filename='map'):
	global player_is_ready
	global map
	global current_map_name
	current_map_name = filename
	#load the map list from the file
	f = open(filename,'r')
	map = f.readlines()
	for x in range(len(map)):
		#remove the line break at the end of the row
		data = map[x][0:-1]
		map[x] = []
		for c in data:
			map[x].append(c)
			
	#fix the map layout so the list indexing matches x/y coordinates
	newmap = []
	counter = 0
	for x in range(len(map)-1,-1,-1):
		newmap.append(map[x])
		counter += 1
	#print(map)
	#print(newmap)
	map = newmap
	#reset the player_is_ready
	player_is_ready = False

def register_turtle(turtl,callback,xoffset=-300,yoffset=-100):
	global turt
	turt = turtl
	global cell_render_callback
	cell_render_callback = callback
	global mapx_offset
	global mapy_offset
	mapx_offset = xoffset
	mapy_offset = yoffset

def print_map():
	"""Draws the map on the screen. Turt is the turle drawing. Map is the 2D list of symbols to draw the map.  cell_render_callback gets called when it is time to render a cell."""
	global player_x
	global player_y
	turt.clear()
	turt.up()
	y = 0
	for row in map:
		x = 0
		for col in row:
			#goto to the x,y position on the map
			turt.goto(x*cell_size + mapx_offset,y*cell_size+mapy_offset)
			#check to see what is drawn on this spot
			cell_render_callback(turt,x,y,col)
				
			x += 1
		y += 1
	#hide the turtle after drawing the map
	turt.hideturtle()