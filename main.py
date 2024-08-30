import turtle
import random
import time
screen=turtle.Screen()
snakeparts=[] 
screen.bgcolor("lightblue")
screen.colormode(255)
snake=turtle.Turtle()
food=turtle.Turtle()
food.shape("circle")
food.color("pink")
snake.shape("square")
snake.color("orange")
food.penup()
food.goto(200,80)
snake.penup()
def snakedown():
  snake.setheading(270)
def snakeleft():
  snake.setheading(180)
def snakeright():
  snake.setheading(0)
def snakeup():
  snake.setheading(90)
def move():
  snake.forward(20)
run=True
screen.listen()
screen.onkey(snakeup,"w")
screen.onkey(snakedown,"s")
screen.onkey(snakeright,"d")
screen.onkey(snakeleft,"a")
def randomcolor():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  color=(r,g,b)
  return color
while run:
  move()
  screen.update()
  time.sleep(0.01)
  if snake.distance(food)<20:
    food.goto(random.randint(-300,450),(random.randint(-200,243)))
    snake1=turtle.Turtle()
    snake1.shape("square")
    snake1.color(randomcolor())
    snake1.up()
    snakeparts.append(snake1)
  for i in range(len(snakeparts)-1,0,-1):
    x=snakeparts[i-1].xcor()
    y=snakeparts[i-1].ycor()
    snakeparts[i].goto(x,y)
  if len (snakeparts)>0:
     x=snake.xcor()
     y=snake.ycor()
     snakeparts[0].goto(x,y)










screen.mainloop()