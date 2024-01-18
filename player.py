"""Libraria turtle necesaria para la creacion del jugador."""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Clase encargada de la creacion de la tortuga
    manipulada por el jugador"""

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move(self):
        """Metodo de avance del jugador."""
        self.forward(MOVE_DISTANCE)

    def player_crossed(self):
        """Metodo para detectar si el usuario cruzo o no la pantalla."""
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False
