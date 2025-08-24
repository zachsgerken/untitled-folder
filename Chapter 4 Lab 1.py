#Zach Gerken, Chapter 4 Lab 1, September 5 2022

#Jane's Stuff Store
print('Jane\'s Stuff Store\n')
#How many items would you like to purchase?
items = int(input('How many items would you like to purchase? '))
total = 0
for num in range(1, items + 1):
    item_value = float(input('Enter the price of the item: $'))
    total += item_value
print('\nThe total cost of your items is $',format(total, '.2f'), sep='')
average = total / items
print('The average cost of each item is $',format(average, '.2f'), sep='')

