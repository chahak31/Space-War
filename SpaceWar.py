import turtle
import math
import random

#create a screen
wn = turtle.Screen()
wn.bgcolor("black")

#create a player
player = turtle.Turtle()
player.penup()
player.color("green")
player.shape("turtle")

#Draw boundary
boundary = turtle.Turtle()
boundary.penup()
boundary.color("white")
boundary.setposition(-300,-300)
boundary.speed(0)
boundary.pendown()
boundary.pensize(3)
for i in range(4):
    boundary.forward(600)
    boundary.left(90)
boundary.hideturtle()

speed = 1

#create a goal
goal = turtle.Turtle()
goal.color("white")
goal.shape("square")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-300,300),random.randint(-300,300))

#define functions
def movefw():
    player.forward(20)

def moveleft():
    player.left(30)

def moveright():
    player.right(30)

"""
def movebw():
    player.forward(-40)
"""

def isCollision(ply, gl):
    d = math.sqrt(math.pow(ply.xcor()-gl.xcor(),2)+math.pow(ply.ycor()-gl.ycor(),2))
    if d<20:
        return True
    else:
        return False

def fire():
    if turtle.onkey == "Down":
        return True

#set Keyboard bindings
turtle.listen()
turtle.onkey(movefw,"Up")
turtle.onkey(moveleft,"Left")
turtle.onkey(moveright,"Right")
#turtle.onkey(movebw,"Down")
turtle.onkey(fire,"Down")

while True:
    player.forward(speed)

    if player.xcor()>300 or player.xcor()<-300:
        player.left(180)

    if player.ycor()>300 or player.ycor()<-300:
        player.left(180)

    goal.forward(2)

    if goal.xcor()>300 or goal.xcor()<-300:
        goal.left(180)

    if goal.ycor()>300 or goal.ycor()<-300:
        goal.left(180)

    if isCollision(player, goal):
        goal.setposition(random.randint(-300,300),random.randint(-300,300))
        goal.left(random.randint(0,360))

    if fire():
        #create a fire turtle
        fireturtle = turtle.Turtle()
        fireturtle.penup()
        fireturtle.speed(0)
        fireturtle.color("red")
        fireturtle.shape("triangle")
        fireturtle.setposition(player.xcor(),player.ycor())
        fireturtle.pendown()
        fireturtle.stamp()
        fireturtle.forward(100)
        fireturtle.hideturtle()


        
