#Allyson Gamboa 02/12/2019
#
#Ch2 Excercise 4
#
#TotalPurchase
#
#Program displays subtotal, sales tax , and total including tax
#
#
#Input(s)
#    pricePerItem1-5
#
#Output(s)
#    subtotal
#    salestax
#    totalWtax
pricePerItem1 = float(input('Please enter the price for your first item: '))
pricePerItem2 = float(input('Please enter the price for your second item: '))
pricePerItem3 = float(input('Please enter the price for your third item: '))
pricePerItem4 = float(input('Please enter the price for your fourth item: '))
pricePerItem5 = float(input('Please enter the price for your fifth item: '))
#
#calculate subtotal
subtotal = float(pricePerItem1 + pricePerItem2 + pricePerItem3 + pricePerItem4 + pricePerItem5 )
#
#calculate sales tax (.07)
salestax = float(pricePerItem1 + pricePerItem2 + pricePerItem3 + pricePerItem4 + pricePerItem5 ) * .07
#
#total with tax
totalWtax = float(subtotal + salestax)
#
#display reciept
print('Your Subtotal is: ' , subtotal)
print('Your Sales Tax is: ' , format(salestax, '.2f'))
print('Your Total is: ' , format(totalWtax, '.2f'))
