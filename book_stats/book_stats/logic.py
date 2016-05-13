import random
with open ('book_stats/booktofactordjango.txt') as book_text:
    book_lines = book_text.readlines()
# with open ('booktofactordjango.txt') as book_text:
#     book_lines = book_text.readlines()
    #opens, reads lines, then closes
def make_word_list():
    """Makes list of book words by joining, lowercasing all words, removing '\n' & other puncutation, then splitting into list of words"""
    return ' '.join(book_lines).lower().replace('\n' , '').replace('.', '').replace(',' , '').split()

def calc_total_words():
    """Does raw count of all items in list book_word_list"""
    return (len(book_word_list))

def get_unique_words():
    """Gets unique words in book_word_list by changing it to a set"""
    return (list(set(book_word_list)))

def calc_total_unique_words():
    """Does a raw count of all items in list unique_word_list"""
    return (len(unique_word_list))

def make_wordfreq_dict(book_word_list, words_to_count):
    """Makes dictionary populated by word as key and word frequency in text as value"""
    for word in book_word_list:
        words_to_count[word] = book_word_list.count(word)
#this code is covered by what David suggested below
def make_top_ten(words_to_count):
    """Makes top 10 list of most frequent words by zipping top 10 of sorted lists fr key/value pairs in words_to_count dict  """
    return [
        list(x)
        for x
        in zip(
            sorted(words_to_count.keys(), key=words_to_count.get, reverse=True)[:10],
            sorted(words_to_count.values(), reverse=True)[:10]
        )
    ]
#this code is covered by what David suggested below
    ###start refactoring here!!!!! this is David's tip to improve code above figure it out
    # def get_count_from_pair(pair):
    #     word, count = pair
    #     return count
    # return sorted(words_to_count.items(), key=get_count_from_pair, reverse=True)[:10]

"""finds word frequency for input word"""

def find_word_freq(word_from_django):
    if word_from_django in words_to_count.keys():
        return words_to_count[word_from_django]
    else:
        return 0


words_to_count = {}
book_word_list = make_word_list()
totalnum_ofwords = calc_total_words()
unique_word_list = get_unique_words()
totalnum_ofunique = calc_total_unique_words()
make_wordfreq_dict(book_word_list, words_to_count)
top_ten = make_top_ten(words_to_count)

test_freq = find_word_freq('thematrix')

print(test_freq)

# print (sorted(words_to_count, key=words_to_count.get, reverse=True)[:10])
# print (sorted(words_to_count.values(), reverse=True)[:10])
#
# print ('These are the top ten most frequent words in the text and their frequency:')
# for item in (top_ten):
#   print (item[0], item[1])
