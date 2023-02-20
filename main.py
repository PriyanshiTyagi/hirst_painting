# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)
import turtle as t
import random

t.colormode(255)
nicky = t.Turtle()
nicky.pu()
nicky.hideturtle()
list = [(230, 177, 60), (41, 123, 156), (151, 19, 58), (2, 177, 143),
        (129, 145, 199), (23, 122, 97), (209, 122, 173), (164, 165, 35), (214, 202, 133), (226, 81, 105),
        (119, 171, 116),
        (19, 40, 92), (231, 101, 48), (167, 47, 79), (29, 162, 221), (135, 119, 169), (146, 105, 53),
        (81, 20, 43), (38, 52, 97), (19, 94, 72), (221, 176, 196), (13, 88, 102), (158, 211, 200), (30, 61, 55),
        (82, 22, 13),
        (134, 22, 19)]
nicky.speed(0)
nicky.setheading(225)

nicky.forward(300)
nicky.setheading(0)

for dots in range(1,101):

    nicky.dot(20, random.choice(list))
    nicky.pu()

    nicky.fd(50)

    if dots%10==0:
        nicky.setheading(90)
        nicky.fd(50)
        nicky.setheading(180)
        nicky.fd(500)
        nicky.setheading(0)


screen = t.Screen()
screen.exitonclick()
