from turtle import *
screensize(1000, 1000)
tracer(20)
left(90)
down()
k = 20
right(315)
for i in range(7):
    forward(12 * k)
    right(45)
    forward(6 * k)
    right(135)
up()
for y in range(-30, 30):
    for x in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'red')
done()
