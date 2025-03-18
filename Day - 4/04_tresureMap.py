list1 = ['','','']
list2 = ['','','']
list3 = ['','','']

map = [list1, list2, list3]

num = input("Where you want to put your treasure? \n")

map[int(num[1]) - 1][int(num[0]) - 1] = "X"

print(f"{list1}\n{list2}\n{list3}")