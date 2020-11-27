from turtle import Turtle

FONT = ("Courier", 15, "normal")
G_font=("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.level = 1
        self.write(f'level:{self.level}', align="center", font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align="center",font=G_font)

    def level_up(self):
        self.level+=1
        self.clear()
        self.write(f'level:{self.level}', align="center", font=FONT)



