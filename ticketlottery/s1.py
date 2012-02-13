## Spotify Software Puzzles - Ticket Lottery
##
## Given the number of people p in your group (all of which entered the
## lottery) and the total number of people m that entered the lottery, what
## is the probability that you will be able to get tickets for your entire
## group?

#import doctest
import math
import sys

def comb(x, y):
    """
    Calculate the number of ways to combine y elements from a total set of x.
    This is basically the same as len(itertools.combinations(x,y)).

    >>> comb(1, 1)
    1.0
    >>> comb(2, 1)
    2.0
    >>> comb(3, 2)
    3.0
    >>> comb(5, 2)
    10.0
    >>> comb(5, 3)
    10.0
    >>> comb(10, 3)
    120.0
    """
    return float(math.factorial(x)) / (float(math.factorial(y)) *
                                       float(math.factorial(x - y)))

def gen_prob(p, n, m):
    """
    Generate a probability function for the hypergeometric distribution.

    The generated function takes one parameter (x) and calculates the
    probability to get X things out of P in a sample of size N drawn from
    a total number of things M.

    Example:
    In a box of ten (m) lightbulbs, three (p) are defect. What is the
    probability that we get exactly one (x) defect lightbulb if we pull
    two (n) randomly from the box (if we don't put them back in the box
    in between pulls).

    >>> prob = gen_prob(3, 2, 10)
    >>> print "%s %%" % (int(round(prob(1) * 100)))
    47 %
    """
    def probability(x):
        try:
            return float(comb(p, x)) * float(comb(m - p, n - x)) / float(comb(m, n))
        except Exception:
            return 0
    return probability

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

    >>> solve(100, 10, 2, 1)
    0.1
    >>> solve(100, 10, 2, 2)
    0.19090909090909094
    >>> solve(10, 10, 5, 1)
    1.0
    """

    # Make sure that input parameters are within range
    for var, min_, max in [(m,1,1000), (n,1,m), (t,1,100), (p,1,m)]:
      if var < min_ or var > max:
        return False

    min_required_wins = int(math.ceil(float(p) / float(t)))
    if min_required_wins > n:
        return 0.0

    # generate a probability function prob
    prob = gen_prob(p, n, m)

    # make a list containing the least number of people required to
    # win the lottery (in order for the whole group to go) up to the
    # total number of people in the group. The solution to this puzzle
    # is the sum of the results from the prob function using this list
    # as input parameters.
    xs = range(min_required_wins, min(n,p) + 1)

    return sum([prob(x) for x in xs])

if __name__ == '__main__':
    #doctest.testmod()
    for line in sys.stdin:
      m, n, t, p = line.split()
      print "%.10f" % (solve(int(m), int(n), int(t), int(p)))
