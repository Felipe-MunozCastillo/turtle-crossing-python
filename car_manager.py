"""Importacion de la librerias necesarias"""
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Clase manejadora de vehiculos"""

    def __init__(self):
        self.all_cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Metodo de creacion de autos"""
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Metodo para el movimiento de los automoviles"""
        for car in self.all_cars:
            car.backward(self.cars_speed)

    def speed_up(self):
        """Metodo para aumentar la velocidad de los vehiculos 
        al completar un nivel"""
        self.cars_speed += MOVE_INCREMENT
        for car in self.all_cars:
            car.backward(self.cars_speed)
