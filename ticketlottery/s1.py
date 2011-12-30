## Spotify Software Puzzles - Ticket Lottery
##
## Given the number of people p in your group (all of which entered the
## lottery) and the total number of people m that entered the lottery, what
## is the probability that you will be able to get tickets for your entire
## group?

import doctest
import itertools

def number_of_combinations(x, y):
    """
    >>> number_of_combinations(1, 1)
    1
    >>> number_of_combinations(2, 1)
    2
    >>> number_of_combinations(3, 2)
    3
    >>> number_of_combinations(5, 2)
    10
    >>> number_of_combinations(5, 3)
    10
    >>> number_of_combinations(10, 3)
    120
    """
    return len([n for n in itertools.combinations(range(x), y)])

def solve(m, n, t, p):
    """
    1 <= m <= 1000: the total number of people who entered the lottery.
    1 <= n <= m:    the total number of winners drawn.
    1 <= t <= 100:  the number of tickets each winner is allowed to buy.
    1 <= p <= m:    the number of people in your group.

    # Check that input parameters are within range
    >>> solve(0, 1, 1, 1)
    False
    >>> solve(1, 0, 1, 1)
    False
    >>> solve(1, 1, 0, 1)
    False
    >>> solve(1, 1, 1, 0)
    False
    >>> solve(1001, 1, 1, 1)
    False
    >>> solve(1, 2, 1, 1)
    False
    >>> solve(1, 1, 101, 1)
    False
    >>> solve(1, 1, 1, 2)
    False
    """

    # Make sure that input parameters are within range
    for var, min, max in [(m,1,1000), (n,1,m), (t,1,100), (p,1,m)]:
      if var < min or var > max:
        return False

if __name__ == '__main__':
    doctest.testmod()
    
