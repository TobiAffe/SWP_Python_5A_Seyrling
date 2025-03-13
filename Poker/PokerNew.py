import random
import numpy as np
import functools
import time
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer
def get_suit(card, numbers_len):
    return card // numbers_len

def get_number(card, numbers_len):
    return card % numbers_len

def str_card(card, suits_ascii, numbers, numbers_len):
    return suits_ascii[get_suit(card, numbers_len)] + numbers[get_number(card, numbers_len)]

def str_cards(cards, suits_ascii, numbers, numbers_len):
    return " ".join(str_card(card, suits_ascii, numbers, numbers_len) for card in cards)

def shuffle_cards(cards):
    for i in range(len(cards)):
        ran = random.randint(i, len(cards) - 1)
        cards[ran], cards[i] = cards[i], cards[ran]

def draw_cards(count, cards):
    if count > len(cards):
        raise ValueError(f"Cannot draw {count} cards. Only {len(cards)} cards are available.")
    return cards[-count:]

def sort_cards(cards, numbers_len):
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if cards[i] % numbers_len > cards[j] % numbers_len:
                cards[i], cards[j] = cards[j], cards[i]
    return cards

def has_straight(cards, numbers_len):
    cards_copy = cards.copy()
    if get_number(cards_copy[0], numbers_len) == 0 and get_number(cards_copy[-1], numbers_len) == 12:
        cards_copy.pop()

    is_straight = True
    for i in range(len(cards_copy) - 1):
        if get_number(cards_copy[i], numbers_len) + 1 != get_number(cards_copy[i + 1], numbers_len):
            is_straight = False
            break

    return is_straight

def has_flush(cards, numbers_len):
    suit_cards = [get_suit(card, numbers_len) for card in cards]
    return len(np.unique(suit_cards)) == 1

def has_pair(cards, how_many, numbers_len):
    pair_cards = np.zeros(numbers_len)
    for card in cards:
        pair_cards[get_number(card, numbers_len)] += 1

    return np.sum(pair_cards == how_many)

@timer
def evaluate_hand(hands_count):
    suits_ascii = ["\u2663", "\u2660", "\u2666", "\u2665"]
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'B', 'D', 'K', 'A']
    suits_len = len(suits_ascii)
    numbers_len = len(numbers)
    count = int(input("Draw how many cards:"))

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

    hand = []

    for _ in range(hands_count):
        deck = [i for i in range(suits_len * numbers_len)]
        shuffle_cards(deck)

        try:
            hand = draw_cards(count, deck)
        except Exception as e:
            print(f"Error: {e}")

        hand = sort_cards(hand, numbers_len)

        is_flush = has_flush(hand, numbers_len)
        is_straight = has_straight(hand, numbers_len)
        is_straight_flush = is_straight and is_flush
        royal_flush_numbers = {8, 9, 10, 11, 12}
        hand_numbers = [get_number(card, numbers_len) for card in hand]
        is_royal_flush = is_straight_flush and royal_flush_numbers.issubset(hand_numbers)

        if is_royal_flush:
            results["Royal Flush"] += 1
        elif is_straight_flush:
            results["Straight Flush"] += 1
        elif has_pair(hand, 4, numbers_len) == 1:
            results["Quads"] += 1
        elif has_pair(hand, 3, numbers_len) == 1 and has_pair(hand, 2, numbers_len) == 1:
            results["Full House"] += 1
        elif is_flush:
            results["Flush"] += 1
        elif is_straight:
            results["Straight"] += 1
        elif has_pair(hand, 3, numbers_len) == 1:
            results["Three of a Kind"] += 1
        elif has_pair(hand, 2, numbers_len) == 2:
            results["Two Pair"] += 1
        elif has_pair(hand, 2, numbers_len) == 1:
            results["One Pair"] += 1
        else:
            results["High Card"] += 1

    # Calculate percentages
    total_hands = sum(results.values())
    for hand_type in results:
        results[hand_type] = (results[hand_type] / total_hands) * 100 if total_hands > 0 else 0

    # Output results
    for hand_type, percentage in results.items():
        print(f"{hand_type}: {percentage:.2f}%")

def main():
    try:
        evaluate_hand(100000)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()