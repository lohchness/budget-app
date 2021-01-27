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

# Printing __str__()
# description - slice up to 23rd character, .ljust 23 spaces
# amount - slice up to 7th character, round(amount, 2) for decimal 
# Total: self.get_balance() and round to 2 decimal points
# or use format() function

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
    if amount <= self.get_balance():
      return True
      # Did not work with the test "test_withdraw_no_funds" (line 67) when it was int(amount) instead of just amount. Why?
    else:
      return False
      # Working

  def withdraw(self, amount, description=""):
    if self.check_funds(amount) is True:
      self.ledger.append({"amount": 0-amount, "description":description})
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

  def __str__(self):
    receipt = ""
    receipt = receipt + self.name.center(30, "*") + "\n"
    for i in self.ledger:
      j = i["amount"]
      k = i["description"]
      # receipt += f"{i['description'][:23].ljust(23)}{str(float(round(j, 2))).rjust(7)}\n"
      # format(value, '.2f')
      receipt += f'{k[:23].ljust(23)}{format(j, ".2f").rjust(7)}\n'
      # Items in ledger
    
    # Total amount, no need for justification
    receipt += f"Total: {format(self.get_balance(), '.2f')}"
    return receipt
    # Working
    # Format function better to use than round() function

def create_spend_chart(categories):

  amount_spent = []
  spent_percent = []
  total_spent = 0

  for i in categories:
    total_spent = 0
    for item in i.ledger: # Each item from each category
      if item['amount'] < 0:
       total_spent -= item['amount']
    amount_spent.append(round(total_spent, 2)) # <-- reason why graph circles were wrong, did not indent in the correct place
  # All values are now in the amount_spent list

  for amount in amount_spent:
    spent_percent.append(round(amount/sum(amount_spent),2)*100)

  #for i in categories:
  #  for j in i.ledger:
  #    total_spent += i.ledger
  #  spent_percent.append(round(i.ledger()/total_spent)*100)


  # Bar Chart
  # Goes through each of the values row by row on the chart

  chart = "Percentage spent by category\n"

  i = 100 # Y-Axis - Count down 100 to 0 with increments of 10 
  while i >= 0:
    chart += str(i).rjust(3) + "| "
    for j in spent_percent:
      if j >= i:
        chart += "o"
      else:
        chart += " "
      chart += "  "
    chart += "\n"
    i -= 10
    # FIXED - Chart is adding the o's 90 degrees CCW for some reason????
      # Will check code above to see if it is wrong with the way I am adding the values to the list

  chart += "    "
  chart += "---"*len(categories)
  chart += "-\n     "
  # End graph circles

  # Names on the chart
  cat_names = []

  for category in categories:
    cat_names.append(str(category.name)) # Puts cats into list

  longest_name = 0
  #longest_name = max(cat_names, key=len)
  # doesnt work for some reason, have to use below for loop
  for name in cat_names:
    if len(name) > longest_name:
      longest_name = len(name)
      # Checks through the names, updates when it encounters a name longer than the current name
  


  # Need length of longest name to test adding the names to the X-Axis
  
  for x in range(longest_name):
    for y in cat_names:
      if len(y) > x:
        chart += y[x]
        chart += "  "
      else:
        chart += "   "
    if x < longest_name - 1:
      chart += "\n     "
  
  return chart