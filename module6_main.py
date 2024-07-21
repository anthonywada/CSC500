'''
Step 5: In the main section of your code, implement the print_menu() function. print_menu() has a ShoppingCart 
parameter and outputs a menu of options to manipulate the shopping cart. Each option is represented by a single 
character. Build and output the menu within the function.

If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement Quit before implementing 
other options. Call print_menu() in the main() function. Continue to execute the menu until the user enters q to 
Quit.

Step 6: Implement Output shopping cart menu option. Implement Output item's description menu option.
'''
from module6_ItemToPurchase import ItemToPurchase
from module6_ShoppingCart import ShoppingCart
from datetime import date

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
      item_price = float(input("Enter the item price:\n  "))
      item_quantity = int(input("Enter the item quantity:\n  "))
      item_description = input("Enter the item description:\n  ")
      shoppingCart.add_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))
    elif user_input == "r":
      print("\nREMOVE ITEM FROM CART")
      item_name = input("Enter the item name to remove:\n  ")
      shoppingCart.remove_item(item_name)
    elif user_input == "c":
      print("\nCHANGE ITEM QUANTITY")
      modify_item_name = input("Enter the item name:\n  ")
      item_new_quantity = int(input("Enter the item's new quantity:\n  "))
      shoppingCart.modify_item(ItemToPurchase(item_name = modify_item_name, item_quantity = item_new_quantity))
    elif user_input == "i":
      print("\nOUTPUT ITEM'S DESCRIPTIONS")
      shoppingCart.print_descriptions()
    elif user_input == "o":
      print("\nOUTPUT SHOPPING CART")
      shoppingCart.print_total()
    print("\n")
    user_input = input(menu).strip().lower()

customer_name = input("Customer name: ")
current_date = date.today().strftime('%B') + " " + date.today().strftime('%d') + ", " + date.today().strftime('%Y')
print_menu(ShoppingCart(customer_name, current_date))
