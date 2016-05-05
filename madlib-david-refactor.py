
#madlib game David's example



def get_adj():
    """prompt user for an adj word and return it as a string."""
    print('A adj, please:')
    return input()

def get_noun_1():
    print('A noun, please:')
    return input()

def get_noun_2():
    print('A noun, please:')
    return input()

def build_madlib(adj, noun1, noun2):
    return ('A ' + adj + ' ' + noun1 + ' jumps over the ' + noun2 + '!')

adj = get_adj()
noun1 = get_noun_1()
noun2 = get_noun_2()

madlib = build_madlib(adj, noun1, noun2)

# print(get_adj.__doc__)

print(madlib)
