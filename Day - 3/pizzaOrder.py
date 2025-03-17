small_p = 15
mid_p = 20
large_p = 25

pep_small_p = 2
pep_med_lar_p = 3

extra_cheese = 1

print("Welcome to the piiza shop")
pizza = input("What size of pizza do you want? S, M or L? ")
peproni = input("Do you want to have extra peproni? Y or N? ")
cheese = input("Do you want extra cheese? Y or N? ")

final_bill = 0

if pizza == "S":
    final_bill += small_p
    if peproni == "Y":
        final_bill += pep_small_p
elif pizza == "M":
    final_bill += mid_p
    if peproni == "Y":
        final_bill += pep_med_lar_p
else:
    final_bill += large_p
    if peproni == "Y":
        final_bill += pep_med_lar_p


if cheese == "Y":
    final_bill += extra_cheese

print(f"Your final bill is {final_bill}")