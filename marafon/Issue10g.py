from turtle import Turtle, Screen
from time import sleep


def can_exit(maze: list) -> bool:
    """
    Passing the Maze
    """
    length = len(maze[0])
    height = len(maze)

    # Special cases
    if not height or not length or maze[0][0]:
        return False
    # if height == 1:
    #     return not any(maze[0])
    # if length == 1:
    #     return not any(row[0] for row in maze)
    # if maze[0][0] or maze[-1][-1] or (maze[0][1] and maze[1][0]) or (maze[-1][-2] and maze[-2][-1]):
    #     return False

    # Some useful variables
    y = x = direction = 0
    ymax = height - 1
    xmax = length - 1
    bs = 20 * (round(50 * ((length + height) / 15) / (length + height)))  # block size
    xstart = - bs * (length - 1) // 2
    ystart = bs * (height - 1) // 2
    xb = (length + 1) * bs // 2
    yb = (height + 1) * bs // 2

    # Screen setting
    screen = Screen()
    screen.setup((length + 3) * bs, (height + 3) * bs)
    screen.title('Passing the Maze')
    screen.tracer(0)

    # Maze creation
    for block in range(length + 2):
        for i in [1, -1]:
            t = Turtle('square')
            t.penup()
            t.color('green', 'skyblue')
            t.shapesize(bs // 20)
            t.goto(xb - block * bs, i * yb)
    for block in range(height):
        for i in [1, -1]:
            t = Turtle('square')
            t.penup()
            t.color('green', 'skyblue')
            t.shapesize(bs // 20)
            t.goto(i * xb, ystart - block * bs)
    for n, row in enumerate(maze):
        ty = ystart - n * bs
        for m, spot in enumerate(row):
            tx = m * bs + xstart
            if spot:
                t = Turtle('square')
                t.penup()
                t.shapesize(bs // 20)
                t.color('green', 'grey')
                t.goto(tx, ty)

    # Turtle creation
    tim = Turtle('turtle')
    tim.penup()
    tim.shapesize(round(bs / 30))
    tim.color('lightgreen', 'darkgreen')
    tim.goto(xstart, ystart)
    tim.pensize(bs // 4)
    tim.pendown()
    screen.update()
    screen.tracer(1)

    # Some helpful functions
    def right_wall() -> bool:
        if direction == 0:  # East direction
            return y == ymax or maze[y + 1][x]
        if direction == 90:  # North direction
            return x == xmax or maze[y][x + 1]
        if direction == 180:  # West direction
            return not y or maze[y - 1][x]
        if direction == 270:  # South direction
            return not x or maze[y][x - 1]

    def free_way() -> bool:
        if direction == 0:  # East direction
            return x < xmax and not maze[y][x + 1]
        if direction == 90:  # North direction
            return y and not maze[y - 1][x]
        if direction == 180:  # West direction
            return x and not maze[y][x - 1]
        if direction == 270:  # South direction
            return y < ymax and not maze[y + 1][x]

    def step() -> tuple:
        if direction == 0:  # East direction
            return y, x + 1
        if direction == 90:  # North direction
            return y - 1, x
        if direction == 180:  # West direction
            return y, x - 1
        if direction == 270:  # South direction
            return y + 1, x

    # Let's go!
    while x != xmax or y != ymax:
        if not right_wall():
            direction -= 90
            if direction == -90:
                direction = 270
            y, x = step()
            tim.setheading(direction)
            tim.forward(bs)
        elif right_wall() and free_way():
            y, x = step()
            tim.forward(bs)
        else:
            direction += 90
            if direction == 360:
                direction = 0
            tim.setheading(direction)
        if not (x or y) and direction == 180:
            sleep(1)
            screen.clear()
            return False
    # screen.exitonclick()
    sleep(1)
    screen.clear()
    return True


if __name__ == '__main__':
    print(can_exit([[0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 1, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 0]]))
    print(can_exit([[0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 1, 0, 0, 1, 1],
                    [1, 0, 0, 0, 0, 1, 1],
                    [1, 1, 0, 1, 0, 0, 1],
                    [1, 1, 0, 0, 1, 1, 1]]))
    print(can_exit([[0, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1]]))
    print(can_exit([[0, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [1, 1, 1, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 0]]))
    print(can_exit([[0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                    [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0]]))
    print(can_exit([[0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
                    [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0]]))
    print(can_exit([[0, 0, 0, 0, 1, 0, 0]]))
    print(can_exit([[0], [0], [1], [0], [0]]))
