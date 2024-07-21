'''
ItemToPurchase class from Module 4, Step 1
'''

class ItemToPurchase:
  def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity
    self.item_description = item_description

  def print_item_cost(self):
    print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_quantity * self.item_price)}")
