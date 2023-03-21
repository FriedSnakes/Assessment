'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
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

def ingredient_cost_calculator():
    while True:
        ingredient_costs = []
        num_ingredients = int(input("\nHow many ingredients are in the recipe? "))
        
        for i in range(num_ingredients):
            ingredient_name = input("Enter the name of ingredient #" + str(i+1) + ": ")
            ingredient_cost = float(input("Enter the cost of " + ingredient_name + ": $"))
            ingredient_quantity = float(input("Enter the quantity of " + ingredient_name + ": "))
            ingredient_costs.append((ingredient_name, ingredient_cost, ingredient_quantity))
        
        total_cost = sum([ingredient[1] * ingredient[2] for ingredient in ingredient_costs])
        print("The total cost of ingredients is: $" + str(total_cost))

        retry = input("Do you want to retry? (Y/N) ")
        if retry.lower() == "y":
            continue
        else:
            return total_cost

def cost_per_serving_calculator():
    while True:
        total_cost = float(input("Enter the total cost of the meal: "))
        num_servings = int(input("Enter the number of servings the meal can make: "))
        cost_per_serving = total_cost / num_servings

        print("The cost per serving of the meal is: $", format(cost_per_serving, '.2f'))
        
        retry = input("Do you want to retry? (Y/N) ")
        if retry.lower() == "y":
            continue
        else:
            return cost_per_serving

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def view_history():
    try:
        with open('history.txt') as f:
            history = f.read()
            print(history)
    except FileNotFoundError:
        print("No history found")

def save_to_history(entry):
    with open('history.txt', 'a') as f:
        f.write(entry + '\n')



while True:
    print("Welcome to the meal cost calculator. You have 4 options before you")
    print("Option 1: Calculate the total cost of ingredients")
    print("Option 2: Calculate the average cost per serving of a meal")
    print("Option 3: Quit the program")
    print("Option 4: Clear your console")
    print("Option 5: Quit program")
    user_action = input("\nWhat would you like to do? ")

    if user_action == '1':
        print("\nYou are calculating the total ingredient cost of a meal")
        total_cost = ingredient_cost_calculator()
        entry = f"Total ingredient cost: ${total_cost}"
        save_to_history(entry)
        continue

    elif user_action == '2':
        print("\nYou are calculating the cost per serving of a meal")
        cost_per_serving = cost_per_serving_calculator()
        entry = f"Cost per serving: ${cost_per_serving:.2f}"
        save_to_history(entry)
        continue

    elif user_action == '3':
        view_history()
        continue

    elif user_action == '4':
        cls()
        continue

    elif user_action == '5':
        print("\nQuitting program!")
    else:
      print("Invalid option\n")
      continue
