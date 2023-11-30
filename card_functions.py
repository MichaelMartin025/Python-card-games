import random

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