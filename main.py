from turtle import Screen
import time
from snake import Snake
from Food import Food
from scoreboard import Score
from Border import Border
window = Screen()
window.setup(height=600, width=600)
window.title("Snake Xenzia")
window.bgcolor("black")
window.tracer(0)
snake = Snake()
food = Food()
score = Score()
window.listen()
border = Border()

window.onkey(fun=snake.up, key="Up")
window.onkey(fun=snake.down, key="Down")
window.onkey(fun=snake.left, key="Left")
window.onkey(fun=snake.right, key="Right")
border.square()
game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.swallowed()
        snake.extend_snake()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    for segments in snake.segments[1:]:
        # if segments == snake.head:
        #     pass
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()





window.exitonclick()
