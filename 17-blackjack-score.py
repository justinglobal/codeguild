#this program scores a blackjack hand that a user enters

#make a dealer, have dealer's hand be random generated

# class Card:
#     def __init__(self, card_type, card_suit, card_value):
#         self.card_type = card_type
#         self.card_suit = card_suit
#         self.card_value = card_value
#     def __eq__(self, other_entry):
#         return (self.card_type == other_entry.card_type)
#     def __repr__(self):
#         return 'Card({}{})'.format(self.card_type, self.card_suit)
#     def score_hand(self):
#         if self.card_type in current_hand == item in ['K', 'Q', 'J']:
#             self.card_value = 10
class Card:
    def __init__(self, card_type, card_suit):
        self.card_type = card_type
        self.card_suit = card_suit
    def __eq__(self, other_entry):
        return (self.card_type == other_entry.card_type)
    def __repr__(self):
        return 'Card({},{})'.format(self.card_type, self.card_suit)
    def make_card_different_somehow(self):
        print (self.card_type , self.card_suit)

def funcitons_are_awesome:
    print "yeah boy"





    # def make_cards_ints(self):
    #     return (self.card_type.replace(['K', '10']).replace(['Q', '10']).replace(['J', '10']))
###### ** -> Start here...def score_hand should be a top-level function??
###             we already have current_hand up there
class Hand:
    def __init__(self, hand_group):
        self.hand_group = hand_group

    def __eq__(self, other_entry):
        return (self.hand_group == other_entry.hand_group)
    def __repr__(self):
        return 'Hand({})'.format(self.hand_group)
    def add_card_to_hand(self):
        return self.hand_group.append(current_card)
    def foo_function(self):
        print ((self.hand_group)[0: ])
    def bar_function(self):
        return ((self.hand_group)[1])
    # def score_hand(self):
    #     if card in current_hand == card in ['K', 'Q', 'J']
    #         card = 10
    # def pre_hand_for_scoring(self):
    #     return self.hand_group.int

##### ** Go here next....above are possible ways to do the score in Hand class

# current_card = Card('10', 'S' , (int('10')))
current_card = Card('10', 'S')
current_hand = Hand([])
print (current_card)
print (current_hand)

Hand.add_card_to_hand(current_hand)
print (current_hand)
# current_card = Card('J', 'H', (int('10')))
current_card = Card('J', 'H')
Hand.add_card_to_hand(current_hand)
print (current_hand)
Hand.foo_function(current_hand)

Card.make_card_different_somehow(current_card)

Card.make_card_different_somehow(Hand.bar_function(current_hand))

# Card.make_cards_ints(Hand.bar_function(current_hand))

# score = Card.score_hand(current_hand)
# print (score)

# def add_card_to_hand(current_card, card_list):
#     card_list.append(current_card)
#     return card_list

# card_list = []

# card_list = add_card_to_hand(current_card, card_list)
# # card_list = [current_card, current_card]
# # num_list = [3, 4]
# print (card_list)
#
# current_card = Card('5', 'D')
# card_list = add_card_to_hand(current_card, card_list)
# current_hand = Hand(card_list)
# # current_hand = Hand(('5', 'K', '10', 'Q'))
# print (current_hand.hand_group)
