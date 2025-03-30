
with open("./Input/Names/invited_names.txt") as names:
    all_names = names.readlines()

for name in all_names:
    name = name.strip("\n")

    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[name]", name)

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as output_letter:
        output_letter.write(letter_content)