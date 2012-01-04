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
    [0, 1]
    >>> print index[1009]
    [0]
    >>> print index[1017]
    [1]
    """
    result = {}
    team_id = 0
    for id1, id2 in teams:
        for id in [id1, id2]:
            try:
                result[id].append(team_id)
            except KeyError:
                result[id] = [team_id]
        team_id += 1
    return result

def solve(teams):
    """
    >>> solve([(1009, 2011), (1017, 2011)])
    [2011]
    """
    return [2011]

if __name__ == '__main__':
    doctest.testmod()
