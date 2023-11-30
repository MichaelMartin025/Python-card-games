# card game
import os, sys
import random

deck = []
hand = []
rank = "none"
suit = "none"
card = 1
rounds = 1

for card_id in range(1,53):
    #print(card)
    deck.append(card_id)
    
#print(len(deck))

def parse_card(rand_card):
    
    if rand_card <= 13:
        #print("Clubs")
        suit = "clubs"
        rank = str(rand_card)
    if rand_card >= 14 and rand_card <= 26:
        #print("Diamonds")
        suit = "diamonds"
        rank = str(rand_card - 13)
    if rand_card >= 27 and rand_card <= 39:
        #print("Hearts")
        suit = "hearts"
        rank = str(rand_card - 26)
    if rand_card >= 40:
        #print("Spades")
        suit = "spades"
        rank = str(rand_card - 39)
        
    if rank == "1":
        #print("Ace")
        rank = "Ace"
    if rank == "11":
        #print("Jack")
        rank = "Jack"
    if rank == "12":
        #print("Queen")
        rank = "Queen"
    if rank == "13":
        #print("King")
        rank = "King"
        
    return rank, suit

def draw_card(deck):
    rand_card = random.choice(deck)
    #print(rand_card)
    deck.remove(rand_card)
    return rand_card, deck

while True:
    hand = []
    card = 1
    while True:
        rand_card, deck = draw_card(deck)
        rank, suit = parse_card(rand_card)
        print(f"\nCard {card}: You drew a {rank} of {suit}.")
        print(f"Remaining cards = {len(deck)}.")
        if len(deck) <= 0:
            print("\nNo more cards.")
            sys.exit()
        hand.append(rank)
        card += 1
        if card > 5:
            break
            
    print(f"\n{hand}")
    print(f"Number of Aces in this hand = {hand.count('Ace')}")
    print(f"\n{rounds} sessions")
    with open("data.txt", "a") as datafile:
        datafile.write(f"{rounds},{hand},Aces={hand.count('Ace')},\n")
    if hand.count("Ace") == 4:
        break
    rounds += 1

print(os.getcwd())        
        
        