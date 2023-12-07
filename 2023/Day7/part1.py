def get_hand_rank(hand):
    card_counts = {}
    for card in set(hand):
        card_counts[card] = hand.count(card)
    if 5 in card_counts.values():
        return 7
    if 4 in card_counts.values():
        return 6
    if 3 in card_counts.values() and 2 in card_counts.values():
        return 5
    if 3 in card_counts.values():
        return 4
    if 2 in card_counts.values():
        if list(card_counts.values()).count(2) == 2:
            return 3
        else:
            return 2
    return 1

def get_card_rank(card):
    big_cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if card in big_cards.keys():
        return big_cards[card]
    return int(card)

def compare_hands(hand):
    comparison_order = [get_hand_rank(hand)]
    comparison_order += [get_card_rank(card) for card in hand]
    return tuple(comparison_order)

hands = [line.strip().split() for line in open("input.txt", "r").readlines()]
hands = [[hand, int(bid)] for hand, bid in hands]
hands = sorted(hands, key=lambda x: compare_hands(x[0]))
print(sum([entry[1] * (multiplier + 1) for multiplier, entry in enumerate(hands)]))