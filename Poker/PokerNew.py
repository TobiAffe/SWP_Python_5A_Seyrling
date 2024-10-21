import random
import numpy as np
from matplotlib import pyplot as plt

suits_ascii = ["\u2663", "\u2660", "\u2666", "\u2665"]
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'B', 'D', 'K', 'A']
suits_len = len(suits_ascii)
numbers_len = len(numbers)

def get_suit(card):
    return card // numbers_len

def get_number(card):
    return card % numbers_len

def str_card(card):
    return (suits_ascii[get_suit(card)] + numbers[get_number(card)])

def str_cards(cards):
    return " ".join(str_card(card) for card in cards)
def shuffel_cards(cards):
    range_list = range(len(cards))
    for i in range_list:
        ran = random.randint(i, len(cards) - 1)
        cards[ran], cards[i] = cards[i], cards[ran]
def draw_cards(count, cards):
    return cards[-count:]

def sort_cards(cards):
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if cards[i] % numbers_len > cards[j] % numbers_len:
                cards[i], cards[j] = cards[j], cards[i]
    return cards

def has_straight(cards):
    is_a = False
    cards_copy = cards[:]
    if get_number(cards_copy[0]) == 0 and get_number(cards_copy[-1]) == 12:
        cards_copy.pop()

    is_straight = True
    for i in range(len(cards_copy) - 1):
        if get_number(cards_copy[i]) + 1 != get_number(cards_copy[i + 1]):
            is_straight = False
            break

    if is_straight:
        return True

    return False

def has_flush(cards):
    suit_cards = [get_suit(card) for card in cards]
    return len(np.unique(suit_cards)) == 1

def has_pair(cards, how_many):
    pair_cards = np.zeros(numbers_len)
    for card in cards:
        pair_cards[get_number(card)] += 1

    # Count how many ranks have exactly 'how_many' occurrences
    return np.sum(pair_cards == how_many)

def evaluate_hand(hands_count):
    results = {
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Quads": 0,
        "Full House": 0,
        "Flush": 0,
        "Straight": 0,
        "Three of a Kind": 0,
        "Two Pair": 0,
        "One Pair": 0,
        "High Card": 0
    }

    for _ in range(hands_count):
        deck = [i for i in range(suits_len * numbers_len)]
        shuffel_cards(deck)
        hand = draw_cards(5, deck)
        hand = sort_cards(hand)

        is_flush = has_flush(hand)
        is_straight = has_straight(hand)
        is_straight_flush = is_straight and is_flush
        royal_flush_numbers = {8, 9, 10, 11, 12}
        hand_numbers = [get_number(card) for card in hand]
        is_royal_flush = is_straight_flush and royal_flush_numbers.issubset(hand_numbers)

        if is_royal_flush:
            results["Royal Flush"] += 1
        elif is_straight_flush:
            results["Straight Flush"] += 1
        elif has_pair(hand, 4) == 1:
            results["Quads"] += 1
        elif has_pair(hand, 3) == 1 and has_pair(hand, 2) == 1:
            results["Full House"] += 1
        elif is_flush:
            results["Flush"] += 1
        elif is_straight:
            results["Straight"] += 1
        elif has_pair(hand, 3) == 1:
            results["Three of a Kind"] += 1
        elif has_pair(hand, 2) == 2:
            results["Two Pair"] += 1
        elif has_pair(hand, 2) == 1:
            results["One Pair"] += 1
        else:
            results["High Card"] += 1

    # Calculate percentages
    total_hands = sum(results.values())
    for hand_type in results:
        results[hand_type] = (results[hand_type] / total_hands) * 100

    # Check if percentages sum to 100%
    total_percentage = sum(results.values())
    print(f"Total Percentage: {total_percentage:.2f}%")

    # Output results
    for hand_type, percentage in results.items():
        print(f"{hand_type}: {percentage:.8f}%")

    # Create a chart
    hand_types = list(results.keys())
    percentages = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.barh(hand_types, percentages)
    plt.xlabel('%')
    plt.show()


if __name__ == '__main__':
    evaluate_hand(100000)

"""
Ausgabe bei 10.000.000 durchläufen:
Total Percentage: 100.00%
Royal Flush: 0.00021000%
Straight Flush: 0.00206000%
Quads: 0.02299000%
Full House: 0.13588000%
Flush: 0.34792000%
Straight: 0.40952000%
Three of a Kind: 2.04132000%
Two Pair: 4.60060000%
One Pair: 41.50449000%
High Card: 50.93501000%
"""

