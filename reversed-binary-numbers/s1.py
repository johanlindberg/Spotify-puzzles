## Spotify Software Puzzles - Reversed Binary Numbers
##
## Your task will be to write a program for reversing numbers in binary. For
## instance, the binary representation of 13 is 1101, and reversing it gives
## 1011, which corresponds to number 11.

import doctest

def solve(n):
    """
    >>> solve(0) # 0b0 -> 0b0
    0
    >>> solve(1) # 0b1 -> 0b1
    1
    
    >>> solve(2) # 0b10 -> 0b01
    1

    >>> solve(13)
    11
    >>> solve(47)
    61
    """
    b = bin(n)[2:] # strip the leading '0b'
    r = "".join([x for x in reversed(b)])
    return int(r, base = 2)

if __name__ == '__main__':
    doctest.testmod()
