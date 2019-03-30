#Allyson Gamboa 3/12/2019

# pg.203 exercise 4-4

# Distance traveled

#gets speed of vehicle from user in mph and
#the number of hours it has traveled, loop displays
#the distance the vehical has traveled

#input
speed = int(input("Please enter the speed of the vehicle: " ))
hoursTraveled = int(input("Please enter the hours spent traveling: "))
#constants
#distance = speed * hoursTraveled
#output
print("Hours\tDistance")
print("__________________")
for hour in range(1, hoursTraveled +1):
     distance = speed * hour
     print(hour,"   ",distance)
