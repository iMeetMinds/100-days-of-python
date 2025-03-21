import math


def paint_cal(height, width, cover):
    no_of_cans = 0
    no_of_cans = math.ceil((height * width) / cover)
    print(f"You will need {no_of_cans} cans of paint")


ht = int(input("height if the wall : "))
wt = int(input("width if the wall : "))
coverage = 5

paint_cal(height = ht, width = wt, cover = coverage)