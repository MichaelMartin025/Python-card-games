# choose from full deck every time
# card game

from card_functions import *

deck = []
hand = []
rank = "none"
suit = "none"
card = 1
rounds = 1
count = 0
subcount = 0
ace1 = 0
ace2 = 0
ace3 = 0

while True:
    count += 1
    subcount = 0
    hand = []
    print(f"\nDeal {count}:")

    for card_id in range(1,53):
        #print(card)
        deck.append(card_id)

    while True:
        subcount += 1
        #print(f"\tinner {subcount}")

        rand_card, deck = draw_card(deck)
        #print(rand_card)
        rank, suit = parse_card(rand_card)
        #print(f"\t{rank} of {suit}")
        if rank == "Ace":
            hand.append(f"{rank} of {suit}")
        # with open("single_deck_4_times.txt", "a") as single_deck_data:
        #     single_deck_data.write(f"{rank} of {suit}\n")
        if subcount >= 4:
            deck.clear()
            break

    if len(hand) == 2:
        ace2 += 1    
    if len(hand) == 3:
        ace3 += 1
    if len(hand) == 4:
        print(f"Aces: {hand}")
        print(f"Number of Aces: {len(hand)}")
        break

    if count >= 100000 :
        print("Not found, End.")
        break

print()
print(f"times 2 aces = {ace2}")
print(f"times 3 aces = {ace3}")