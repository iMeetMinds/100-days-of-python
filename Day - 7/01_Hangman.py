import random
# import hangman_art
from hangman_art import stages,logo
# import hangman_words
from hangman_words import word_list

print(logo)
# chosen_word = name_list[random.randint(0, 6)]
chosen_word = random.choice(word_list)
print(f"Your chosen word is {chosen_word}")

lives = 6
display = []

for n in range(len(chosen_word)):
    display.append("_")

# while display.count("_") != 0:
end_of_game = False
guess_list = []
while not end_of_game:
    guess = input("Guess a Letter : ").lower()

    if guess in guess_list:
        print(f"You have already guessed this letter {guess}")
        continue

    if guess in chosen_word:
        for pos in range(len(chosen_word)):
            if chosen_word[pos] == guess:
                display[pos] = guess
    else:
        print(f"You guessed {guess}, that's not in a word. You lose a life.")
        lives -= 1

    print(display)
    print(stages[lives])
    guess_list.append(guess)

    if lives == 0:
        end_of_game = True
        print("You Lose")

    if "_" not in display:
        end_of_game = True
        print("You Win")

