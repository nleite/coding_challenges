#!/bin/env python

def word_paragraph_count(paragraph):
    lines = paragraph.split("\n")
    print(lines)
    counts = [0]

    for p in lines:
        if p == "":
            counts.append(0)
            continue
        words = [x for x in p.split(" ") if len(x) > 1]

        counts[-1] =  counts[-1]  + len(words)

    counts = filter(lambda x: x != 0, counts)
    t = tuple(counts)
    print t
    return t

para1 = "howdy, that is all!"
e1 = (4,)

assert e1 == word_paragraph_count(para1)

para2 = """
The wind would walk through milles
Glamour would be uppon us a
Passing the thoughts

Hi!
There
"""

e2 = (14, 2)
assert e2 == word_paragraph_count(para2)
