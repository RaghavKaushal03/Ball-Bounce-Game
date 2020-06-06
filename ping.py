import turtle
import os
import winsound

#create the window
wn = turtle.Screen()
wn.title("Raghav's Game")
wn.bgcolor("sky blue")
wn.setup(width=800,height=600)
wn.tracer(0) #animation speed

scoreA,scoreB=0,0

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square") #20px by 20px
paddleA.color("black")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square") #20px by 20px
paddleB.color("black")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

#bALL
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)

ball.dx=0.15
ball.dy=0.15

#score
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center",font=("courier"))


#functions

def paddleAUp():
    y=paddleA.ycor()
    y=y+20
    paddleA.sety(y)

def paddleADown():
    y=paddleA.ycor()
    y=y-20
    paddleA.sety(y)

   

def paddleBUp():
    y=paddleB.ycor()
    y=y+20
    paddleB.sety(y)

def paddleBDown():
    y=paddleB.ycor()
    y=y-20
    paddleB.sety(y)


 #keyboard binding
    

wn.listen()
wn.onkeypress(paddleAUp,"w")
wn.onkeypress(paddleADown,"s")
wn.onkeypress(paddleBUp,"Up")
wn.onkeypress(paddleBDown,"Down")

while True:
    wn.update()
    
    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        winsound.PlaySound("ballBounce.wav",winsound.SND_ASYNC)
        ball.dy=ball.dy*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        winsound.PlaySound("ballBounce.wav",winsound.SND_ASYNC)
        ball.dy=ball.dy*-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
        scoreA =+ 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA,scoreB),align="center",font=("courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
        scoreB =+ 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA,scoreB),align="center",font=("courier",24,"normal"))
#bit.ly/GDResourses


    #collide with paddles
    if ball.xcor()>340 and (ball.ycor()<paddleB.ycor()+50 and ball.ycor()>paddleB.ycor()-50):
        ball.dx=ball.dx*-1         

    if ball.xcor()<-340 and (ball.ycor()<paddleA.ycor()+50 and ball.ycor()>paddleA.ycor()-50):
        ball.dx=ball.dx*-1                