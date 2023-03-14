'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''


# Create an empty list to store ingredient costs
def get_ingredient_costs():
  ingredient_costs = []

  # Get user input for ingredient names and costs
  num_ingredients = int(input("How many ingredients are in the recipe? "))
  for i in range(num_ingredients):
    ingredient_name = input("Enter the name of ingredient #" + str(i + 1) +
                            ": ")
    ingredient_cost = float(
      input("Enter the cost of " + ingredient_name + ": $"))
    ingredient_quantity = float(
      input("Enter the quantity of " + ingredient_name + ": "))
    ingredient_costs.append(
      (ingredient_name, ingredient_cost, ingredient_quantity))

  return ingredient_costs


def main():
  while True:
    ingredient_costs = get_ingredient_costs()

    # Calculate the total cost of ingredients
    total_cost = 0
    for ingredient in ingredient_costs:
      total_cost += ingredient[1] * ingredient[2]

    # Print the total cost
    print("The total cost of ingredients is: $" + str(total_cost))

    # Ask user if they want to retry
    retry = input("Do you want to retry? (Y/N) ")
    if retry.lower() != "y":

      # cost per serving calculator

      # get user inputs
      recipe_name = input("Enter the name of the recipe: ")
      recipe_yield = float(input("Enter the yield (number of servings) of the recipe: "))
      
      
      # calculate cost per serving
      cost_per_serving = total_cost / recipe_yield
      
      # print results
      print("\n")
      print("Recipe name: ", recipe_name)
      print("Recipe yield: ", recipe_yield, " servings")
      print("Total cost: $", format(total_cost, ".2f"))
      print("Cost per serving: $", format(cost_per_serving, ".2f"))
      break

while True:
    print("Type 1 to calculate the cost of total ingredients, 2 to calculate the cost per serving of a meal, or 3 to quit the program")
    user_action = input("What would you like to do?")
    if user_action == '1':
      print("dog")
    elif user_action == '2':
      print("cat")
    elif user_action == '3':
      break
    else:
      print("Invalid option")
      continue
   
       
