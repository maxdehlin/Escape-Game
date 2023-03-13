import turtle
import turtle_escape_room as room 


fred = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(10000,10000)#speed up the drawing of turtle graphics
fred.speed(0)
dead = False
#listen for key events
turtle.listen()

#register custom images
# turtle.register_shape('guy.gif')
turtle.register_shape('character.gif')

momentum = "right"

room.load_map('map')
room.cell_size = 30 #size of each cell in the game

# welcome
print("Welcome to The Game. Make your way to the green square with the arrowkeys.")
print("You can jump over the red squares with the spacebar.")
print("However, you may only jump if you have momentum in the direction you are facing. ")
print("For example, if you have just moved to the right you may only jump to the right.")
print("Press 'r' to restart")

def render_cell(turt,x,y,symbol):
	"""
	  Called each time the map is drawn on the screen.
		turt - the turtle currently drawing
		x, the x coordinate of the cell being drawn
		y, the y coordinate of the cell being drawn
		symbol - The character on the map (from the file) currently being rendered."""
	#draw the player
	if(room.player_is_ready==True and room.player_x == x and room.player_y == y ):
			turt.shape('character.gif')
			turt.stamp()
	else:#everything not the player
		if(symbol=='w'):#wall
			turt.color('black')
			turt.shape("square")
			turt.stamp()
		elif(symbol=='d'):#door
			turt.color('gray')
			turt.shape('square')
			turt.stamp()
		elif(symbol=='p' and room.player_is_ready==False):#place the player
			room.player_x = x
			room.player_y = y
			room.player_is_ready = True
			turt.shape('character.gif')
			turt.stamp()
			print('Begin!')
		elif symbol == 'e':
			# display an enemy
			turt.color('red')	
			turt.shape("square")
			turt.stamp()
		elif symbol == 'i':
			# display ice blocks
			turt.color('gray')	
			turt.shape("square")
			turt.stamp()
		elif symbol == 'f':
			# display win block
			turt.color('green')	
			turt.shape("square")
			turt.stamp()

# win if reach green win block
def win():
	if (room.map[room.player_y][room.player_x]=='f'):
		print("Congratulations! You've won!")
		reset()

# ice function

def ice(direction):
	# checks if player is on ice and checks what direction they just moved 
	if (room.map[room.player_y][room.player_x]=='i'): 
		if direction == 'up':
			if (room.map[room.player_y+1][room.player_x]!='w'):
				# moves player up if it's allowed
				up()

		elif direction == 'down':
			if (room.map[room.player_y-1][room.player_x]!='w'):
				# moves player down if it's allowed
				down()

		elif direction == 'left':
			if (room.map[room.player_y][room.player_x-1]!='w'):
				# moves player left if it's allowed				
				left()

		elif direction == 'right':
			if (room.map[room.player_y][room.player_x+1]!='w'):
				# moves player right if it's allowed
				right()


# actions

def up():
	""""""
	########
  #do not allow the player to move up if there is a wall in the way
	########
	if(room.map[room.player_y+1][room.player_x]!='w' and room.map[room.player_y+1][room.player_x]!='e'):
		room.player_y += 1
		global momentum
		momentum = "up"
		win()

		# runs ice function
		ice('up')
	room.print_map()
		
def down():
	""""""
	#do not allow the player to move down if there is a wall in the way
	if(room.map[room.player_y-1][room.player_x]!='w' and room.map[room.player_y-1][room.player_x]!='e'):
		room.player_y -= 1 
		room.print_map()
		global momentum
		momentum = "down"

		ice('down')
	room.print_map()


def left():
	""""""
	#do not allow the player to move left if there is a wall in the way
	if(room.map[room.player_y][room.player_x-1]!='w' and room.map[room.player_y][room.player_x-1]!='e'):
		room.player_x -= 1 
		room.print_map()
		global momentum
		momentum = "left"


		ice('left')
	room.print_map()	

			
def right():
	""""""
	#do not allow the player to move right if there is a wall in the way
	if(room.map[room.player_y][room.player_x+1]!='w' and room.map[room.player_y][room.player_x+1]!='e'):
		room.player_x += 1 
		room.print_map()
		global momentum
		momentum = "right"
		ice('right')
	room.print_map()

			
# jumps

def jump():
	""""""
	# jumps the character over a red block

	if momentum == "right":
		# checks for black walls and doesn't let jump into lava block
		if(room.map[room.player_y][room.player_x+2]!='w' and room.map[room.player_y][room.player_x+1]!='w' and room.map[room.player_y][room.player_x+2]!='e'):
			room.player_x += 2

	if momentum == "left":
		# checks for black walls and doesn't let jump into lava block
		if(room.map[room.player_y][room.player_x-2]!='w' and room.map[room.player_y][room.player_x-1]!='w' and room.map[room.player_y][room.player_x-2]!='e'):
			room.player_x -= 2

	if momentum == "up":
		# checks for black walls and doesn't let jump into lava block
		if(room.map[room.player_y+2][room.player_x]!='w' and room.map[room.player_y+1][room.player_x]!='w' and room.map[room.player_y+2][room.player_x]!='e'):
			room.player_y += 2

	if momentum == "down":
		# checks for black walls and doesn't let jump into lava block
		if(room.map[room.player_y-2][room.player_x]!='w' and room.map[room.player_y-1][room.player_x]!='w' and room.map[room.player_y-2][room.player_x]!='e'):			
			room.player_y -= 2
	room.print_map()


def reset():
	room.player_x = 1
	# print(room.player_x)
	room.player_y = 10
	print('Game reset')

	room.print_map()

room.register_turtle(turtl=fred,callback=render_cell,xoffset=-300,yoffset=-150)
#register the up, down, left, right, jump, reset events
turtle.onkey(up, "Up") 
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(jump, "space")
turtle.onkey(reset, "r")


#print the map
room.print_map()
# turtle.ontimer(on_timer,1000)
turtle.mainloop()  # This will make sure the program continues to run 