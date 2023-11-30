# choose from full deck every time
# card game

from card_functions import *

deck = []
hand = []
rank = "none"
suit = "none"
card = 1
rounds = 1
count = 1
subcount = 1

while True:
    count += 1

    while True:
        subcount += 1
        for card_id in range(1,53):
            #print(card)
            deck.append(card_id)
        rand_card, deck = draw_card(deck)

        rank, suit = parse_card(rand_card)
        print(f"{rank} of {suit}")
        with open("single_deck_4_times.txt", "a") as single_deck_data:
            single_deck_data.write(f"{rank} of {suit}\n")
        if subcount >= 4:
            break

    if count > 5:
        break

print()