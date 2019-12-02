#!/usr/bin/env python
def flat_list(l):
    out = []
    for el in l:
        if type(el) == list:
            out.extend(flat_list(el))
        else:
            out.append(el)
    return out


input = [1,[2,3], [[4, [6,[7,8]]]]]
expected = [1,2,3,4,6,7,8]

result = flat_list(input)
print(result)
assert(expected == result )
