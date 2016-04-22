

class Board:
    def __init__(self, board_list_of_dicts):
        self.board_list_of_dicts = board_list_of_dicts
    def __eq__(self, other_entry):
        return (self.board_list_of_dicts == other_entry.board_list_of_dicts)
    def __repr__(self):
        return 'Board({})'.format(self.board_list_of_dicts)
###new functions are below, need to be put in classes
##next step is to integrate 'color' into workflow    
col_index = current_move - 1
def find_first_empty_row_index(board, col_index):
    for pair in reversed(list(enumerate(board))):
        # print(pair)
        row_index = pair[0]
        row = pair[1]
        if row[col_index] == '':
            return row_index

def place_token(board, row_index, col_index, color):
    board[row_index][col_index] = color



class Token:
    def __init__(self, color):
        self.color = color
    def __eq__(self, other_entry):
        return (self.place == other_entry.color)
    def __repr__(self):
        return 'Token({})'.format(self.color)
    # def make_move(self):
    #     self.color = 'Y'
    #     return
        # instatiating token will assign color
        # Token method (function) will alternate color for assignment to board

def main():
    """collection of functions"""
    def get_raw_text():
        with open ('4-moves.txt') as raw_moves_text:
            moves_list = raw_moves_text.readlines()
        return moves_list
    def format_moves_list(moves_list):
        ' '.join(moves_list).replace('\n' , '').split()
        print(moves_list)
        return moves_list

    moves_list = (format_moves_list(get_raw_text()))

    current_board = Board([
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '']
    ])

    # test_board = [
    # ['', '', '', '', '', '', ''],
    # ['', '', '', '', '', '', ''],
    # ['', '', '', '', '', '', ''],
    # ['', '', '', '', '', '', ''],
    # ['', '', '', '', '', '', ''],
    # ['', '', '', '', '', '', '']
    # ]
    # current_token = Token('R')
    # current_move = 2


    # current_board.place_token(current_move)
    print ('1_____________________________________')
    print (test_board)
    row_index = find_first_empty_row_index(test_board, col_index)
    # current_board[0]['a1'] = 'Y'
    # print (current_board[0]['a1'])

    # move = '1'
    #
    # single_time = 0
    # while single_time < 1
    #     for row_dict in current_board:
    #         if row_dict[key where move is in key.name] == '':
    #             sorted()
    #             single_time += 1



main()
