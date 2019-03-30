#Allyson Gamboa 03/12/2019

# pg.205 exercise 4-13

# Population

#this program predicts the approximate size of a population of organisms.
#user enters the starting number of organisms, average daily increase in
#population as a percentage, and number of days organisms will multiply

#input
numberOfOrganisms = int(input("Please enter the starting number of organisms: "))
percentOfIncrease = float(input("Please enter a percent increase: "))
numberOfDays = int(input("Please enter the number of days: "))
day = 0
population = 0
#output
population = numberOfOrganisms
print("Day\tApprox. Popualtion")
print("------------------------")
for day in range (1, numberOfDays +1):
     print(day,"   ",population)
     population = population + (numberOfOrganisms * population)
