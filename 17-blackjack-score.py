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
    def make_another_change(self):
        print (self.card_type.replace('J', '10'))
        #make 'all cards here?'
# class Hand:
#     def __init__(self, hand_list):
#         self.hand_list = hand_list
#     def __eq__(self, other_entry):
#         return (self.hand_list == other_entry.hand_list)
#     def __repr__(self):
#         return 'Hand({})'.format(self.hand_list)
#     def add_card_to_hand(self, current_card):
#         return self.hand_list.append(current_card)
#     def foo_function(self):
#         print (self.hand_list)
#         print (self.hand_list[1].card_type)
#     def bar_function(self):
#         return self.hand_list[1] # .card_type
class Hand:
    def __init__(self, hand_list):
        self.hand_list = hand_list
    def __eq__(self, other_entry):
        return (self.hand_list == other_entry.hand_list)
    def __repr__(self):
        return 'Hand({})'.format(self.hand_list)
    def add_card_to_hand(self, current_card):
        return self.hand_list.append(current_card)
    def foo_function(self):
        print (self.hand_list)
        print (self.hand_list[1].card_type)
    def bar_function(self):
        return self.hand_list[1] # .card_type
    # def make_card_type_list(self):
    #     return [int(item.card_type.replace(
    #     'J', '10').replace(
    #     'Q', '10').replace(
    #     'K', '10').replace(
    #     'A', '11')) for item in self.hand_list]

    def make_cards_ints(self):
        return [int(item.card_type.replace(
        'J', '10').replace(
        'Q', '10').replace(
        'K', '10')) for item in self.hand_list]

    def calc_score(self):


    # def make_cards_ints(self):
    #     if sum([int(item.card_type.replace(
    #     'J', '10').replace(
    #     'Q', '10').replace(
    #     'K', '10').replace(
    #     'A', '11')) for item in self.hand_list]) <= 21:
    #         return [int(item.card_type.replace(
    #         'J', '10').replace(
    #         'Q', '10').replace(
    #         'K', '10').replace(
    #         'A', '11')) for item in self.hand_list]
    #     else:
    #         return [int(item.card_type.replace(
    #         'J', '10').replace(
    #         'Q', '10').replace(
    #         'K', '10').replace(
    #         'A', '1')) for item in self.hand_list]
#two cleaner steps
#logic errors ex: what if two aces? returns min sum...
# card_type to score
def main():
    current_card = Card('K', 'S')
    current_hand = Hand([])
    print (current_card)
    print (current_hand)
    # print ('1_____________________________________')
    Hand.add_card_to_hand(current_hand, current_card)
    # print (current_hand)
    # print ('2_____________________________________')

    current_card = Card('K', 'H')
    Hand.add_card_to_hand(current_hand, current_card)
    # current_card = Card('A', 'D')
    # Hand.add_card_to_hand(current_hand, current_card)
    print (current_hand)
    # print ('3_____________________________________')
# def ghgj():
    # Hand.foo_function(current_hand)
    # print ('4_____________________________________')
    # Card.make_card_different_somehow(current_card)
    #
    # Card.make_card_different_somehow(Hand.bar_function(current_hand))
    #
    # print ('5_____________________________________')
    # Card.make_another_change(Hand.bar_function(current_hand))
    # print ('6_____________________________________')
    # print (Hand.bar_function(current_hand))
    print ('7_____________________________________')
    # print ('score:' , sum(Hand.make_cards_ints(current_hand)))
    print (Hand.make_cards_ints(current_hand))

###start here this works
#     print (calc_score(current_hand))
#
#
# def calc_score(current_hand):
#     return sum(Hand.make_card_type_list(current_hand))

    #david reminder
    # def add_int_to_list(l, i):
    #     l.append(i)
    #
    # l = []
    # add_int_to_list(l, 5)


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
    # print (current_hand.hand_list)

main()
