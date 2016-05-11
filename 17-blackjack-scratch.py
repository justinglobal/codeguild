#this program scores a blackjack hand that a user enters

class Card:
    def __init__(self, card_type, card_suit):
        self.card_type = card_type
        self.card_suit = card_suit
    def __eq__(self, other_entry):
        return (self.card_type == other_entry.card_type)
    def __repr__(self):
        return 'Card({}{})'.format(self.card_type, self.card_suit)

class Hand:
    def __init__(self, hand_group):
        self.hand_group = hand_group
    def __eq__(self, other_entry):
        return (self.hand_group == other_entry.hand_group)
    def __repr__(self):
        return 'Hand({})'.format(self.hand_group)

def add_card_to_hand(current_card, card_list):
    card_list.append(current_card)
    return card_list
# def score_hand

card_list = []
current_card = Card('10', 'S')
print (current_card)
card_list = add_card_to_hand(current_card, card_list)
# card_list = [current_card, current_card]
# num_list = [3, 4]
print (card_list)
current_card = Card('5', 'D')
card_list = add_card_to_hand(current_card, card_list)
current_hand = Hand(card_list)
# current_hand = Hand(('5', 'K', '10', 'Q'))
print (current_hand.hand_group)
