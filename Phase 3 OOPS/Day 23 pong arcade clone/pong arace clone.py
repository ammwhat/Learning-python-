from turtle import Turtle, Screen
import random
import time

#The screen setup 
screen = Screen()
screen.setup(height = 600, width = 800)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong Arcade")

# game mode selection 
screen.listen()
game_mode = screen.textinput("Game Mode", "Type '1' for Single Player, '2' for Multiplayer:")
control_type = "keyboard"

if game_mode == "1":
    control_type = screen.textinput("Single Player Controls", "Type 'mouse' or 'keyboard':")
    if control_type:
        control_type = control_type.lower()

# the paddle class
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def up(self):
       new_y = self.ycor() + 40
       self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
       
     

# the ball classs
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = random.choice([-12,12])
        self.y_move = 12
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def reset_position(self):
        self.goto(0,0)
        self.x_move *= -1

# scorecard class
class Scorecard(Turtle):
    def __init__(self,poisition):
        super().__init__()
        self.score = 0 
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(poisition)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}", align = "center", font = ("Courier", 50, "bold"))     

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

#class gameover 
# writes win on the side which gets to 10 points first
class Gameover(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.goto(position)      
        self.write("WIN", align = "center", font = ("Courier", 50, "bold"))    

# boundary class
class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")           
        self.penup()
        self.shape("square")
        self.goto(0,280)
        self.setheading(270)
        for _ in range(0,15):
            self.stamp()
            self.forward(40)

# Game setup
r_paddle = Paddle([380,0])
l_paddle = Paddle([-380,0])
ball = Ball()            
boundary = Boundary()
l_scorecard = Scorecard([-50,220])
r_scorecard = Scorecard([50,220])
canvas = screen.getcanvas()

def track_mouse(event):
    new_y = 300- event.y
    if new_y > 250:
        new_y = 250
    elif new_y < -250:
        new_y = -250
    r_paddle.goto(r_paddle.xcor(), new_y)

if game_mode == "1":
    # Single Player Setup
    if control_type == "mouse":
        canvas.bind("<Motion>", track_mouse)
    else:
        screen.onkeypress(r_paddle.up, "Up")
        screen.onkeypress(r_paddle.down, "Down")
else:
    # Multiplayer Setup
    screen.onkeypress(r_paddle.up, "Up")
    screen.onkeypress(r_paddle.down, "Down")
    screen.onkeypress(l_paddle.up, "w")
    screen.onkeypress(l_paddle.down, "s")
screen.listen()    

def ai_move():
    if l_paddle.ycor() < ball.ycor() and l_paddle.ycor() < 250:
        l_paddle.goto(l_paddle.xcor(), l_paddle.ycor() + 15)
    elif l_paddle.ycor() > ball.ycor() and l_paddle.ycor() > -250:
        l_paddle.goto(l_paddle.xcor(), l_paddle.ycor() - 15)

# Main game loop 
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.04)
    ball.move()

    if game_mode == "1":
        ai_move()

    # logic for ball bouncing wrt wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_move *= -1
    # logic for ball bouncing wrt paddle, xcor() = 340; 380-(20+20) 20 for ball 20 for paddle
    if (r_paddle.distance(ball) < 50 and ball.xcor() > 340 and ball.x_move >0 ) or (l_paddle.distance(ball) < 50 and ball.xcor() < -340 and ball.x_move < 0):
        ball.x_move *= -1
    # increasing score based on which sides couldnt touch the ball
    # making the ball come to the side which scores 
    if ball.xcor() > 400:
        l_scorecard.increase_score()
        ball.reset_position()
    if ball.xcor() < -400:
        r_scorecard.increase_score()
        ball.reset_position()
    # displaying win using game_over based on whichever side scores 10 first
    
    if r_scorecard.score == 10:
        game_is_on  = False
        game_over = Gameover([200,0])

    if l_scorecard.score == 10:
        game_is_on = False
        game_over = Gameover([-200,0])    

screen.exitonclick()