'''
Module 4: Portfolio Milestone


Step 1: Build the ItemToPurchase class with the following specifications:

Attributes
item_name (string)
item_price (float)
item_quantity (int)
Default constructor
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()
Example of print_item_cost() output:
Bottled Water 10 @ $1 = $10
'''
class ItemToPurchase:
  def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity

  def print_item_cost(self):
    print(f'{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_quantity * self.item_price)}')

'''
Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.

Example:
Item 1
  Enter the item name:
    Chocolate Chips
  Enter the item price:
    3
  Enter the item quantity:
    1
Item 2
  Enter the item name:
    Bottled Water
  Enter the item price:
    1
  Enter the item quantity:
    10
'''
number_of_items = 2
list_of_ItemToPurchase = []

for i in range(number_of_items):
  print('Item', i+1)
  item_name = input('Enter the item name:\n  ')
  item_price = float(input('Enter the item price:\n  '))
  item_quantity = int(input('Enter the item quantity:\n  '))
  list_of_ItemToPurchase.append(ItemToPurchase(item_name, item_price, item_quantity))

print('\r')
'''
Step 3: Add the costs of the two items together and output the total cost.

Example:
TOTAL COST
Chocolate Chips 1 @ $3 = $3
Bottled Water 10 @ $1 = $10
Total: $13
'''
total_cost = 0
print('TOTAL COST')
for i in range(len(list_of_ItemToPurchase)):
  total_cost += (list_of_ItemToPurchase[i].item_price * list_of_ItemToPurchase[i].item_quantity)
  list_of_ItemToPurchase[i].print_item_cost()
print(f'Total: ${int(total_cost)}')
