#Allyson Gamboa 03/26/2019

#pg. 207 #18

# hypnotic square

import turtle
#constant
side=4 #line length
for x in range (1, 27): #line iteration number
     turtle.forward(side) 
     turtle.left(90) #angle of turn
     side=side+10 # length + 10 pixels for every iteration
