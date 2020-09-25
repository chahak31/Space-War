import turtle
import math

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

#define functions
def movefw():
    player.forward(20)

def moveleft():
    player.left(30)

def moveright():
    player.right(30)

def movebw():
    player.forward(-40)

#set Keyboard bindings
turtle.listen()
turtle.onkey(movefw,"Up")
turtle.onkey(moveleft,"Left")
turtle.onkey(moveright,"Right")
turtle.onkey(movebw,"Down")

while True:
    player.forward(speed)

    if player.xcor()>300 or player.xcor()<-300:
        player.left(180)

    if player.ycor()>300 or player.ycor()<-300:
        player.left(180)






    
