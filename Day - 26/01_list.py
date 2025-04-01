numbers = [1,1,2,3,5,8,13,21,34,55]
new_numbers = [n*n for n in numbers]
# print(new_numbers)

result = [n for n in numbers if n % 2 ==0]
# print(result)

with open("text_1.txt") as t1:
    num1 = [int(n) for n in t1.readlines() if n.replace("\n","")]
    print(num1)

with open("text_2.txt") as t2:
    num2 = [int(n) for n in t2.readlines() if n.replace("\n","")]
    print(num2)

result_num = [n for n in num1 if n in num2]
print(result_num)