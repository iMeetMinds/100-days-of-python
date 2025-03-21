from operator import truediv

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def shifting(letter, n):
    leg_alpha = len(alphabet)
    if not (alphabet.count(letter) > 0):
        return letter
    pos_letter = alphabet.index(letter)
    new_pos = pos_letter + n
    if new_pos >= leg_alpha:
        new_pos = new_pos % leg_alpha
    if new_pos < 0:
        new_pos += leg_alpha
    return alphabet[new_pos]


def ceaser_cipher(msg, n, direct):
    final_msg = ""
    if direction == "decode":
        n *= -1
    for letter in msg:
        final_msg += shifting(letter, n)
    print(f"Your {direct}d msg is {final_msg}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser_cipher(text, shift, direction)

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if go_again == 'no':
        should_continue = False
        print("Goodbye!!")



# def decrypt(msg = text, n = shift):
#     decrypted_msg = ""
#     for letter in msg:
#         decrypted_msg += shifting(letter, -n)
#     print(decrypted_msg)

# if direction == "encode":
#     print(f"Your encoded msg is {ceaser_cipher(text, shift)}")
# elif direction == "decode":
#     print(f"Your encoded msg is {ceaser_cipher(text, -shift)}")

# print(shifting("a", -5))