from turtle import Turtle, Screen
import random 
import time

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# the player class
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        self.forward(30)   

    def reset(self):
        self.goto(0, -280)   

class Carmanager():
    def __init__(self):
        self.allcars = []
        self.car_speed = 10

    def create_car(self):
        winning_number = 2
        chance = random.randint(1,6)
        car_color = ["blue", "green" , "yellow"]
        if winning_number == chance:
            new_car = Turtle()
            new_car.color(random.choice(car_color))
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.allcars.append(new_car)

    def move(self):
        for car in self.allcars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.car_speed += 10

    def clear_cars(self):
        for car in self.allcars:
            car.hideturtle()    
        self.allcars.clear()    
        self.car_speed = 10

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-270,270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"{self.level}", align="center", font = ("courier", 20, "bold"))

    def increase_level(self):
        self.level += 1
        self.update_level()    

class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.hideturtle()
        self.write("GAME OVER\npress 'r' to restart", align= "center", font = ("arial", 24, "bold"))
        
def reset_game():
    global game_is_on
    player.showturtle()
    game_over.clear()
    player.reset()
    level.level = 1
    level.update_level()
    player.reset()
    game_is_on = True

# game setup
player = Player()
car_mananger = Carmanager()
screen.listen()
screen.onkey(player.move, "Up")
level = Level()

#game loop
game_is_on = True
while True:
    screen.update()
    time.sleep(0.1)
    if game_is_on:
     car_mananger.create_car()
     car_mananger.move()
     for car in car_mananger.allcars:
         if player.distance(car) < 30:
            game_is_on = False
            game_over = Gameover()
            car_mananger.clear_cars()
            player.hideturtle()
            screen.update()
            screen.listen()
            screen.onkey(reset_game, "r")
            time.sleep(1.4)
         if player.ycor() > 280:
             level.increase_level()
             car_mananger.level_up()
             player.reset()
            




        









   
    