# Simple game to shoot parabolic projectiles

import turtle
import math

wn = turtle.Screen()
wn.setup(width=600, height=400)
wn.bgcolor("black")
wn.tracer(0)

verVar = True

pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Ball(turtle.Turtle):
    def __init__(self, color):
        self.shape = "circle"
        self.color = color

    def render(self, pen):
        pen.shape(self.shape)
        # pen.setheading(self.heading)
        pen.shapesize(stretch_wid=.2, stretch_len=.2)
        pen.stamp()


class Sprite(turtle.Turtle):
    def __init__(self, x, y, color, shape):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.heading = 0
        self.da = 0

    def update(self):
        self.heading += self.da

    def rotate_left(self):
        self.da = 1

    def rotate_right(self):
        self.da = -1

    def stoprotation(self):
        self.da = 0

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.setheading(self.heading)
        pen.shapesize(stretch_wid=.5, stretch_len=.5)
        pen.stamp()



shooter = Sprite(-200, -100, "white", "triangle")
shooter.da = 0

ball = Ball("red")

def quitscreen():
    global verVar
    verVar = False


wn.listen()
wn.onkeypress(quitscreen, "q")
wn.onkeypress(shooter.rotate_left, "Left")
wn.onkeypress(shooter.rotate_right, "Right")
wn.onkeyrelease(shooter.stoprotation, "Right")
wn.onkeyrelease(shooter.stoprotation, "Left")

# wn.onkeypress(releaseball, "Space")



# main game

while verVar == True:
    pen.clear()

    #update player
    shooter.update()

    #render sprites
    shooter.render(pen)
    ball.render(pen)
    wn.update()

turtle.mainloop()
