# We will make a bouncing ball
import time
import os


ball = "🥎"
postion = 0
width = 50
direction = 1

for i in range(5):
    os.system("cls" if os.name == "nt" else "clear")
    print(" " * postion + ball)

    position += direction
    if position == width or postion == 0:
        direction *= -1