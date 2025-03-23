import random
from game_data import data
from art import logo,vs

def fetch_random_data():
    return data[random.choice(range(len(data)))]

def data_desc(disc):
    return f"{disc['name']}, {disc['description']}, from {disc['country']}"

def validate_answer(disc_a, disc_b):
    if disc_a['follower_count'] > disc_b['follower_count']:
        return 'a'
    else:
        return 'b'


final_score = 0
play_continued = True
entity_a = fetch_random_data()
print(logo)
while play_continued:
    if final_score != 0:
        print(f"You're right! Current score is {final_score}")

    entity_b = fetch_random_data()
    while entity_a == entity_b:
        entity_b = fetch_random_data()

    print(f"Compare A: {data_desc(entity_a)}")
    print(vs)
    print(f"Compare B: {data_desc(entity_b)}")

    ans = input("Who has more followers? Type 'A' or 'B': ").lower()

    if validate_answer(entity_a,entity_b) == ans:
        final_score += 1
        if ans == 'b':
            entity_a = entity_b

    else:
        print(f"Sorry, you are wrong. Final score {final_score}")
        play_continued = False