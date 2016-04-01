

#this is a code hint i got from google that I want to remember
#it removes a character from each str item in a list of str's
# mylist = [("aaaa8"),("bb8"),("ccc8"),("dddddd8")]
# mylist = ' '.join(mylist).replace('8','').split()
# print mylist

#bad_chars = ('\n' , '.' , ',')
import random
with open ('booktofactor.txt') as book_text:
    book_lines = book_text.readlines()
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
    def get_count_from_pair(pair):
        word, count = pair
        return count
    return sorted(words_to_count.items(), key=get_count_from_pair, reverse=True)[:10]


words_to_count = {}
book_word_list = make_word_list()
totalnum_ofwords = calc_total_words()
unique_word_list = get_unique_words()
totalnum_ofunique = calc_total_unique_words()
make_wordfreq_dict(book_word_list, words_to_count)
top_ten = make_top_ten(words_to_count)

# Prototypeing tip from David

# lines_of_book = asdflasdjfl
# book_word_list = make_word_list_from_lines(lines_of_book)
# unique_word_book_list = find_unique_words(book_word_list)
# words_to_count = calc_word_freq(book_word_list, unique_word_book_list)
# top_ten_word_count_pairs = make_top_ten_pairs(words_to_count)

# words_to_count = {}
# words_to_count = make_wordfreq_dict()
# book_word_list = (list(book_word_list))

#code below is my for loop to make my word/freq dictionary
# for word in book_word_list:
#     words_to_count[word] = book_word_list.count(word)
#this code will make a my dict into tuples
# [(k,v) for (k,v) in d.items()]
print (sorted(words_to_count, key=words_to_count.get, reverse=True)[:10])
print (sorted(words_to_count.values(), reverse=True)[:10])
# print ('These are the top ten most frequent words in the text and their frequency:' , top_ten)
# print [list(x) for x in zip((sorted(words_to_count, key=words_to_count.get, reverse=True)[:10]), (sorted(words_to_count.values(), reverse=True)[:10]))]
print ('These are the top ten most frequent words in the text and their frequency:')
for item in (top_ten):
  print (item[0], item[1])

# [list(x) for x in zip(list1, list2)]
# [[1, 'a'], [2, 'b'], [3, 'c']]

# print (book_word_list.count('The'))
# print (book_word_list.count('the'))
# print (book_word_list.count('paper'))
# print (totalnum_ofunique)
# print (totalnum_ofwords)
#print (word_dict)
#print (book_lines)
# print (max(book_word_list))
#
# book_word_list.sort(key=max, reverse=True)
# # print (book_word_list)
# for i in range(10):
#     print (book_word_list[i])


# for item in book_lines:
    # item.remove('\n')


# book_lines_remove = book_lines.remove('\n')
# print (book_lines_remove)

# book_lines_str = '\n'.join(book_lines)
#
# book_lines_split = book_lines_str.split(' ')
#
# print(book_lines_split)

# book_lines_stripd = book_lines.strip()
#
# print (book_lines_stripd)

#code below selects a random line, strips the characters and prints it
# random_text_line = random.choice(book_lines).strip()
# print(random_text_line)

#print (book_lines)

#the code below selects a length to display but doesn't work properly
# selected_word = ''
# while (len(selected_word)) <= 3:
#     selected_word = random.choice(book_lines).strip()
#
#     print(selected_word)


#the code below formats two values as name and number from the book_lines
# for line in book_lines:
#     name, number = line.strip().split()
#     print("{} - {}".format(name, number))
