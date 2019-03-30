# Exam Programming Prob3

# Allyson Gamboa 02/21/2019

# Tip, tax, and total program
# program gets meal cost from user then calculates 18 percent tip
# and a 7 percent sales tax. this info is displayed on a reciept with a total.
# Input Variables
mealcost = 0
mealcost = float(input('Please enter the cost of your meal: '))

# constants
tip = .18
tax = .07



# Output 
mealtax = float(mealcost * tax)
mealtip = float(mealcost * tip)
total = float(mealcost + mealtax + mealtip)

print('Tip: ' + str(format(mealtip,'.2f')/n
'Tax :' + str(format(mealtax,'.2f'))/n
'Your total is : ' + str(format(total, '.2f')))
