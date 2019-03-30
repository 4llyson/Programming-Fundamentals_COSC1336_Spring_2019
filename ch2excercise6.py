#Allyson Gamboa 02/12/2019
#
#Ch 2 Excercise 6
#
#SalesTax
#
#Program will compute state and county tax on an item
#
#Input(s)
#    purchase
#Output(s)
#    purchase, statetax, countytax, totaltax, totalsale
#
#get purchase amount from user
purchase = float(input('Please enter the amount of your puchase: ' ))
#
#calculate statetax (.05)
statetax = float(purchase * .05 )
#
#calculate countytax (.025)
countytax = float(purchase * .025 )
#
#calculate totaltax amount
totaltax = float(statetax + countytax )
#
#calculate total sale
totalsale = float(purchase + totaltax )
#
#display reciept with all outputs
print('Purchase amount: ' , format(purchase, '.2f'))
print('State Tax: ' , format(statetax, '.2f'))
print('County Tax: ' , format(countytax, '.2f'))
print('Total Tax: ' , format(totaltax, '.2f'))
print('Total Sale: ' , format(totalsale, '.2f'))


