# Exam Programming Prob 2 Nested Decision Stuctures

# Allyson Gamboa 02/21/2019

# amount program

# program gets users input and displays
# the greater amount between amount1 and amount2

# Input Variables
amount1= 0

amount2 = 0

amount1 = int(input('Please enter the first amount: '))

amount2 = int(input('Please enter the second amount: '))

# Output Variables


if amount1 >= 10 and amount2 <= 100:
     print('amount1: ' + str(amount1) + ',' + 'amount2: ' + str(amount2))

     if amount1 == amount2:
          print('These amounts are equal to eachother.')
     else:
          print()
          

else:
     print('amount2: ' + str(amount2) + ',' + 'amount1: ' + str(amount1))
