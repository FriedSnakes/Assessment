'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''



#function to record ingredient name and cost
import json
import os

def file(ingredient_name, ingredient_cost):
    ingredient_list = {ingredient_name: ingredient_cost}
    file_name = input("What do you want the file name to be? ")
    try:
        with open(file_name, "w") as f:
            f.write(json.dumps(ingredient_list))
    except Exception as e:
        print("An error occurred while writing to the file:", e)

   
       
# Create an empty list to store ingredient costs
def ingredient_cost_calculator():
  while True:
    ingredient_costs = []
    
    # Get user input for ingredient names and costs
    num_ingredients = int(input("\nHow many ingredients are in the recipe? "))
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

    # Ask user if they want to retry
    retry = input("Do you want to retry? (Y/N) ")
    if retry.lower() == "y":
      continue
    else:
      print("")
      print("")
      print("")
      break

def cost_per_serving_calculator():
  while True:
    # Step 1: Define variables
    total_cost = 0.0
    num_servings = 0
    cost_per_serving = 0.0
    
    # Step 2: Get user input
    total_cost = float(input("Enter the total cost of the meal: "))
    num_servings = int(input("Enter the number of servings the meal can make: "))
    
    # Step 3: Calculate the cost per serving
    cost_per_serving = total_cost / num_servings
    
    # Step 4: Print the result
    print("The cost per serving of the meal is: $", format(cost_per_serving, '.2f'))
    print("")
    print("")
    print("")
    break

#function to clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
#Title

print("____________Meal Cost Calculator!____________")
print("")
print("")
print("")


while True:
  print("Welcome to the meal cost calculator. You have 4 options before you")
  print("Option 1: Calculate the total cost of ingredients")
  print("Option 2: Calculate the average cost per serving of a meal")
  print("Option 3: Quit the program")
  print("Option 4: Clear your console")
  user_action = input("What would you like to do?\n")
  if user_action == '1':
    print("\nYou are calculating the total ingredient cost of a meal\n")
    ingredient_cost_calculator()
    continue
  elif user_action == '2':
    print("\nYou are calculating the cost per serving of a meal\n")
    cost_per_serving_calculator()
    continue
  elif user_action == '3':
    print("\nQuitting program!")
    break
  elif user_action == '4':
    cls()
    continue
  else:
    print("Invalid option\n")
    continue