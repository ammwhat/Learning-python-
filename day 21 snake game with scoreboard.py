from turtle import Turtle, Screen
import random
import time

#Screen setup 
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# Snake class
class Snake:
    def __init__(self):
        self.segments = []
        starting_positions = [(0,0),(-20,0),(-40,0)]
        for position in starting_positions:
            self.add_segment(position)
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)
   
    # functions for up,down,right,left with if statemnts so the body doesnt collide with itself 
    # (in degrees) right = 0, up = 90, left = 180, down = 270
    # snake should only move in a certain direction if that move doesnt lead to collision withitself

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segment[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segment.heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment.heading() != 180:
            self.segment[0].setheading(0)

# the food class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid = 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)

# Scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard
     
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score :{self.score}", align = "center", font = ("Arial", 24, "normal") )
 
    def increase_score(self):
        self.score += 1
        self.update_scoreboard

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = ("Arial", 24, "normal"))

# game setup
my_snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left , "Left")
screen.onkey(my_snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    my_snake.move()
    time.sleep(0.05)

    #detect collision with food
    if my_snake.segment[0].distance(food) < 15:
        food.refresh()
        my_snake.extend()
        my_snake.increase_score()
    # collision with wall
    if my_snake.segment[0].xcor() > 280 or my_snake.segment[0].xcor < -280 or my_snake.segment[0].ycor > 280 or my_snake.segment.ycor() < -280:
         game_is_on = False
         score_board.game_over()
    # collision with tail 
    for segment in my_snake.segments[1:]:
        if my_snake.segment[0].distance(segment) < 10:
            game_is_on = False
            score_board.gameover()

screen.exitonlick()

     

  
