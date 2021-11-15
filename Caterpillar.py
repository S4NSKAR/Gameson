#IMPORT LIBRARIES
import turtle as t
import random as rd
from tkinter import messagebox

#BACKGROUND
t.bgcolor('yellow')
#CREATE CATERPILLAR
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

#CREATE LEAF
leaf_shape = ((0,0),(14,2),(18,6),(30,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf = t.Turtle()
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

#CREATE START TEXT
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',font=('Megrim',24,'bold'))
text_turtle.hideturtle()

#CREATE SCORE
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

#FIND IF SNAKE IS WITHIN WALL
def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpillar.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

#DEFINE GAME OVER
def game_over():
    caterpillar.color('red')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))
    t.setposition(150,255)
    t.write('Score : ', font=('Agency FB', 30, 'bold'))
    messagebox.showinfo('Creators : ', 'Developed by : \nSanskar \nRishabh \nGourav \nDevanshu')

#DEFINE/UPDATE SCORE
def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-80
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

#PLACE RANDOM LEAF
def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()


def start_game():

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 2
    caterpillar.shapesize(0.1,caterpillar_length,20)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf)<30:
            place_leaf()
            caterpillar_length = caterpillar_length + 0.5
            caterpillar.shapesize(0.1,caterpillar_length,20)
            caterpillar_speed = caterpillar_speed + 0.2
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
