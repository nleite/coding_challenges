#!/bin/env python


def is_palindrome(word):
    for i, c in enumerate(word):
        idx = (i*-1) - 1
        print(word[idx])
        if c != word[idx]:
            return False
        if idx == c:
            break
    return True


assert is_palindrome("bab")

assert !is_palindrome("norberto")

assert is_palindrome("1235321")

assert is_palindrome("abba")
