import pandas

dict_nato = {row.letter:row.code for (index,row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

is_word_spelled = False
while not is_word_spelled:
    user_input = input("Enter a word : ")
    try:
        list_nato = [dict_nato[char.upper()] for char in user_input]
    except KeyError:
        print("Sorry, Only letters in the alphabets please.")
    else:
        print(list_nato)
        is_word_spelled = True

