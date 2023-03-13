'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''

# Create an empty list to store ingredient costs
ingredient_costs = []

# Get user input for ingredient names and costs
def main():
  num_ingredients = int(input("How many ingredients are in the recipe? "))
  for i in range(num_ingredients):
      ingredient_name = input("Enter the name of ingredient #" + str(i+1) + ": ")
      ingredient_cost = float(input("Enter the cost of " + ingredient_name + ": $"))
      ingredient_quantity = float(input("Enter the quantity of " + ingredient_name + ": "))
      ingredient_costs.append((ingredient_name, ingredient_cost, ingredient_quantity))
  
  # Calculate the total cost of ingredients
  total_cost = 0
  for ingredient in ingredient_costs:
      total_cost += ingredient[1] * ingredient[2]
  
  # Print the total cost
  print("The total cost of ingredients is: $" + str(total_cost))

