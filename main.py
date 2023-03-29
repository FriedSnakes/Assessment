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
        num_ingredients = get_number_input("\nHow many ingredients are in the recipe? ")
        
        for i in range(num_ingredients):
            ingredient_name = input("Enter the name of ingredient #" + str(i+1) + ": ")
            ingredient_cost = get_valid_number_decimal("Enter the cost of " + ingredient_name + ": $")
            ingredient_quantity = get_number_input("Enter the quantity of " + ingredient_name + ": ")
            ingredient_costs.append((ingredient_name, ingredient_cost, ingredient_quantity))
        
        total_cost = sum([ingredient[1] * ingredient[2] for ingredient in ingredient_costs])
        print("The total cost of ingredients is: $" + str(total_cost))

        retry = input("Do you want to retry? (Y to retry, any other button to not) ")
        if retry.lower() == "y":
            continue
        else:
            return total_cost

def is_valid_number(input_str):
  return input_str.isdigit()


def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        if is_valid_number(user_input):
          return int(user_input)
        else:
          print("Please enter a valid number.")

def get_valid_number_decimal(prompt):
    while True:
        num = input(prompt)
        try:
            val = float(num)
            return val
        except ValueError:
            print("This is not a number. Please enter a valid number.")

def cost_per_serving_calculator():
    while True:
        total_cost = get_valid_number_decimal("Enter the total cost of the meal: ")
        num_servings = get_valid_number_decimal("Enter the number of servings the meal can make: ")
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


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")

def clear_history():
    try:
        delete_file("history.txt")
    except Exception as e:
        print("An error occurred while clearing the history:", e)
    else:
        print("History cleared successfully!")


print("Welcome to the meal cost calculator. ")

while True:
    print("\nYou have 6 options before you")
    print("Option 1: Calculate the total cost of ingredients")
    print("Option 2: Calculate the average cost per serving of a meal")
    print("Option 3: View your history")
    print("Option 4: Clear your console")
    print("Option 5: Clear history")
    print("Option 6: Quit program")
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
        print("Clearing Console!")
        cls()
        continue
      
    elif user_action == '5':
          print("Clearing History")
          clear_history()
          continue
  
    elif user_action == '6':
        print("\nQuitting program!")    
        break
    
    else:
      print("Invalid option\n")
      continue



    