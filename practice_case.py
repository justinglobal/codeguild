#this program changes 'case' types ex: from CamelCase to snake_case

# init_word = 'case_matters'


def camel_to_snake(init_word):
    letter_list = list(init_word)
    for letter in letter_list:
        if letter.isupper() == True:
            letter = 'BOOMSHACKALACKA'

def snake_to_camel(init_word):
    word_list = init_word.split('_')
    capital_list = [item.capitalize() for item in word_list]
    return ''.join(capital_list)

def main():

    init_word = "case_matters"
    init_word2 = 'CaseMatters'
    print(init_word)
    print(snake_to_camel(init_word))
    print(init_word2)
    print(camel_to_snake(init_word2))
main()
