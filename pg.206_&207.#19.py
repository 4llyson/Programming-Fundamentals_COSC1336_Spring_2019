#Allyson Gamboa 03/26/2019

# pg. 206 # 19

# stop sign with stop written in the middle

import turtle
turtle.fillcolor('red')
turtle.begin_fill()
start_x=-200        #starting x coordinate
start_y=0           #starting y coordinate
num_lines=8         #number of lines drawn
line_length=100     #length of lines
angle=60           # angle of turn

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
     

#write stop
turtle.penup()
turtle.goto(-210,55)

turtle.pendown()
turtle.pensize(800)
turtle.end_fill()
turtle.write('STOP', font=("Impact", 50))

#end program
