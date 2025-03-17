print("Welcome to love calculator")
name1 = input("Enter Your name \n").lower()
name2 = input("Enter your loved one's name \n").lower()

char = name1 + name2

love_count = char.count("l") + char.count("o") + char.count("v") + char.count("e")
true_count = char.count("t") + char.count("r") + char.count("u") + char.count("e")

love_perc = int(str(love_count) + str(true_count))
print(love_perc)
if (love_count < 10) and (love_count > 90):
    print(f"your love count is {love_count}, you are like mentos in water")
elif (love_count > 40) and (love_count < 50):
    print(f"your love count is {love_count},You are alright together")
else:
    print(f"your love count is {love_perc}")