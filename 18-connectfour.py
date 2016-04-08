

class Board:
    def __init__(self, board_list):
        self.board_list = board_list
    def __eq__(self, other_entry):
        return (self.board_list == other_entry.board_list)
    def __repr__(self):
        return 'Board({})'.format(self.board_list)
    def place_token(self):
        self.board_list[0]['a1'] = 'Y'
        return self.board_list
# class Token:
#     def __init__(self, color):
#         self.color = color
#     def __eq__(self, other_entry):
#         return (self.place == other_entry.color)
#     def __repr__(self):
#         return 'Token({})'.format(self.color)
#     def
        #instatiating token will assign color
        #Token method (function) will alternate color for assignment to board

def main():
    """collection of functions"""
    def get_raw_text():
        with open ('4-moves.txt') as raw_moves_text:
            moves_list = raw_moves_text.readlines()
        return moves_list
    def format_moves_list(moves_list):
        ' '.join(moves_list).replace('\n' , '').split()
        return moves_list

    moves_list = (format_moves_list(get_raw_text()))

    empty_board = Board([{'a1':'', 'a2':'', 'a3':'', 'a4':'', 'a5':'', 'a6':'', 'a7':'',},
        {'b1':'', 'b2':'', 'b3':'', 'b4':'', 'b5':'', 'b6':'', 'b7':'',},
        {'c1':'', 'c2':'', 'c3':'', 'c4':'', 'c5':'', 'c6':'', 'c7':'',},
        {'d1':'', 'd2':'', 'd3':'', 'd4':'', 'd5':'', 'd6':'', 'd7':'',},
        {'e1':'', 'e2':'', 'e3':'', 'e4':'', 'e5':'', 'e6':'', 'e7':'',},
        {'f1':'', 'f2':'', 'f3':'', 'f4':'', 'f5':'', 'f6':'', 'f7':'',}])
    print (empty_board)
    empty_board.place_token()
    print ('1_____________________________________')
    print (empty_board)
    # empty_board[0]['a1'] = 'Y'
    # print (empty_board[0]['a1'])

    # move = '1'
    #
    # single_time = 0
    # while single_time < 1
    #     for row_dict in empty_board:
    #         if row_dict[] == '':
    #             sorted()
    #             single_time += 1



main()
