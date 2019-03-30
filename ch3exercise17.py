
# Allyson Gamboa 02/26/2019

# Wi-fi Diagnostic Tree

# Program guides user through the steps of fixing a bad connection

# constants
yes = True
no = False

#input
problem = yes or no

step1 = False
step2 = False
step3 = False
step4 = False
step5 = False

#output

step1 = print('Reboot the computer and try to connect.')
problem = input('Did that fix the Problem (enter yes or no): ' )   
if step2 == 'no':
     print('Reboot the router and try to connect.')
     problem = input('Did that fix the Problem (enter yes or no):' )
     if step3 == 'no':
          print('make sure the cables between to the router and modem are plugged in firmly.')
          problem = input('Did that fix the Problem (enter yes or no):' )
          if step4 == 'no':
               print('move the router to a new location.')
               problem = input('Did that fix the Problem (enter yes or no):' )
               if step5 == 'no':
                   print('get a new router')


              


              
