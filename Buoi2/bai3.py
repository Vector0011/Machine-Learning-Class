my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
import operator
print([a[0] for a in sorted(my_dict.items(), key=operator.itemgetter(1))])
