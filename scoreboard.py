from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
COLOR = "white"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.color(COLOR)
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        """Clear the scoreboard and updates it to new results"""
        self.clear()
        self.write(arg="Score: {} High Score: {}".format(self.score, self.high_score), align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Update high score and set score to 0 for a new game"""
        if self.score > int(self.high_score):
            self.high_score = self.score
            # update file with the highest score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()



