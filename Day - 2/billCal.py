print("Welcome to the Bill Calculator")

bill_amt = input("What was the total bill? $")
persons = input("How many people were there? ")
tip = input("How much tip you would like to give? 10%, 12% or 15%? ")

per_person = (((float(bill_amt) * int(tip)) / 100) + int(bill_amt)) / int(persons)
final_amt = "{:.2f}".format(per_person)

print(f"Per person should pay {final_amt}")