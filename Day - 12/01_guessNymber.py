import random

print("Welcome to number guessing game!!")
print("I'm thinking of a number between 1 to 100.")

HARD_ATTEMPT = 5
EASY_ATTEMPT = 10
game_attempt = 0
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

computer_choice_no = random.choice(range(101))
print(computer_choice_no)
if difficulty_level == 'hard':
    game_attempt = HARD_ATTEMPT
else:
    game_attempt = EASY_ATTEMPT

while game_attempt != 0:
    print(f"You have {game_attempt} attempts remaining to guess the number.")
    guess_no = int(input("Make a guess : "))

    game_attempt -= 1

    if guess_no > computer_choice_no:
        print("Too High.")
    elif guess_no < computer_choice_no:
        print("Too Low.")
    else:
        print(f"You got it. The answer is {computer_choice_no}!!")
        game_attempt = 0
        break

    if game_attempt == 0:
        print("You've run out of guesses. You lose!!")
