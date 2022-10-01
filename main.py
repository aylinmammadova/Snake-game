from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("My snake game")
screen.tracer(0)

# # Creating snake
snake = Snake()
# # Calling a food
food = Food()
score = ScoreBoard()

# # Controlling snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# # Moving a snake
game_is_on = True
while game_is_on:
    screen.update()
    # slowing down
    time.sleep(0.1)
    snake.move()

    # # Detecting collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        score.increase_score()
        food.refresh()

    # # Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
