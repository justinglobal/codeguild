"""
logic.py file for jokes project
"""

jokes_list = []

def save_joke(setup_text, punchline_text):
    """takes in setup_text and punchline_text, defines them as joke tuple and
    puts joke tuple into jokes_list"""
    joke = (setup_text, punchline_text)
    jokes_list.append(joke)

def get_all_setups():
    """Makes setups_list from first item in joke tuple for all joke tuples in list"""
    setups_list = [joke[0] for joke in jokes_list]
    return setups_list

def get_all_punchlines():
    """Makes punchlines_list from 2nd item in joke tuple for all joke tuples in list"""
    punchlines_list = [joke[1] for joke in jokes_list]
    return punchlines_list



# jokes_dict = {}
#
# def save_joke(setup_text, punchline_text):
#     """save joke setup_text and punchline_text"""
#     jokes_dict[setup_text] = punchline_text
#
# def get_all_setups():
#     """gets all joke setups defined as keys from jokes_dict"""
#     return jokes_dict.keys()
#
# def get_all_punchlines():
#     """gets all joke punchlines defined as values from jokes_dict"""
#     return jokes_dict.values()



# comments = []
#
#
# def save_comment(comment_text):
#     """Save a new comment.
#     """
#     comments.append(comment_text)
#
#
# def get_all_comments():
#     """Return all previously saved comments as a list of strings."""
#     return comments
