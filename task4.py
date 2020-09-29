import collections
from timeit import timeit

d1 = {1: 1, 2: 2, 3: 3}
d2 = collections.OrderedDict(sorted(d1.items(), key=lambda t: t[0]))
print(timeit("d1.get(1)", "from __main__ import d1"))
print(timeit("d2.get(1)", "from __main__ import d2"))
print(timeit("d1.keys()", "from __main__ import d1"))
print(timeit("d2.keys()", "from __main__ import d2"))
print(timeit("d1.items()", "from __main__ import d1"))
print(timeit("d2.items()", "from __main__ import d2"))