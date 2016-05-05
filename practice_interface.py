class ListListTTTBoard:
    """Tic-Tac-Toe board that implements storage as a list
    of rows, each with three slots.
    The following board results in the following data structure.
    X| |
     |X|O
     | |
    [
        ['X', ' ', ' '],
        [' ', 'X', 'O'],
        [' ', ' ', ' '],
    ]
    """

    def __init__(self):
        """Initializes an empty board."""
        self.rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.
        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        row = x collumn = y
        """
        self.rows[y][x] = player
        # pass

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        lists_transposed_for_score = list(zip(*self.rows))
        transposed_list_no_tuples = [list(tuples) for tuples in lists_transposed_for_score]
        # print(transposed_list_no_tuples)
        winner = None
        for row_list_item in self.rows:
            if row_list_item == ['X', 'X', 'X']:
                winner = 'X'
            elif row_list_item == ['O', 'O', 'O']:
                winner = 'O'
        for row_list_item in transposed_list_no_tuples:
            if row_list_item == ['X', 'X', 'X']:
                winner = 'X'
            elif row_list_item == ['O', 'O', 'O']:
                winner = 'O'
        return winner

    def __str__(self):
        """Returns a string representation of the board.
        Should be three rows with each cell separated by a '|'.
        X| |
         |X|O
         | |
        """
        rows_joined_list = ['|'.join(row_list_item) for row_list_item in self.rows]
        str_to_print = '\n'.join(rows_joined_list)
        return '{}\n'.format(str_to_print)
        # pass


class DictTTTBoard:
    """Tic-Tac-Toe board that implements storage as a flat
    dictionary of slots.
    The following board results in the following data structure.
    X| |
     |X|O
     | |
    {
        'a1': 'X', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': 'X', 'c2': 'O',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    }
    """

    def __init__(self):
        """Initializes an empty board."""
        self.pos_to_token = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' ',
        }
                            #token
    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.
        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        #this is pre-fipped for k, v # that makes token_to_pos = {
        #     'a1': (0,0), 'b1': (0,1), 'c1': (0,2),
        #     'a2': (1,0), 'b2': (1,1), 'c2': (1,2),
        #     'a3': (2,0), 'b3': (2,1), 'c3': (2,2),
        #     }
        token_to_pos = {
        (2,0): 'a3', (2,1): 'b3', (2,2): 'c3',
        (1,2): 'c2', (1,0): 'a2', (0,0): 'a1',
        (0,2): 'c1', (0,1): 'b1', (1,1): 'b2'
        }

        move_tuple = y,x
        print(move_tuple)

        move_key = token_to_pos[move_tuple]
        print(move_key)
        self.pos_to_token[move_key] = player
        # print(self.pos_to_token)


    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        pass

    def __str__(self):
        """Returns a string representation of the board.
        Should be three rows with each cell separated by a '|'.
        X| |
         |X|O
         | |
        """


        # return '{}\n'.format(str_to_print)

        return str(self.pos_to_token.values())


class CoordsTTTBoard:
    """Tic-Tac-Toe board that implements storage as a list of x, y, token triplets.
    An empty board is an empty list.
    Each token that is on the board adds one item to the triplet list.
    The following board results in the following data structure.
    X| |
     |X|O
     | |
    [(0, 0, 'X'), (1, 1, 'X'), (2, 1, 'O')]
    """

    def __init__(self):
        """Initalizes an empty board."""
        self.x_y_token_triplets = []

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.
        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        pass

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        pass

    def __str__(self):
        """Returns a string representation of the board.
        Should be three rows with each cell separated by a '|'.
        X| |
         |X|O
         | |
        """
        pass


def play(board):
    """Plays a test game on an empty board.
    Asserts that the board is working properly.
    """
    board.place(1, 1, 'X')
    print(board)
    board.place(0, 0, 'O')
    print(board)
    board.place(1, 0, 'X')
    print(board)#print(repr(str(board)))
    assert str(board) == "O|X| \n |X| \n | | \n"
    print(board)
    board.place(0, 2, 'O')
    print(board)
    assert board.won() is None
    board.place(1, 2, 'X')
    print(board)
    assert board.won() == 'X'


def main():
    # board1 = DictTTTBoard()
    # play(board1)
    board2 = ListListTTTBoard()
    play(board2)
    # board3 = CoordsTTTBoard()
    # play(board3)


main()
