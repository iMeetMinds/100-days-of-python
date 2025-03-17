weight = input("Enter your weight in KG :")
height = input("Enter your height in M :")

bmi = float(int(weight) / (float(height) ** 2))

print("your bmi is " + str(round(bmi, 2)))

if bmi < 18.5:
    print("youare under weight")
elif bmi < 25:
    print("You have normal wweight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")