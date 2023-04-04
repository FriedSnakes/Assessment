'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
# Importing necessary modules
import os
from termcolor import colored

# Function to calculate the total cost of ingredients
def ingredient_cost_calculator():
    while True:
        ingredient_costs = []
        # Prompting the user to enter the number of ingredients in the recipe
        num_ingredients = get_number_input(colored("\nHow many ingredients are in the recipe? ", "magenta"))
        
        # Looping through each ingredient and prompting the user for the name, cost, and quantity
        for i in range(num_ingredients):
            ingredient_name = input(colored("Enter the name of ingredient #" + str(i+1) + ": ", "magenta"))
            ingredient_cost = get_valid_number_decimal(colored("Enter the cost of " + colored(ingredient_name + ": $", "cyan") , "magenta"))
            ingredient_quantity = get_valid_number_decimal(colored("How many serving sizes of " + colored(ingredient_name + " is required: ", "cyan")  , "magenta"))
            # Adding the ingredient to a list as a tuple of name, cost, and quantity
            ingredient_costs.append((ingredient_name, ingredient_cost, ingredient_quantity))
        
        # Calculating the total cost of all ingredients by multiplying cost and quantity and summing
        total_cost = sum([ingredient[1] * ingredient[2] for ingredient in ingredient_costs])
        print("The total cost of ingredients is: $" + format(total_cost, '.2f'))

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
          print(colored("Invalid option, numerals only\n","red"))

#function to check user input is an integer, and allows inputs to be decimals

def get_valid_number_decimal(prompt):
    while True:
        num = input(prompt)
        try:
            val = float(num)
            if val <= 0:
                print(colored("Number must be greater than zero\n", "red"))
            else:
                return val
        except ValueError:
            print(colored("Invalid option, numerals only\n", "red"))



          
# Function to calculate the cost per serving of a meal
def cost_per_serving_calculator():
    while True:
        # Prompting the user to enter the total cost of the meal and the number of servings it can make
        total_cost = get_valid_number_decimal(colored("Enter the total cost of the meal: $ ", "magenta"))
        num_servings = get_valid_number_decimal(colored("Enter the number of servings the meal can make: ", "magenta"))
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
        print(colored(f"Error deleting {file_path}: {e}","red"))

# function to clear the history.txt file
def clear_history():
    try:
        delete_file("history.txt")
    except Exception as e:
        print(colored("An error occurred while clearing the history:", e, ("red")))
    else:
        print("History cleared successfully!")

# main program starts here
print("_"*50)
print("Welcome to the meal cost calculator. ")
print("_"*50)
#Informing user of colour code
print(colored("Magenta means user input is expected", "magenta"))
print(colored("Red means error has been encountered", "red"))
print(colored("Cyan means it is a user input", "cyan"))
while True:
    # printing available options to the user
    print(colored("\nYou have 6 options before you", "magenta"))
    print("Option 1: Calculate the total cost of ingredients")
    print("Option 2: Calculate the average cost per serving of a meal")
    print("Option 3: View your history")
    print("Option 4: Clear your console")
    print("Option 5: Clear history")
    print("Option 6: Quit program")
    # getting user input for the action to be taken
    user_action = input("\nWhat would you like to do? Enter option number, then press enter ")

    # conditional statements for each of the user actions
    if user_action == '1':
        print("\nYou are calculating the total ingredient cost of a meal")
        # calling a function to calculate the total ingredient cost
        total_cost = ingredient_cost_calculator()
        # formatting the calculated value as a string and adding it to the history.txt file
        RecipeName = input("What would you like to name this recipe?")
        entry = f"Total ingredient cost of {RecipeName}: ${total_cost}"
        save_to_history(entry)
        # continuing the loop to prompt for more user actions
        continue

    elif user_action == '2':
        print("\nYou are calculating the cost per serving of a meal")
        # calling a function to calculate the cost per serving
        cost_per_serving = cost_per_serving_calculator()
        # formatting the calculated value as a string and adding it to the history.txt file
        File_Name = input("What would you like to name this recipe?")
        entry = f"Cost per serving of {File_Name}: ${cost_per_serving:.2f}"
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
        print(colored("Invalid option, numerals only\n","red"))


    


    