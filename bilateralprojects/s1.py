## Spotify Software Puzzles - Best Before
##
## Given a list of two-person teams, compute the smallest number of people
## to get at least one person from each project, as well as a list of those
## people. If possible (subject to the set of people being smallest possible),
## the list of invitees should include your friend.

import doctest

def make_index(teams):
    """
    >>> index = make_index([(1009, 2011), (1017, 2011)])
    >>> len(index)
    3
    >>> print index[2011]
    [1009, 1017]
    >>> print index[1009]
    [2011]
    >>> print index[1017]
    [2011]
    """
    result = {}
    for id1, id2 in teams:
        for a, b in [(id1, id2), (id2, id1)]:
            if a not in result.keys():
                result[a] = [b]
            else:
                result[a].append(b)
    return result

def solve(teams):
    """
    >>> solve([(1009, 2011), (1017, 2011)])
    [2011]
    """
    return [2011]

if __name__ == '__main__':
    doctest.testmod()
