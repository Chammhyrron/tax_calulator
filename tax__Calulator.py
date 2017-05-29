Sales_tax= 0.065
price = float(input('the total price of the items '))
tax = price*Sales_tax
print('taxes '+str(tax))

total = price+tax
print('this is your total '+str(total))
