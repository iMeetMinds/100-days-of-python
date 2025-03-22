import string

from art import logo

print(logo)

bidders = []

def add_bid(b_name, u_bid):
    bid_dic : dict[string, any] = {"name": b_name, "amount": u_bid}
    bidders.append(bid_dic)

def auction_winner():
    high_bid = 0
    high_bid_user = {}
    for curr_dict in bidders:
        curr_bid = curr_dict["amount"]
        if high_bid < curr_bid:
            high_bid = curr_bid
            high_bid_user = curr_dict

    print(f"The winner is {high_bid_user['name']} with a bid of ${high_bid_user['amount']}")

is_continued = True
while is_continued:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? $"))

    add_bid(name, bid)
    more_users = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_users == "no":
        is_continued = False

auction_winner()