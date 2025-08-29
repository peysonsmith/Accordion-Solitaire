# imports:
import random

# Create a class for a card with a value and suit
class Card:
    def __init__(self, value, suit, id):
        self.value = value
        self.suit = suit
        self.id = id

# Generates a deck of 52 cards each with a suit and value
def generate_deck(values, suits, face_cards):
    deck = []
    for suit in suits:
        for value in values:
            if value in face_cards:
                face_id = face_cards[value]
                deck.append(Card(value, suit, face_id))
            else:
                deck.append(Card(value, suit, value))
    return deck

#-----------------------------------------------------------------------------------------------------------------

# Create a random that is able to pull a card from the deck and take it out of the remaining cards
def pull_card(deck):
    curr_card = random.choice(deck)
    deck.remove(curr_card)
    return curr_card

#-----------------------------------------------------------------------------------------------------------------

# Create a class representing a pile with a list of the cards in that pile. Have the option to add a card and 
# find the number of cards in the pile
class Pile:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def size(self):
        return len(self.cards)
    
    def top_card(self):
        return self.cards[-1]

#-----------------------------------------------------------------------------------------------------------------

# Draws by pulling a random card from the deck and putting it on top of a new pile
def draw_card(piles, deck):
    new_pile = Pile()
    new_pile.add_card(pull_card(deck))
    piles.append(new_pile)

# adds the cards from one pile to another
def combine_piles(pile1, pile2):
    for card in pile1.cards:
        pile2.add_card(card)
    pile1.cards.clear()  # Clear the source pile

def make_move(piles, deck, index):
    # Add boundary checks
    if index <= 0 or index >= len(piles):
        return
    
    if len(piles) <= 1:
        return
        
    # Check if we can access adjacent piles safely
    if index - 1 < 0:
        return

    my_card = piles[index].top_card()
    close_card = piles[index - 1].top_card()
    
    # Only try to access jump_card if we have enough piles
    if index >= 3:
        jump_card = piles[index - 3].top_card()
    else:
        jump_card = None

    # Edge case: there is only 1 pile
    if len(piles) <= 1:
        return
    
    # Edge case: there is less than 4 piles
    elif len(piles) < 4 and (my_card.suit == close_card.suit or 
        my_card.value == close_card.value):
        print("piles have been combined!")
        combine_piles(piles[index], piles[index - 1])
        del piles[index]

    # Checks if your card has the same value/suit as the previous pile and the pile that is 3 piles away
    elif jump_card and ((my_card.suit == close_card.suit or 
        my_card.value == close_card.value) and 
        (my_card.suit == jump_card.suit or 
        my_card.value == jump_card.value)):
        # Asks the user which pile they wish to place the card on
        choice = input("Type 'jump' to place card on far pile, type 'close' to place card on close pile: ")

        # Check for invalid input
        while choice != "jump" and choice != "close":
            print("Invalid input!")
            choice = input("Type 'jump' to place card on far pile, type 'close' to place card on close pile: ")

        # Place card on pile they chose
        if choice == "jump":
            combine_piles(piles[index], piles[index - 3])
            del piles[index]
            return True
        if choice == "close":
            combine_piles(piles[index], piles[index - 1])
            del piles[index]
            return True

    # Checks if only the far pile matches
    elif jump_card and (my_card.suit == jump_card.suit or 
        my_card.value == jump_card.value):
        choice = input("Type 'jump' to place card on far pile: ")

        # Check for invalid input
        while choice != "jump":
            print("Invalid input!")
            choice = input("Type 'jump' to place card on far pile: ")

        # Place card on jump pile
        combine_piles(piles[index], piles[index - 3])
        del piles[index]
        return True

    # Checks if only the close pile matches
    elif (my_card.suit == close_card.suit or 
        my_card.value == close_card.value):
        choice = input("Type 'close' to place card on close pile: ")

        # Check for invalid input
        while choice != "close":
            print("Invalid input!")
            choice = input("Type 'close' to place card on close pile: ")

        # Place card on close pile
        combine_piles(piles[index], piles[index - 1])
        del piles[index]
        return True

    else:
        return False
    
# Once a move has been and check if another move can be made and make the move
def cascade_move(piles, deck):
    moves_made = True

    while moves_made:
        moves_made = False

        for i in range(len(piles) - 1, -1, -1):
            if can_pile_move(piles, i):
                print(f"Cascade move: Pile {i} can move!")
                if make_move(piles, deck, i):
                    moves_made = True
                    print_piles(piles)  # Show current state
                    break  # Start checking from the beginning again

    print("No more cascade moves possible.")   

# Checks if pile at given index can make a valid move
def can_pile_move(piles, index):
    # Boundary checks
    if index <= 0 or index >= len(piles):
        return False
    if len(piles) <= 1:
        return False
    if index - 1 < 0:
        return False
        
    my_card = piles[index].top_card()
    close_card = piles[index - 1].top_card()
    
    # Check close pile match
    close_match = (my_card.suit == close_card.suit or 
                   my_card.value == close_card.value)
    
    # Check jump pile match (if exists)
    jump_match = False
    if index >= 3:
        jump_card = piles[index - 3].top_card()
        jump_match = (my_card.suit == jump_card.suit or 
                      my_card.value == jump_card.value)
    
    return close_match or jump_match

# Print out all of the top cards of the piles
def print_piles(piles):
    if len(piles) < 1:
        print("no piles")
        return
    
    pile_index = 1
    for pile in piles:
        print(f"{pile_index}: {pile.top_card().id} {pile.top_card().suit}" )
        pile_index += 1
    print("-------------------------------------------------------------------")

# After all the cards have been gone through, tally up the number of points the player recieves
# 5 for every card in the first pile, then 3, then 1, -1, -3, ...
def count_score(piles):
    score = 0
    if len(piles) >= 2:
        for i in range(0, len(piles), -1):
            score += (piles[i].size * (7 + -2(i)))
    return score
            

#----------------------------------------------------MAIN--------------------------------------------------------
def main():    
    # Create deck of cards each with a value and suit
    # List of all values and suits each card could have
    values = range(2, 15)
    suits = ["spades", "hearts", "clubs", "diamonds"]

    # Create a dictionary for face cards
    face_cards = {
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A',
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    # Create a new pile of the random card that can be placed 1 pile away or 3 piles away if the suit or number
    # match of the top card of either of those piles and the current card
    piles = []
    deck = generate_deck(values, suits, face_cards)

    deck_length = len(deck)
    for i in range(0, deck_length):
        print(f"\n--- Drawing card {i+1} ---")
        draw_card(piles, deck)
        print_piles(piles)

        #pause after drawing
        input("Press Enter ")
        
        index = len(piles) - 1
        
        # Try to move the newly drawn card
        if make_move(piles, deck, index):
            print("Move successful! Checking for cascade moves...")

            input("Press Enter ")

            cascade_move(piles, deck)
        else:
            print("No valid moves for this card.")
        
        print(f"Current number of piles: {len(piles)}")

        input("Press Enter to continue...")
    print(count_score(piles))

main()
#------------------------------------------------------------------------------------------------------------------