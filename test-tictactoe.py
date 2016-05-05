import practice_interface
import unittest


# DictTest
# class TestDictTTTBoard(unittest.TestCase):
#     def test_place(self):
#         pos_to_token = {
#             'a1': ' ', 'b1': ' ', 'c1': ' ',
#             'a2': ' ', 'b2': ' ', 'c2': ' ',
#             'a3': ' ', 'b3': ' ', 'c3': ' ',
#         }
#         expected_result = {
#             'a1': ' ', 'b1': ' ', 'c1': ' ',
#             'a2': ' ', 'b2': 'X', 'c2': ' ',
#             'a3': ' ', 'b3': ' ', 'c3': ' ',
#         }
#         found = practice_interface.place.TestDictTTT(pos_to_token)
#         expected = expected_result
#
#         assert found == expected

class TestListListTTTBoard(unittest.TestCase):
    def test_place_list(self):
        test_board = practice_interface.ListListTTTBoard()
        test_board.place(1, 1, 'X')
        found = test_board.rows
        expected = [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]
        assert found == expected

    def test_won(self):
        test_board = practice_interface.ListListTTTBoard()
        found1 = test_board.won()
        #check diagonal also
        assert found1 == None



