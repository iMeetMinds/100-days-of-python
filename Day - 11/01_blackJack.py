from art import logo
import random
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sum_array(array):
    sum_num = sum(array)
    if (sum_num > blackjack_win_score) and (11 in array):
        sum_num -= 10
    return sum_num

def draw_card(array):
    array.append(random.choice(cards))
    return array

def beginner_array():
    card_array = []
    for i in range(2):
        card_array = draw_card(card_array)
    return card_array

def print_score_user(array_list, score):
    print(f"Your cards : {array_list}, current score : {score}")

def print_score_comp(array_list):
    print(f"Computer's first card: {array_list[0]}")

def update_comp_game(c_cards, score):
    if score < 17:
        c_cards = draw_card(c_cards)
    return c_cards

def print_final_result(user_score, comp_score):
    if comp_score == blackjack_win_score:
        print("Lose, opponent has Blackjack 😱 \n\n")
    elif user_score == blackjack_win_score:
        print("Win with a Blackjack 😎 \n\n")
    elif user_score > blackjack_win_score:
        print("You went over. You lose 😭 \n\n")
    else:
        if user_score > comp_score:
            print("You win 😃 \n\n")
        elif user_score == comp_score:
            print("Draw 🙃 \n\n")
        else:
            print("You lose 😤 \n\n")

blackjack_win_score = 21

def black_jack():
    want_to_play = input("Do you want to play a game of BlackJack? type 'y' or 'n' ").lower()

    if want_to_play == 'y':
        your_card = beginner_array()
        user_sum = sum_array(your_card)
        print_score_user(your_card, user_sum)
        computer_card = beginner_array()
        computer_sum = sum_array(computer_card)
        print_score_comp(computer_card)

        game_continued = True
        while game_continued:
            if (user_sum >= blackjack_win_score) or (computer_sum == blackjack_win_score):
                print(f"Your final hand: {your_card}, final score : {user_sum}")
                print(f"Computer's final hand: {computer_card}, final score : {computer_sum}")
                print_final_result(user_sum, computer_sum)
                game_continued = False
            else:
                draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

                if draw_another_card == 'y':
                    your_card = draw_card(your_card)
                    user_sum = sum_array(your_card)
                    print_score_user(your_card, user_sum)
                    print_score_comp(computer_card)

                else:
                    game_continued = False
                    print(f"Your final hand: {your_card}, final score : {user_sum}")
                    print(f"Computer's final hand: {computer_card}, final score : {computer_sum}")
                    print_final_result(user_sum, computer_sum)

                computer_card = update_comp_game(computer_card, computer_sum)
                computer_sum = sum_array(computer_card)
        black_jack()

    else:
        print("Thanks for playing the game!!")

black_jack()