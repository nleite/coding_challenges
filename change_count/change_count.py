#!/bin/env python

def filter_coins(coins, money):
    '''Removes any coin that are either larger than the ``money`` or negative
    values - there should not be a negative value coin'''
    valid_coins = []
    for c in coins:
        if c < 1:
            continue
        if c > money:
            continue
        valid_coins.append(c)

    return valid_coins


def recur_elements(money, matrix, combination, current, next):
    compared = money - sum(combination)
    #print(combination)
    if compared < 0:
        popped = combination.pop()
        if len(next) == 0:
            return
        if current == popped:
            current = next.pop()
        combination.append(current)
        return recur_elements(money, matrix, combination, current, next)
    if compared > 0:
        combination.append(current)
        return recur_elements(money, matrix, combination, current, next)
    if compared == 0:
        # copy the combination into the matrix as a sorted tuple
        found = combination[:]
        found.sort()
        matrix.add(tuple(found))
        if len(next) == 0:
            return
        popped = combination.pop()
        if current == popped:
            if combination.pop() == current:
                current = next.pop()
        return recur_elements(money, matrix, combination, current, next)


def change_count(money, coins):
    '''Return the number of possible coin combinations to return the money
    amount of coins.
    The order of coin sequences do not matter i.e. [1,1,2] == [2,1,1] == [1,2,1]
    '''
    # filter all invalid coin values
    coins = filter_coins(coins, money)
    # keep a set of all possible combinations
    matrix = set()
    #print(money)
    # for each coin
    for c in coins:
        # in each position
        for i, _ in enumerate(coins):
            # create a tree of combinations, and store the matching combinations in a set
            recur_elements(money, matrix, [c], coins[i], coins[:])
    # return the size of the set of matching combinations 
    #print( matrix )
    return len(matrix)


def main():

    # Test cases
    assert change_count(4, [-1, 2, 5]) == 1 # [2,2]

    assert change_count(5, [1, 2]) == 3 # [1,1,1,1,1] [1,1,1,2] [1,2,2]

    assert change_count(10, [1, 2, 5]) == 10 # [1,1,1,1,1,1,1,1,1,1] [1,1,1,1,1,1,1,1,2] [1,1,1,1,1,1,2,2] [1,1,1,1,2,2,2] [1,1,2,2,2,2] [1,1,1,1,1,5] [1,1,1,2,5] [1,2,2,5] [2,2,2,2,2] [5,5]

    assert change_count(7, [3, 5]) == 0

    assert change_count(8, [1, 2, 3, 4]) == 15 # [1,1,1,1,1,1,1,1] [1,1,1,1,1,1,2] [1,1,1,1,2,2] [1,1,2,2,2] [2,2,2,2] [2,2,4] [3,3,2] [3,4,1] [3,1,2,2] [3,3,1,1] [3,1,1,1,1,1] [4,4] ...

if __name__ == "__main__":
    main()
