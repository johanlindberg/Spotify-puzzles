## Spotify Software Puzzles - Reversed Binary Numbers
##
## Your task will be to write a program for reversing numbers in binary. For
## instance, the binary representation of 13 is 1101, and reversing it gives
## 1011, which corresponds to number 11.

import doctest

def solve(n):
    """
    >>> solve(0) # 0b -> 0b
    0
    >>> solve(1) # 1b -> 1b
    1
    
    >>> solve(2) # 10b -> 01b
    1
    """
    return int('0b' + reverse_bin(n), base = 2)

def binary(n):
    """
    >>> binary(2)
    '10'
    >>> binary(42)
    '101010'
    """
    return bin(n)[2:]

def reverse_bin(n):
    """
    >>> reverse_bin(2) # 10b -> 01b
    '01'
    >>> reverse_bin(42) # 101010b -> 010101b
    '010101'
    """
    return "".join([x for x in reversed(binary(n))])

if __name__ == '__main__':
    doctest.testmod()
