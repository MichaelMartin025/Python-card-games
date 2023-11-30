# single deck data file reader

ace = 0
ace_line = "none"

with open("single_deck.txt", "r") as single_deck_data:
    for e,line in enumerate(single_deck_data):
        #print(e+1, line)
        if "Ace" in line:
            ace += 1
            ace_line = line
                       
print(f"\nAces found = {ace} out of {e+1} attemps")
print(ace/(e+1))
print()