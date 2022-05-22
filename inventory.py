# import tabulate 
from tabulate import tabulate

# create class called shoe
class Shoe:
  # create constructor have 5 variable country, code, product, cost, quantity
  def __init__(self, country, code, product, cost, quantity):
      self.country = country
      self.code = code
      self.product = product
      self.cost = cost
      self.quantity = quantity

# create function called "read_data"
def read_data():
  # try-except block
  try:
    # open the text file 
    with open('inventory.txt', 'r') as f:
      # loop though the text file 
      for line in f:
        # print line
        print(line)

  # if filename is there 
  except Exception:
    # print out this
    print("Does not exits")

# create object list
shoe_list = [
            Shoe("South Africa", "SKU44386", "Air Max 90", 2300, 20),
            Shoe("Australia", "SKU57443", "Waffle Racer", 2700, 4),
            Shoe("India", "SKU38773", "Air Max 1", 1900, 29),
            Shoe("United States", "SKU29077", "Cortez", 970, 60),
            Shoe("Vietnam", "SKU95000", "Air Mag", 2000, 2)
            ]

# create function called 'search'
def search(code):
  # create list in the list loop though shoe_list 
  shoes_code = [shoe for shoe in shoe_list if shoe.code == code]
  shoes_qty = [shoe for shoe in shoe_list if shoe.quantity <= 10]
  shoes_high_qty = [shoe for shoe in shoe_list if shoe.quantity > 10]

  # loop shoe in shoes_code 
  # if the code match
  for shoe in shoes_code:
    # print this
    print(f"The code is {shoe.code} and product name is {shoe.product}")

  # loop shoe in shoes_qty 
  # if the quantity is less than 10
  for shoe in shoes_qty:
    # print this
    print(f"This product {shoe.product} is low on quantity {shoe.quantity} restock it")
  
  # loop shoe in shoes_high_qty 
  # if the quantity is hig
  for shoe in shoes_high_qty:
    # print this
    print(f"The product {shoe.product} with high quantities is for sale")

# create new function called "value_per_item"
def value_per_item():

  # loop though shoe_list
  for shoe in shoe_list:
    # calc the total worth of the stock
    value = shoe.cost * shoe.quantity

    # create object list called table
    table = [
            ["Country", "Code", "Product", "Cost", "Quantity", "Total worth"],
            [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity, value]
            ]

    print(" ")
    # print tabulate
    print(tabulate(table, headers='firstrow'))

read_data()
search("SKU44386")
value_per_item()
