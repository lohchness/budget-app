# TO DO LIST 

# Getting "amount" adding it to funds for each deposit
# Do get_balance, then check_funds, then withdraw 
#   get_balance checks the remaining funds left, and check_funds checks if there are enough funds for a certain amount. withdraw needs to see if there are enough funds to complete the transaction, and returns True if it is successful.

# Transfer function needs a budget category? 
#   For Example: Two objects are created, Food and Entertainment. Food transfers some of the money over to Entertainment. The funds are deducted in Food, then the funds are appended into Entertainment.
#   Returns True if successful
# USE THE WITHDRAW AND DEPOSIT METHODS

# How to display a receipt when printing an object?
# def __str__() method

class Category():
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description = ""): # Description defaults to "" if empty, but the other arguments are required
    self.ledger.append({"amount":amount, "description":description})

  def get_balance(self): # Checks how much money there is, a sum of all the "amount" items. Works with negative numbers
    funds = 0
    for amount in self.ledger:
      funds = funds + amount["amount"]
    return funds
    # working
  
  def check_funds(self, amount):
    if int(amount) <= self.get_balance():
      return True
    else:
      return False
      # Working

  def withdraw(self, amount, description=""):
    if self.check_funds(amount) is True:
      self.ledger.append({"amount": -amount, "description":description})
      return True
    else:
      return False
      # working
    
  def transfer(self, amount, category):
    if self.check_funds(amount) is True:
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}") # Backwards for some reason?
      return True
    else:
      return False


def create_spend_chart(categories):
  pass