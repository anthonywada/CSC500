'''
Final project submission:
Create an online shopping cart with an interface to manipulate the cart and view
its contents.
'''

class ItemToPurchase:
  '''Defines a new item name, price, quantity, and description'''
  def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity
    self.item_description = item_description

  def print_item_cost(self):
    print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_quantity * self.item_price)}")

class ShoppingCart:
  '''Defines shopping cart with instances of ItemToPurchase, and methods to
     interact with the cart contents'''
  def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
    self.customer_name = customer_name
    self.current_date = current_date
    self.cart_items = []

  def add_item(self, ItemToPurchase):
    '''Adds an item to cart_items list. Has parameter ItemToPurchase.
       Does not return anything.'''
    self.cart_items.append(ItemToPurchase)

  def remove_item(self, ItemNameToRemove):
    '''Removes item from cart_items list. Has a string (an item's name) parameter.
       Does not return anything.'''
    removed = 0
    for i, item in enumerate(self.cart_items):
      if item.item_name == ItemNameToRemove:
        self.cart_items.pop(i)
        removed = 1
    if removed != 1:
      print("Item not found in cart. Nothing removed.")

  def modify_item(self, ItemToPurchase):
    '''Modifies an item's description, price, and/or quantity.
       Has parameter ItemToPurchase. Does not return anything.'''
    modified = 0
    for i, item in enumerate(self.cart_items):
      if item.item_name == ItemToPurchase.item_name:
        if ItemToPurchase.item_description != "none":
          self.cart_items[i].item_description = ItemToPurchase.item_description
        if ItemToPurchase.item_price != 0:
          self.cart_items[i].item_price = ItemToPurchase.item_price
        if ItemToPurchase.item_quantity != 0:
          self.cart_items[i].item_quantity = ItemToPurchase.item_quantity
        modified = 1
    if modified != 1:
      print("Item not found in cart. Nothing modified.")

  def get_num_items_in_cart(self):
    '''Returns quantity of all items in cart. Has no parameters.'''
    num_items_in_cart = 0
    for i, item in enumerate(self.cart_items):
      num_items_in_cart += item.item_quantity
    return num_items_in_cart

  def get_cost_of_cart(self):
    '''Determines and returns the total cost of items in cart. Has no parameters.'''
    cost_of_cart = 0
    for i, item in enumerate(self.cart_items):
      cost_of_cart += item.item_price * item.item_quantity
    return cost_of_cart

  def print_total(self):
    '''Outputs total of objects in cart'''
    if len(self.cart_items) == 0:
      print("SHOPPING CART IS EMPTY")
    else:
      print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
      print("Number of Items:", self.get_num_items_in_cart())
      for i, item in enumerate(self.cart_items):
        item.print_item_cost()
      print(f'Total: ${self.get_cost_of_cart()}')

  def print_descriptions(self):
    '''Outputs each item's description'''
    print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
    print("Item Descriptions")
    for i, item in enumerate(self.cart_items):
      print(f"{item.item_name}: {item.item_description}")

def print_menu(shoppingCart):
  menu = ("MENU\n"
          "a - Add item to cart\n"
          "r - Remove item from cart\n"
          "c - Change item quantity\n"
          "i - Output items' descriptions\n"
          "o - Output shopping cart\n"
          "q - Quit\n"
          "Choose an option: ")
  user_input = input(menu).strip().lower()
  while user_input != "q":
    if user_input == "a":
      print("\nADD ITEM TO CART")
      item_name = input("Enter the item name:\n  ")
      item_description = input("Enter the item description:\n  ")
      item_price = float(input("Enter the item price:\n  "))
      item_quantity = int(input("Enter the item quantity:\n  "))
      shoppingCart.add_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))
    elif user_input == "r":
      print("\nREMOVE ITEM FROM CART")
      item_name = input("Enter name of item to remove:\n  ")
      shoppingCart.remove_item(item_name)
    elif user_input == "c":
      print("\nCHANGE ITEM QUANTITY")
      modify_item_name = input("Enter the item name:\n  ")
      item_new_quantity = int(input("Enter the new quantity:\n  "))
      shoppingCart.modify_item(ItemToPurchase(item_name = modify_item_name, item_quantity = item_new_quantity))
    elif user_input == "i":
      print("\nOUTPUT ITEM'S DESCRIPTIONS")
      shoppingCart.print_descriptions()
    elif user_input == "o":
      print("\nOUTPUT SHOPPING CART")
      shoppingCart.print_total()
    print("\n")
    user_input = input(menu).strip().lower()

customer_name = input("Enter customer's name: ")
current_date = input("Enter today's date: ")

print(f"Customer name: {customer_name}\nToday's date: {current_date}\n")
print_menu(ShoppingCart(customer_name, current_date))
