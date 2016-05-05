test_board = [
['', '', '', '', '', '', ''],
['', '', '', '', '', '', ''],
['', '', '', '', '', '', ''],
['', '', '', '', '', '', ''],
['', '', '', '', '', '', ''],
['', 'R', '', '', '', '', '']
]
# current_token = Token('R')
current_move = 2
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

# drop(test_board, 1, 'Y')
# print(test_board)



# row_index = find_first_empty_row_index(test_board, col_index)
row_index = find_first_empty_row_index(test_board, col_index)
print(row_index)
# place_token(test_board, row_index, col_index, 'Y')
# print(test_board)
#
# while
## print (test_board)
# print('1_____________________________________')
#
# for row in reversed(test_board):
#     tag = 0
#     while tag < 1:
#         if row[1] in reversed(test_board) == '':
#             row[1] = 'R'
#         else:
#             tag += 1
#
# for row in reversed(test_board):
#     if row[current_move-1] == '':
#         row[current_move-1] = 'Y'
#
# # test_list = ['', '', '', 'R']
# #
# # output_list = [i for i,x in enumerate(test_list) if x == '']
#
# # for i,x in enumerate(test_list):
# #     if x == ''
# #     return output_list
#
# # print(output_list)
#
# # for row in reversed(test_list):
# #     if row[current_move-1] == '':
# #         # position = "whatever row we are on"
# #         row[current_move-1] = 'Y'
# #print(row[current_move-1])
#
#
#
#
#
# # some_list = [i for i, x in enumerate(reversed(test_board)) if x == '']
#
# # print(some_list)
# #
# print(test_board)
# print(test_board[5][1])
#
# # print('updated')
#
#
#
#
#
#
#     # print(row[current_move-1])
#
#     # if row[current_move-1] == '':
#     #     row[current_move-1] = 'R'
#
#
# # move = '2'
# # # indexed_item = 0
# # for indexed_item in board_list_of_dicts:
# #     print(indexed_item)
# #     if indexed_item['a' + move] == '':
# #         indexed_item['a' + move] = 'R'
# #     elif indexed_item['b' + move] == '':
# #         indexed_item['b' + move] = 'R'
# #     elif indexed_item['c' + move] == '':
# #         indexed_item['d' + move] = 'R'
#
#
#
#
#
# # keys_list = list(sorted(dict_1.keys()))
# # print (keys_list)
# # collumn = 2
# # print (((keys_list)[collumn - 1])[-1])
#
#
# # current_board = board_list_of_dicts
# #
# # def format_current_board(current_board):
# #     row_dict = {}
# #     move = 2
# #     print (current_board)
# #     # if board_list_of_dicts
# #         # for row_dict in current_board:
# #         #     if row_dict[key where move is in key.name] == '':
# #     need to update current_board with 'R' in the list of the bottom row (a)
# #         # if row_dict[key where move is in key.name] == '':
# #         row_dict['a2'] = 'R'
# #         keys_list = list(sorted(row_dict.keys()))
# #
# #     print (keys_list)
# #     # print (((keys_list)[0])[-1])
# #     print (((keys_list)[move - 1])[-1])
# #
# # format_current_board(current_board)
