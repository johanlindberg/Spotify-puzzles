## Spotify Software Puzzles - Best Before
##
## Given a list of two-person teams, compute the smallest number of people
## to get at least one person from each project, as well as a list of those
## people. If possible (subject to the set of people being smallest possible),
## the list of invitees should include your friend.

import doctest

def make_index(teams):
    """
    make_index creates a dict indexing all employees and projects.

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
    project_id = 0
    for id1, id2 in teams:
        for id in [id1, id2]:
            try:
                result[id].append(project_id)
            except KeyError:
                result[id] = [project_id]
        project_id += 1
    return result

def prune_index(index, n):
    """
    prune_index deletes all duplicates in the index dict.

    >>> index = { 2011: [0,1], 1009: [0], 1017: [1] }
    >>> index = prune_index(index, 2)
    >>> len(index)
    1
    >>> print index[2011]
    [0, 1]
    """

    projects = range(n)
    result = {}

    # sort index based on number of projects
    for id in sorted(index.keys(), key = lambda k: len(index[k]), reverse = True):
        for p in index[id]:
            if p in projects:
                projects.remove(p)
                result[id] = index[id]

    return result

def solve(teams):
    """
    >>> solve([(1009, 2011), (1017, 2011)])
    [2011]
    """
    index = prune_index(make_index(teams), len(teams))
    return index.keys()

if __name__ == '__main__':
    doctest.testmod()
