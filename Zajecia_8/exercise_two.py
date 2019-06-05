tuple_examples = ('element one', 2, '3', 'four')
print(type(tuple_examples))
n = 0
for element in tuple_examples:
    print(element)
    n += 1

print('This tuple has: {0} elements'.format(n))
print('Let\'s add an element to index {0}!'. format(n))

try:
    tuple_examples[n] = 'next element'
except TypeError:
    print("You can not change a tuple... Moron...")

print("Let\'s change an element!")
try:
    tuple_examples[0] = 1
except TypeError:
    print("You can not change a tuple as I have told you... Moron x2...")
