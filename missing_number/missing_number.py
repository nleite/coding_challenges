#!/bin/env python

import random
def missing_number(sequence, max):
    sum_sq = reduce(lambda x, y: int(x)+int(y), sequence)
    sum_max = reduce(lambda x,y: x+y, range(max))
    return sum_max - sum_sq

max0 = 250
e0 = 235
sq0 = [ str(x) for x in range(250) if x != e0 ]
random.shuffle(sq0)
assert e0 == missing_number(sq0, max0)
