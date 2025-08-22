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

# Create a class for a card with a value and suit
class Card:
    def __init__(self, value, suit, id):
        self.value = value
        self.suit = suit
        self.id = id

# Generates a deck of 52 cards each with a suit and value
def generate_cards(values, suits):
    deck = []
    for suit in suits:
        for value in values:
            if value in face_cards:
                face_id = face_cards[value]
                deck.append(Card(value, suit, face_id))
            else:
                deck.append(Card(value, suit, value))
    return deck

# 




# Create a random that is able to pull a card from the deck and take it out of the remaining cards

# Create a pile that remembers how many cards are on that pile and what the top card of that pile is
 
# Create a new pile of the random card that can be placed 1 pile away or 3 piles away if the suit or number
# match of the top card of either of those piles and the current card
 
# Can now move any of the remaining piles if they are able to be played

# Restrict the player from drawing a new card if a move can currently be played

# After all the cards have been gone through, tally up the number of points the player recieves