# Allyson Gamboa   02/19/2019   
 
# Pg 155 exercise 15

# Time Calculator
 
# Program gets number of seconds from user and
#calculates into days, hours, minutes and seconds. 

# Input variables
number_of_seconds = 0

#constants 
seconds = 59
minutes = 60 
hours = 3600
days = 86400

#Output
calcdays = 0
calchours = 0
calcmins = 0
calcsecs = 0



number_of_seconds = int(input('Enter the number of seconds you want converted: '))

if number_of_seconds > days:
     calcdays = int(number_of_seconds/days)
     calchours = int(days - calcdays) / hours
     calcmins = int(hours - calchours ) / minutes
     calcsecs = int(minutes - calcmins) / seconds
     print (str(int(calcdays)) + 'days ' + str(int(calchours)) + 'hours ' + str(int(calcmins)) + 'mins ' + str(int(calcsecs)) + 'secs' )
     

elif number_of_seconds >= hours:
     calchours = int(number_of_seconds/ hours)
     calcmins = int(hours - calchours ) / minutes
     calcsecs = int(minutes - calcmins) / seconds
     print (str(int(calchours)) + 'hrs '+ str(int(calcmins)) + 'mins ' + str(int(calcsecs)) + 'secs')


elif number_of_seconds >= minutes:
     calcmins = int(number_of_seconds / minutes)
     calcsecs = int(minutes - calcmins) / seconds
     print (str(int(calcmins)) + 'min. '+ str(int(calcsecs)) + 'secs ')



else:
     print (str(number_of_seconds) + 'sec.')










