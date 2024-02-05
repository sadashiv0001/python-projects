import time

def custom_shuffle(deck):
    """
    Custom shuffle algorithm using a pseudo-random seed (including current time) for swapping cards.
    """
    seed = int(time.time())  # Initialize seed with current time
    length = len(deck)

    for i in range(length - 1, 0, -1):
        # Generate a pseudo-random index using the current time and loop index
        seed = (seed + i) % length

        # Swap the current card with the randomly selected card
        deck[i], deck[seed] = deck[seed], deck[i]

# Example usage
def display_deck(deck):
    """
    Display the rank and suit of each card in the deck.
    """
    for card in deck:
        print(f"{card['rank']} of {card['suit']}")

# Generating a deck
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# Test Case 1: Display Original Deck
print("Test Case 1 - Original Deck:")
display_deck(deck)
print("\n")

# Test Case 2: Shuffle the Deck
custom_shuffle(deck)
print("Test Case 2 - Shuffled Deck:")
display_deck(deck)
print("\n")

# Test Case 3: Shuffle the Deck Again
custom_shuffle(deck)
print("Test Case 3 - Shuffled Deck Again:")
display_deck(deck)
print("\n")

# Test Case 4: Create and Display a New Deck
new_deck = [{'rank': '6', 'suit': 'Clubs'}, {'rank': '10', 'suit': 'Hearts'}, {'rank': 'A', 'suit': 'Spades'}]
print("Test Case 4 - New Deck:")
display_deck(new_deck)
print("\n")

# Test Case 5: Shuffle a Small Deck
small_deck = [{'rank': '2', 'suit': 'Hearts'}, {'rank': '5', 'suit': 'Diamonds'}]
print("Test Case 5 - Small Deck Before Shuffling:")
display_deck(small_deck)
custom_shuffle(small_deck)
print("\nTest Case 5 - Small Deck After Shuffling:")
display_deck(small_deck)
