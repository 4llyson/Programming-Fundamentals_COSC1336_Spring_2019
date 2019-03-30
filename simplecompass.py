#Allyson Gamboa 03/26/2019

# pg107 2-24

#shape design

# simple compass labled with directions + circle in the middle
import turtle
turtle.setup(600,400)
turtle.write('east')
turtle.left(180)
turtle.forward(200)
turtle.write('west')
turtle.penup()
turtle.back(100)
turtle.pendown()
turtle.right(90)
turtle.forward(100)

turtle.write('north')
turtle.right(180)
turtle.forward(200)
turtle.write('south')
turtle.penup()
turtle.goto(-128,0)
turtle.pendown()
turtle.circle(30)
#end program
