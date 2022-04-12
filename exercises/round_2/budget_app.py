'''
# CHALLENGE: Budget App
# Link: https://replit.com/@DaniloBilanoski/boilerplate-budget-app#budget.py

# DESCRIPTION
Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

    A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdraw took place, and False otherwise.
    A get_balance method that returns the current balance of the budget category based on the deposits and withdraws that have occurred.
    A transfer method that accepts an amount and another budget category as arguments. The method should add a withdraw with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.

When the budget object is printed it should display:

    A title line of 30 characters where the name of the category is centered in a line of * characters.
    A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    A line displaying the category total.

Here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdraws and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     


'''

class Category():

  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description=""):
    '''
     A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    '''
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    '''
    The amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdraw took place, and False otherwise.
    '''
    # Validation will go based on the check funds method
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": -abs(amount), "description": description})
      return True
    else:
      return False
  
  def get_balance(self):
    '''
     Returns the current balance of the budget category based on the deposits and withdraws that have occurred.
    '''
    current_balance = 0
    
    for item in self.ledger:
      current_balance += item["amount"]

    return(current_balance)

  def check_funds(self, amount):
    '''
    Accepts an amount as an argument, returns False if the amount is greater than the balance of the budget category and returns True otherwise.
    '''
    current_funds = self.get_balance()
    if amount > current_funds:
      return False
    else:
      return True

  def transfer(self, amount, category):
    '''
    A transfer method that accepts an amount and another budget category as arguments. The method should add a withdraw with the amount and the description "Transfer to [Destination Budget Category]". 
    
    The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    '''

    if self.check_funds(amount) == True:
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount,f"Transfer from {self.name}")
      return True
    else:
      return False


  def __str__(self):
    '''
    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96
    '''
    final_string = list()
    final_string.append(self.name.center(30,"*"))

    total = 0

    for item in self.ledger:
      # Line needs to have ledger item description left alligned and truncated to 23 symbols
      # Line needs to have ledger amount right alligned and truncated to 7 symbols 
      line = f"{item['description'][:23].ljust(23)}{str('{:.2f}'.format(item['amount']))[:7].rjust(7)}"
      final_string.append(line)
      # Counting sum of leger item amounts
      total += item['amount']
    
    final_string.append(f"Total: {float(str('{:.2f}'.format(total))[:30].ljust(30))}")

    return(str("\n".join(final_string)))

def create_spend_chart(categories):
  '''
  Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g  
  '''
  # Calculate money spent per category, add to dicionary
  expenses = dict()
  total_expense = 0
  print(categories)
  for category in categories:

    expense = 0
    
    for item in category.ledger:
      if item['amount'] < 0:
        expense += abs(item['amount'])
        total_expense += abs(item['amount'])

    expenses[category.name] = expense
  
  # Sort the dictionary and put percentages out of total as values
  # My version - sorts the data in the descending order so graph is easier to read, assignemnt did not include this
  '''
  # ORIGINAL ASSIGMENT (Without sorting the data)

  # Rework the dictionary to put percentages out of total as values
  sorted_expenses = dict()
  for key, value in expenses.items():
    sorted_expenses[key] = int((((value/total_expense)*10)//1)*10)
  '''
  sorted_amounts = sorted(expenses.values(),reverse=True)
  sorted_expenses = dict()

  for amount in sorted_amounts:
    for key in expenses.keys():
      if expenses[key] == amount:
        # We need to round down a number to the nearest 10
        sorted_expenses[key] = int((((amount/total_expense)*10)//1)*10)
  print(sorted_expenses)

    # Create chart graph
  chart_header = "Percentage spent by category\n"
  chart_graph = str()

  # In range from 100 to 10 with step 10, check if each tenth should have a dot on chart by comparing a current tenth value to a current expense value
  for tenth in reversed(range(0,101,10)):
    chart_graph += f"{str(tenth).rjust(3)}|"
    for value in sorted_expenses.values():
      if tenth > value:
        chart_graph += 3*" "
      else:
        chart_graph += " o "
    chart_graph += " \n"
  
  # Create chart description items
  chart_series = str()
  # Decorative lines lenght
  chart_series += 4*" " + (len(sorted_expenses)*3+1)*"-"
  # Line height will be the number of symbols in the largest category name
  line_height = max(len(x) for x in sorted_expenses.keys())

  # So for each line in the height take the category name and append the letter at the index number of the current line (will go till end of the largest word in a list)
  # Once done, add "\n" then do next in a list. In case we ran out of letters, catch the error and append empty space

  for line in range(line_height):
    # Start each new line with needed empty space
    chart_series += "\n    "
    for keys in sorted_expenses.keys():
      try:
        chart_series += f"{keys[line].center(3)}"
      except:
        chart_series += 3*" "
    chart_series += " "
    
  print((chart_header + chart_graph + chart_series))
  return(chart_header + chart_graph + chart_series)

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

print(food.get_balance())

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])

print(actual)
