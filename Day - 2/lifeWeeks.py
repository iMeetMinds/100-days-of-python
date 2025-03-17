age = input("What is your age? \n")

totalMonths = (90*12) - (int(age)*12)
totalWeeks = (90*52) - (int(age)*52)
totalDays = (90*365) - (int(age)*365)

print(f"You have {totalDays} days, {totalWeeks} weeks and {totalMonths} months left")