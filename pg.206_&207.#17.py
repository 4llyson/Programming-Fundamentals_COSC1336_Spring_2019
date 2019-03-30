#Allyson Gamboa 03/26/2019

# pg. 206 # 17

# star shape with 8 vertices

import turtle
start_x=-200        #starting x coordinate
start_y=0           #starting y coordinate
num_lines=8         #number of lines drawn
line_length=100     #length of lines
angle=135           # angle of turn

#inital positon
turtle.hideturtle()
turtle.penup()
turtle.goto(start_x, start_y)
turtle.pendown()

#draw 8 lines
#by 170 degrees
for x in range(num_lines):
     turtle.forward(line_length)
     turtle.left(angle)
#end program
