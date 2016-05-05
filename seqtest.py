
###example for how to use tuples


item_to_price_cents = {
  'apple': 99,
  'pear': 150
}

for time in item_to_price_cents:
    price = item_to_price_cents[item]

    print('{} costs {} cents'.format(item, price))

for pair in item_to_price_cents.items():
    item = pair[0]
    price =pair[1]

    print('{} costs {} cents'.format(item, price))

for item, price in item_to_price_cents.items():
    print('{} costs {} cents'.format(item, price))



prices_dollars = [1.50, 0.75]
prices_cents = []
for dollar_val in prices_dollars:
    cents_val = dollars_val * 100
    prices_cents.append(cents.val)

#list comprehention

prices_cents = [dollar_val * 100 for dollar_val in prices_dollars]

#code below finds all upper case in list
words_in_document = {'the' , 'cat' , 'hat', 'Justin'}
uppercase_words_in_document = {word.upper() for word in words_in_document}

#below uses operation on a dictionary
item_to_price_cents = {
  'apple': 99,
  'pear': 150
}

product_to_price_dollars = {
    product: prices_cents / 100
    for product, prices_cents
    in product_to_price_cents.items()
}
