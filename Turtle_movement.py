import turtle
state = 0


def move_up():
    global state
    if state != 1:
        turtle.setheading(90)
        state = 1
    else:
        turtle.forward(20)


def move_right():
    global state
    if state != 2:
        turtle.setheading(360)
        state = 2
    else:
        turtle.forward(20)


def move_left():
    global state
    if state != 3:
        turtle.setheading(180)
        state = 3
    else:
        turtle.forward(20)


def move_down():
    global state
    if state != 4:
        turtle.setheading(270)
        state = 4
    else:
        turtle.forward(20)


turtle.onkey(move_up, "Up")
turtle.onkey(move_right, "Right")
turtle.onkey(move_left, "Left")
turtle.onkey(move_down, "Down")

turtle.listen()
turtle.done()