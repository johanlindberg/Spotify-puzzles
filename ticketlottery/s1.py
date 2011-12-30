## Spotify Software Puzzles - Ticket Lottery
##
## Given the number of people p in your group (all of which entered the
## lottery) and the total number of people m that entered the lottery, what
## is the probability that you will be able to get tickets for your entire
## group?

import doctest
import itertools

def c(x, y):
    """
    Calculate the number of ways to combine y elements from a total set of x.

    >>> c(1, 1)
    1
    >>> c(2, 1)
    2
    >>> c(3, 2)
    3
    >>> c(5, 2)
    10
    >>> c(5, 3)
    10
    >>> c(10, 3)
    120
    """
    return len([n for n in itertools.combinations(range(x), y)])

def p(x, y, m, n):
    """
    Calculate the probability to get X things out of Y in a sample of
    size M drawn from a total number of things N.

    Example:
    In a box of ten (n) lightbulbs, three (y) are defect. What is the
    probability that we get exactly one (x) defect lightbulb if we pull
    two (m) randomly from the box (if we don't put them back in the box
    in between pulls).

    >>> print "%s %%" % (int(round(p(1, 3, 2, 10) * 100)))
    47 %
    """
    return float(c(y, x)) * float(c(n - y, m - x)) / float(c(n, m))

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
    
