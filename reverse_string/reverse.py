

def reverse_string(initial):
    reversed = ""
    for c in initial:
        reversed = c + reversed
    return reversed

initial = "abcde"
reversed = "edcba"


assert reversed == reverse_string(initial)
