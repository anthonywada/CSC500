'''
Step 4: Build the ShoppingCart class with the following data attributes and related methods. Note: Some can be method stubs (empty methods) initially, to be completed in later steps

Parameterized constructor, which takes the customer name and date as parameters

Attributes
  customer_name (string) - Initialized in default constructor to "none"
  current_date (string) - Initialized in default constructor to "January 1, 2020"
  cart_items (list)
Methods
  add_item()
    Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
  remove_item()
    Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    If item name cannot be found, output this message: Item not found in cart. Nothing removed.
  modify_item()
    Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
    If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
  get_num_items_in_cart()
    Returns quantity of all items in cart. Has no parameters.
  get_cost_of_cart()
    Determines and returns the total cost of items in cart. Has no parameters.
  print_total()
    Outputs total of objects in cart.
    If cart is empty, output this message: SHOPPING CART IS EMPTY
  print_descriptions()
    Outputs each item's description.
'''

class ShoppingCart:
  def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
    self.customer_name = customer_name
    self.current_date = current_date
    self.cart_items = []

  def add_item(self, ItemToPurchase):
    self.cart_items.append(ItemToPurchase)

  def remove_item(self, ItemNameToRemove):
    removed = 0
    for i, item in enumerate(self.cart_items):
      if item.item_name == ItemNameToRemove:
        self.cart_items.pop(i)
        removed = 1
    if removed != 1:
      print("Item not found in cart. Nothing removed.")

  def modify_item(self, ItemToPurchase):
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
    num_items_in_cart = 0
    for i, item in enumerate(self.cart_items):
      num_items_in_cart += item.item_quantity
    return num_items_in_cart

  def get_cost_of_cart(self):
    cost_of_cart = 0
    for i, item in enumerate(self.cart_items):
      cost_of_cart += item.item_price * item.item_quantity
    return cost_of_cart

  def print_total(self):
    if len(self.cart_items) == 0:
      print("SHOPPING CART IS EMPTY")
    else:
      print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
      print("Number of Items:", self.get_num_items_in_cart())
      for i, item in enumerate(self.cart_items):
        item.print_item_cost()
      print(f'Total: ${self.get_cost_of_cart()}')

  def print_descriptions(self):
    print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
    print("Item Descriptions")
    for i, item in enumerate(self.cart_items):
      print(f"{item.item_name}: {item.item_description}")
