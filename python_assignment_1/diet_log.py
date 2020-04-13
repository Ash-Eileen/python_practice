#!/usr/bin/env python3

def pos_float(n):
    """ Prompts the user to enter a positive float """
    while True:
        try:   
            value = float(input(n))
        except ValueError:
            print("Please enter a number")
            continue
        if value < 0:
            print("Please enter a nonnegative number")
            continue
        else:
            break            
    return value

# Ensure a positive, whole number is captured from user for patient numbers
while True:
    try:
        patients = int(input("Enter a number of patients: "))
    except ValueError: 
        print("Please enter a whole number")
        continue
    if patients < 1:
        print("Please enter a positive number")
        continue
    else:
        break

# Defining protein, carbs and fats to call later
protein, carbohydrates, fat = 0, 0, 0

# getting result of user input of proteins, carbs and fats for each patient
for i in range(patients):
    print("Patient " + str(i+1))
    protein_inp = pos_float("     Amount of protein (g) required: ")
    carb_inp = pos_float("     Amount of carbohydrates (g) required: ")
    fat_inp = pos_float("     Amount of fat (g) required: ")    
    i + 1
    # Add revelant input for each patient to count
    protein = protein_inp + protein 
    carbohydrates = carb_inp + carbohydrates
    fat = fat_inp + fat

# Working out averages for proteins, carbs and fats
protein_av = protein / patients
carb_av = carbohydrates / patients
fat_av = fat / patients

# Working out average kjs
kilojoules = 4.18 * (4*protein_av + 4*carb_av + 9.30*fat_av)

kilojoules = round(kilojoules, 2)

print("\nAverages:")
print("Protein (g): " + str(protein_av))
print("Carbohydrates (g): " + str(carb_av))
print("Fat (g): " + str(fat_av))
print("Kilojoules (kJ): " + str(kilojoules))
