weight = input("Enter your weight in KG :")
height = input("Enter your height in M :")

bmi = int(weight) / (float(height) ** 2)

print("your bmi is " + str(round(bmi, 2)))