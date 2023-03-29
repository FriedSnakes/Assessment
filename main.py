'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
# Importing necessary modules
import json
import os

# Function to write to a file with given ingredient name and cost
def file(ingredient_name, ingredient_cost):
    # Creating a dictionary with the ingredient name and cost
    ingredient_list = {ingredient_name: ingredient_cost}
    # Prompting the user to enter a file name for the file to be written to
    file_name = input("What do you want the file name to be? ")
    try:
        # Opening the file in write mode
        with open(file_name, "w") as f:
            # Writing the dictionary as a JSON string to the file
            f.write(json.dumps(ingredient_list))
    except Exception as e:
        print("An error occurred while writing to the file:", e)

# Function to calculate the total cost of ingredients
def ingredient_cost_calculator():
    while True:
        ingredient_costs = []
        # Prompting the user to enter the number of ingredients in the recipe
        num_ingredients = get_number_input("\nHow many ingredients are in the recipe? ")
        
        # Looping through each ingredient and prompting the user for the name, cost, and quantity
        for i in range(num_ingredients):
            ingredient_name = input("Enter the name of ingredient #" + str(i+1) + ": ")
            ingredient_cost = get_valid_number_decimal("Enter the cost of " + ingredient_name + ": $")
            ingredient_quantity = get_valid_number_decimal("Enter the quantity of " + ingredient_name + ": ")
            # Adding the ingredient to a list as a tuple of name, cost, and quantity
            ingredient_costs.append((ingredient_name, ingredient_cost, ingredient_quantity))
        
        # Calculating the total cost of all ingredients by multiplying cost and quantity and summing
        total_cost = sum([ingredient[1] * ingredient[2] for ingredient in ingredient_costs])
        print("The total cost of ingredients is: $" + str(total_cost))

        # Prompting the user if they want to retry
        retry = input("Do you want to retry? (Y to retry, any other button to not) ")
        if retry.lower() == "y":
            continue
        else:
            return total_cost

# Function to check if user input is a valid integer
def is_valid_number(input_str):
  return input_str.isdigit()

# Function to get integer input from the user with the given prompt
def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        if is_valid_number(user_input):
          return int(user_input)
        else:
          print("Please enter a valid number.")

#function to check user input is an integer, and allows inputs to be decimals

def get_valid_number_decimal(prompt):
    while True:
        num = input(prompt)
        try:
            val = float(num)
            return val
        except ValueError:
            print("This is not a number. Please enter a valid number.")



          
# Function to calculate the cost per serving of a meal
def cost_per_serving_calculator():
    while True:
        # Prompting the user to enter the total cost of the meal and the number of servings it can make
        total_cost = get_valid_number_decimal("Enter the total cost of the meal: ")
        num_servings = get_valid_number_decimal("Enter the number of servings the meal can make: ")
        # Calculating the cost per serving by dividing total cost by number of servings
        cost_per_serving = total_cost / num_servings

        # Printing the cost per serving to the console
        print("The cost per serving of the meal is: $", format(cost_per_serving, '.2f'))
        
        # Prompting the user if they want to retry
        retry = input("Do you want to retry? (Y/N) ")
        if retry.lower() == "y":
            continue
        else:
            return cost_per_serving

# function to clear console screen depending on the OS
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# function to view the saved history in the history.txt file
def view_history():
    try:
        with open('history.txt') as f:
            history = f.read()
            print(history)
    except FileNotFoundError:
        print("No history found")

# function to save the calculated entries to the history.txt file
def save_to_history(entry):
    with open('history.txt', 'a') as f:
        f.write(entry + '\n')

# function to delete a file
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")

# function to clear the history.txt file
def clear_history():
    try:
        delete_file("history.txt")
    except Exception as e:
        print("An error occurred while clearing the history:", e)
    else:
        print("History cleared successfully!")

# main program starts here
print("Welcome to the meal cost calculator. ")
while True:
    # printing available options to the user
    print("\nYou have 6 options before you")
    print("Option 1: Calculate the total cost of ingredients")
    print("Option 2: Calculate the average cost per serving of a meal")
    print("Option 3: View your history")
    print("Option 4: Clear your console")
    print("Option 5: Clear history")
    print("Option 6: Quit program")
    # getting user input for the action to be taken
    user_action = input("\nWhat would you like to do? ")

    # conditional statements for each of the user actions
    if user_action == '1':
        print("\nYou are calculating the total ingredient cost of a meal")
        # calling a function to calculate the total ingredient cost
        total_cost = ingredient_cost_calculator()
        # formatting the calculated value as a string and adding it to the history.txt file
        entry = f"Total ingredient cost: ${total_cost}"
        save_to_history(entry)
        # continuing the loop to prompt for more user actions
        continue

    elif user_action == '2':
        print("\nYou are calculating the cost per serving of a meal")
        # calling a function to calculate the cost per serving
        cost_per_serving = cost_per_serving_calculator()
        # formatting the calculated value as a string and adding it to the history.txt file
        entry = f"Cost per serving: ${cost_per_serving:.2f}"
        save_to_history(entry)
        # continuing the loop to prompt for more user actions
        continue

    elif user_action == '3':
        # calling a function to view the history
        view_history()
        # continuing the loop to prompt for more user actions
        continue

    elif user_action == '4':
        print("Clearing Console!")
        # calling a function to clear the console screen
        cls()
        # continuing the loop to prompt for more user actions
        continue

    elif user_action == '5':
        print("Clearing History")
        # calling a function to clear the history.txt file
        clear_history()
        # continuing the loop to prompt for more user actions
        continue

    elif user_action == '6':
        print("\nQuitting program!") 
        # breaking out of the loop and ending the program
        break

    else:
        print("Invalid option\n")


    


    