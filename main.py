import turtle
import time
import random
import os
from random import randint

delay = 0.1
score = 0

wn = turtle.Screen()
wn.title("Snake by Om")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

#snake
snake = turtle.Turtle()
wn = turtle.Screen()
imageup = os.path.expanduser("~\OneDrive\Desktop\snake_head.gif")
imagedown = os.path.expanduser("~\OneDrive\Desktop\snake_down.gif")
imageright = os.path.expanduser("~\OneDrive\Desktop\snake_right.gif")
imageleft = os.path.expanduser("~\OneDrive\Desktop\snake_left.gif")
seg_hor = os.path.expanduser("~\OneDrive\Desktop\segment_ver.gif")
seg_ver = os.path.expanduser("~\OneDrive\Desktop\segment_hor.gif")
snakebg = os.path.expanduser("~\OneDrive\Desktop\snake_bg.gif")
foodim = os.path.expanduser("~\OneDrive\Desktop\imagefood.gif")
wn.addshape(foodim)
wn.addshape(snakebg)
wn.bgpic(snakebg)
wn.addshape(imageup)
wn.addshape(imagedown)
wn.addshape(imageright)
wn.addshape(imageleft)
wn.addshape(seg_ver)
wn.addshape(seg_hor)
snake.shape(imageup)
snake.speed(100)
snake.color("green")
snake.shapesize(1, 1)
snake.penup()
snake.goto(350, 0)
snake.direction = "stop"

#food
k = 1
food = turtle.Turtle()
food.speed(0)
food.shape(foodim)
food.color("red")
food.shapesize(stretch_len=1, stretch_wid=k)
food.penup()
food.goto(randint(-300, 300), randint(-300, 300))


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("SCORE : 0", align="center", font=("consolas", 24, "bold"))

#border
border = turtle.Turtle()
border.color("white")
border.shape("circle")
border.shapesize(0.0001)
border.penup()
border.goto(0, 300)
border.pendown()
border.forward(350)
border.right(90)
border.forward(600)
border.right(90)
border.forward(700)
border.right(90)
border.forward(600)
border.right(90)
border.forward(350)
border.right(90)

#functions
def snakeup():
    if snake.direction != "down":
        snake.direction = "up"

def snakedown():
    if snake.direction != "up":
        snake.direction = "down"

def snakeleft():
    if snake.direction != "right":
        snake.direction = "left"

def snakeright():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        snake.shape(imageup)
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        snake.shape(imagedown)
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        snake.shape(imageleft)
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        snake.shape(imageright)
        x = snake.xcor()
        snake.setx(x + 20)

wn.listen()
wn.onkeypress(snakeup, "w")
wn.onkeypress(snakedown, "s")
wn.onkeypress(snakeright, "d")
wn.onkeypress(snakeleft, "a")

segs = []

#main game loop
while True:
    wn.update()
    #warping
    if(snake.xcor() > 330) or (snake.xcor() < -330):
        if(snake.xcor() > 330):
            snake.goto(-330, snake.ycor())
        else:
            snake.goto(330, snake.ycor())

    if(snake.ycor() > 280) or (snake.ycor() < -280):
        if(snake.ycor() > 280):
            snake.goto(snake.xcor(), -280)
        else:
            snake.goto(snake.xcor(), 280)

    #collision
    if snake.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape(seg_ver)
        new_segment.penup()
        segs.append(new_segment)
        delay -= 0.001
        score += 10
        pen.clear()
        pen.write("Score : {} ".format(score), align="center", font=("consolas", 24, "bold"))
    # Checking for snake collisions with body segs
    for index in range(len(segs) - 1, 0, -1):
        x = segs[index - 1].xcor()
        y = segs[index - 1].ycor()
        segs[index].goto(x, y)
    if len(segs) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segs[0].goto(x, y)
    move()
    for segment in segs:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segs:
                segment.goto(1000, 1000)
            segs.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {}".format(score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

wn.mainloop()







