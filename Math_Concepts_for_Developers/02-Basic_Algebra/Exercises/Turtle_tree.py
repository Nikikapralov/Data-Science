from turtle import *

def draw_branch(branch_length, angle, size):
    if branch_length > 5:
        pensize(size)
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 15, angle, size / 1.5)
        left(2 * angle)
        draw_branch(branch_length - 15, angle, size / 1.5)
        right(angle)
        backward(branch_length)

def draw_tree(trunk_length, angle, size):
    pensize(size)
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle, size / 1.5)
    done()

draw_tree(100, 30, 25)