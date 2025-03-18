import random

name_string = input("Provide me names of everybody. separated by comma. \n")

name_list = name_string.split(",")
random_int = random.randint(0, len(name_list) - 1)

print(f"{name_list[random_int]} is going to pay for meal today!!")
print(f"{random.choice(name_list)} is going to pay for meal today!!")
