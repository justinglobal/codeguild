"""
logic.py file for jokes project
"""

jokes_dict = {}

def save_joke(setup_text, punchline_text):
    """save joke setup_text and punchline_text"""
    jokes_dict[setup_text] = punchline_text

def get_all_setups():
    """gets all joke setups defined as keys from jokes_dict"""
    return jokes_dict.keys()

def get_all_punchlines():
    """gets all joke punchlines defined as values from jokes_dict"""
    return jokes_dict.values()



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
