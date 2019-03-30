# Allyson Gamboa   02/19/2019   
 
# Pg 152 exercise 3

# Age Classifier
# input gets a persons age and displays message 
#indicating whether person is an infant, a child, a teenager, or an adult.

# Input variables
person_age = 0

# Output/parameters
infant = person_age <= 1
child = person_age > 1 and person_age < 13
teenager = person_age == 13 or person_age < 20
adult = person_age <= 20 

#prompt
person_age = int(input('Please enter age: '))

if person_age <= 1:
     print('This is the age of an Infant')
elif person_age > 1 and person_age < 13:
     print('This is the age of a Child')
elif  person_age == 13 or person_age < 20:
     print('This is the age of a Teenager')
else:
     person_age <= 20
     print('This is the age of an Adult') 

     
