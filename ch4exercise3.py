#Allyson Gamboa 03/12/2019

# pg.203 exercise 4-3

# Budget analysis

# gets amount user budgets for month
#loop prompts the user to enter each expense
#keeps a running total
#program displays the amount that the user is
#above or below budget

#input
amountbudgeted = float(input("Enter your budget amount: "))
 #expense = float(input("Please enter an expense amount: "))
 #moreExpenses = input("Are there any additional expenses? [type 'y' for yes]")

#constants

# intialize loop/variables
moreExpenses = "y"
totalExpense = 0.0
expense= 0.0
#overbudget calculations = (totalExpense - amountbudgeted)
#underbudget calculations = (amountbudgeted - totalExpense)

#output
while moreExpenses == "y":
     expense = float(input("Please enter an expense amount: "))
     totalExpense += expense
     moreExpenses = input("Are there any additional expenses? [type 'y' for yes]")
     overbudget = (totalExpense - amountbudgeted)
     underbudget = (amountbudgeted - totalExpense)
     
if totalExpense > amountbudgeted:
     print("You are over budget by $" + format(overbudget, '.2f'))
     
elif amountbudgeted > totalExpense:
     print("You are under budget by $" + format(underbudget, '.2f'))
     
else:
     print("You met your budget of $" + format(amountbudgeted, '.2f'))
