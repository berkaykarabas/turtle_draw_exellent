import random
import turtle as t
t.colormode(255)

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83), (245, 205, 7), (35, 88, 88), (103, 24, 56)]

my_turtle = t.Turtle()
my_turtle.speed(0)

for i in range(13):
    y = 50*i
    for i in range(14):
        x = 50*i
        my_turtle.penup()
        my_turtle.setposition(-325+x,-300+y)
        my_turtle.pendown()
        my_turtle.dot(30,random.choice(color_list))
        my_turtle.hideturtle()
screen = t.Screen()
screen.mainloop()