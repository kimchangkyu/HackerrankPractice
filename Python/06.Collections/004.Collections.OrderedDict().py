from collections import OrderedDict

ordered_dictionary = OrderedDict()

N = int(input())

for i in range(N):
    item, price = input().rsplit(" ", 1)
    if item in ordered_dictionary:
        ordered_dictionary[item] += int(price)
    else:
        ordered_dictionary[item] = int(price)

for item in ordered_dictionary:
    print(item, ordered_dictionary[item])