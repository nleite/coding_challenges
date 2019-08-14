#!/bin/env python

def change_count(money, coins):
    '''Return the number of possible coin combinations to return the money
    amount of coins.
    The order of coin sequences do not matter i.e. [1,1,2] == [2,1,1] == [1,2,1]
    '''
    combinations = 0
    # ...
    return combinations


def main():

    # Test cases
    assert change_count(4, [-1, 2, 5]) == 1 # [2,2]

    assert change_count(5, [1,2]) == 3 # [1,1,1,1,1] [1,1,1,2] [1,2,2]

    assert change_count(10, [1,2,5]) == 10 # [1,1,1,1,1,1,1,1,1,1] [1,1,1,1,1,1,1,1,2] [1,1,1,1,1,1,2,2] [1,1,1,1,2,2,2] [1,1,2,2,2,2] [1,1,1,1,1,5] [1,1,1,2,5] [1,2,2,5] [2,2,2,2,2] [5,5]

    assert change_count(7, [3,5]) == 0

if __name__ == "__main__":
    main()
