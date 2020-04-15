# Program to select the best available diet for a patient and save this information to a csv file
# Author: Ashley Smith

#!/usr/bin/env python3

import sys

def get_num(prompt, error):
    """
        Uses given prompt to request a number.
        The error is displayed and user is prompted to re-enter the prompt until an int is provided.
        If there is no user input the program exits

        Arguments:
        prompt -- The prompt to display when asking the user to input the integer
        error -- The error to display if an invalid value is entered

        Returns the input as an int
    """
    while True:
        value = input(prompt)
        if len(value) == 0: 
            sys.exit(0)
        try:
            return int(value)
        except ValueError:
            print(error)

def get_patient_id(prompt, error):
    """
        Uses get_num function to request an input from user.
        If the input does not meets the requirements of being 6 digits with no leading zeros then prompts until valid input is received

        prompt -- The prompt to display when asking the user to enter a valid input
        error -- The error to display if an invalid value is entered

        Returns the input as a 6 digit int.
    """
    value = str(get_num(prompt, error))
    while len(value) != 6 or value[0] == "0" or value[0] == "-":
        print(error)
        value = str(get_num(prompt, error))
    return value

def get_non_neg(prompt, error="Please enter a nonnegative number"):
    """ 
        Prompts the user to enter a non-negative float.
        If an invalid value is entered the given error is displayed and the process repeats.

        Arguments:
        prompt -- The prompt to display when asking the user to input the integer
        error -- The error to display if an invalid value is entered

        Returns the input as a float
    """
    while True:
        value = input(prompt)
        try:   
            value = float(value)
        except ValueError:
            print(error)
            continue
        if value < 0:
            print(error)
            continue
        else:
            break        
    return value

def calculate_error(diet, requirements):
    # Takes the key of the diet name in the diet dictionary and works out the absolute error of the difference between the values
    # in the requirements key. These values are added tgoether for each indvidual diet and returned in a new dictionary that includes
    # the diet name and the total absolute value of the differences.
    error = {}
    for key, value in diet.items():
        error[key] = sum([abs(v - requirements[k]) for k, v in value.items()])
    return error 

def choose_diet(protein, carbohydrates, fat):
    # Uses the calculate_error function and returns the key that has the lowest value.
    requirements = {"protein": protein, "carbohydrates": carbohydrates, "fat": fat} 
    error = calculate_error(diet, requirements)
    best = min(error, key=error.get)
    return best    

# Dictionary containing the available diets
diet = {"Normal": {"protein":32.50, "carbohydrates":60.00, "fat":40.68}, 
        "Oncology": {"protein":35.00, "carbohydrates":52.50, "fat":37.63}, 
        "Cardiology": {"protein":32.50, "carbohydrates":30.00, "fat":26.88}, 
        "Diabetes": {"protein":20.00, "carbohydrates":27.50, "fat":27.95}, 
        "Kidney": {"protein":15.00, "carbohydrates":55.00, "fat":23.65}}

# Loop requesting patient id and dietary requirements. This will continue until there is a blank entry in the patient id request.
while True:
    patient_id = get_patient_id("Please enter a patient id (or blank to exit): ", "Please enter a valid patient id (six-digit positive integer)")
    protein = get_non_neg("Amount of protein (g) required: ")
    carbohydrates = get_non_neg("Amount of carbohydrates (g) required: ")
    fat = get_non_neg("Amount of fat (g) required: ")   
    # Utilises choose_diet function to find the best available diet
    best = choose_diet(protein, carbohydrates, fat)
    # Prints the best available diet
    print("Selected diet: " + best)
    # Adds the patient id and best available diet to a csv file in the current directory. If no csv file exists this will create the file.
    file_out = open('meals_choice.csv', 'a+')
    file_out.write(patient_id + "," + best+ "\n")
    file_out.close()

