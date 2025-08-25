import main

values = range(2, 15)
suits = ["spades", "hearts", "clubs", "diamonds"]

deck = main.generate_deck(values,suits)
my_card = main.pull_card(deck)
print(f"{my_card.id} of {my_card.suit}")

for card in deck:
    print(f"{card.id} of {card.suit}")