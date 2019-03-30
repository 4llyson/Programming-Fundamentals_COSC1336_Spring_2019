#Allyson Gamboa 02/12/2019
#
#pg 104 Exercise 3
#
#LandCalculation
#
#Converts square feet to acres 
#
#Input(s)
#    squareFeet
#
#Output(s)
#    acres
#
#get users total square feet
totalsquarefeet = float(input('Enter total square feet to be converted to acres:  '))
#
#one acre is equal to 43560 square feet
acres = totalsquarefeet / 43560
#
#display number of acres
#
print('The number of acres is:  ' , format(acres , '.2f'))
