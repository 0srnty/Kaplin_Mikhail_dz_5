import collections
from timeit import timeit

l1 = [1, 1]
d1 = collections.deque(l1)
print(timeit("l1.append(1)", "from __main__ import l1"))
print(timeit("d1.append(1)", "from __main__ import d1"))
print(timeit("l1.pop()", "from __main__ import l1"))
print(timeit("d1.pop()", "from __main__ import d1"))




