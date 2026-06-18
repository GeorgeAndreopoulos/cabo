import random
deck = []
suits = ['S','H','D','C'] #Spades, Hearts, Diamonds, Clubs
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for s in suits:
    for n in numbers:
        deck.append(s + str(n))

#jokers:
deck.append("A0")
deck.append("B0")

values = {
    0: -2,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 0,
    11: 11,
    12: 12,
    13: 13
}

deck_for_round = deck.copy()
hand = []
print(len(deck_for_round))
for i in range(4):
    card_index = random.randint(0,53)
    hand.append(deck_for_round[card_index])
    deck_for_round.pop(card_index)

print(hand)

def get_score(hand):
    global values
    score = 0
    for el in hand:
        digit = int(el[1:])
        value = values[digit]
        score += value
    return score

print(get_score(hand))