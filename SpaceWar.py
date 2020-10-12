import os
import turtle
import math
import random

#sets the animation speed to the maximum
turtle.speed(0)
turtle.bgcolor("black")
#hide the default turtle
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(1)

#Child of the turtle class
class Sprite(turtle.Turtle):
    #constructor
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)

        self.speed = 1

    def move(self):
        self.fd(self.speed)

        #Boundary detection
        if self.xcor()>290:
            self.setx(290)
            self.rt(60)
        if self.xcor()<-290:
            self.setx(-290)
            self.rt(60)
        if self.ycor()>290:
            self.sety(290)
            self.rt(60)
        if self.ycor()<-290:
            self.sety(-290)
            self.rt(60)

#Child of Sprite class
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed=4
        self.lives=3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed+=1

    def decelerate(self):
        self.speed-=1

class Game():
    def __init__(self):
        self.level=1
        self.score=0
        self.state="Playing"
        self.pen = turtle.Turtle()
        self.lives=3

    def draw_border(self):
        #Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300,300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()

#Create game object
game = Game()

#Draw the game border
game.draw_border()
#create my sprites
player = Player("triangle","white", 0,0)

#Keyboard bindings
turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.decelerate,"Down")

#Main game loop
while True:
    player.move()

delay = input("Press enter to finish")
