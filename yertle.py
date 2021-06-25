
import turtle
import random

# constants for pen width
MAXPENSIZE = 100
MINPENSIZE = 5
PENINCREMENT = 5

# global variable for tracking pen width
global pensize
pensize = 10

# define list of colors for random choices
colors = ["red","orange","yellow","green","blue","indigo","violet","pink","cyan"]
# define list of shapes for random choices
shapes = ["arrow","turtle","circle","square","triangle","classic"]

# instantiate yertle the turtle
yertle = turtle.Turtle()

def move(distance = 10):
    yertle.forward(distance)

def turnleft(degrees = 90):
    yertle.left(degrees)

def turnright(degrees = 90):
    yertle.right(degrees)

def changecolor():
    color = random.choice(colors)
    yertle.color(color)

def changeshape():
    shape = random.choice(shapes)
    yertle.shape(shape)

def draw():
    yertle.pendown()

def up():
    yertle.penup()

def wider():
    global pensize  # use global variable tracking pen size
    pensize = pensize + PENINCREMENT
    if pensize > MAXPENSIZE:
        pensize = MAXPENSIZE
    yertle.pensize(pensize)
    
def narrower():
    global pensize  # use global variable tracking pen size
    pensize = pensize - PENINCREMENT
    if pensize < MINPENSIZE:
        pensize = MINPENSIZE
    yertle.pensize(pensize)

# toggle yertle's visibility
def showhide():
    if yertle.isvisible():
        yertle.hideturtle()
    else:
        yertle.showturtle()

def endgame():
    yertle.getscreen().bye()

# set up the window and display instructions
yertle.getscreen().setup(width=500, height=500)
yertle.hideturtle()
yertle.penup()
yertle.setposition(-240.00,230.00)
yertle.write("Try the following keys: arrows, c, s, h, d, u, +, -", font=("Arial", 16, "normal"))
yertle.setposition(-240.00,210.00)
yertle.write("Type 'q' to quit", font=("Arial", 16, "normal"))
yertle.home()
yertle.showturtle()

# listen for key presses
turtle.listen()

# set function to call for each key
turtle.onkey(move, "Up")
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(changecolor, "c")
turtle.onkey(changeshape, "s")
turtle.onkey(showhide, "h")
turtle.onkey(draw, "d")
turtle.onkey(up, "u")
turtle.onkey(wider, "plus")
turtle.onkey(narrower, "minus")
turtle.onkey(endgame, "q")

# start the event loop
turtle.mainloop()
