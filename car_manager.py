from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.number_of_cars = 20
        for i in range(self.number_of_cars):
            self.create_car()

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape('square')
        car.shapesize(stretch_len=2, stretch_wid=1)
        random_color = random.randint(0, 5)
        car.color(COLORS[random_color])
        random_y = random.randint(-250, 230)
        random_x = random.randint(-280,250)
        car.goto(random_x, random_y)

        self.cars.append(car)

    def move_car(self):
        for car in self.cars:

            if car.xcor() < -260:
                new_x = 250
                new_y = random.randint(-250, 230)
                car.goto(new_x, new_y)

            else:
                x = car.xcor()-STARTING_MOVE_DISTANCE
                y = car.ycor()
                car.goto(x, y)











