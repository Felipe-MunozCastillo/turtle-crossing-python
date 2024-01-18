"""Importacion de Turtle para que se 
muestre el puntaje en pantalla"""
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Clase encargada de manejar el puntaje del jugador."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Metodo que actualiza la pantalla con los datos actuales del puntaje."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Metodo para aumentar el puntaje del jugador."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Metodo para mostrar mensaje una vez que el jugador pierde."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
