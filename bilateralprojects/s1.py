## Spotify Software Puzzles - Bilateral projects
##
## Given a list of two-person teams, compute the smallest number of people
## to get at least one person from each project, as well as a list of those
## people. If possible (subject to the set of people being smallest possible),
## the list of invitees should include your friend.

import doctest
import sys

def make_index(teams):
    """
    make_index creates a dict indexing all employees and projects.

    >>> index, _ = make_index([(1009, 2011), (1017, 2011)])
    >>> len(index)
    3
    >>> print index[2011]
    [0, 1]
    >>> print index[1009]
    [0]
    >>> print index[1017]
    [1]
    """

    index, projects = {}, {}
    project_id = 0
    for id1, id2 in teams:
        for id in [id1, id2]:
            try:
                index[id].append(project_id)
            except KeyError:
                index[id] = [project_id]

            try:
                projects[project_id].append(id)
            except KeyError:
                projects[project_id] = [id]
        project_id += 1

    return index, projects

def prune_index(index, projects, n):
    """
    prune_index deletes all duplicates in the index dict.

    >>> index = { 2011: [0,1], 1009: [0], 1017: [1] }
    >>> projects = { 0: [1009,2011], 1: [1017,2011] }
    >>> index = prune_index(index, projects, 2)
    >>> len(index)
    1
    >>> print index[2011]
    [0, 1]
    """

    projs = range(n)
    result = {}

    ids = sorted(index.keys(), key = lambda k: len(index[k]), reverse = True)
    while len(ids) > 0:
        id = ids.pop(0)
        for p in index[id]:
            if p in projs:
                projs.remove(p)               # remove from list of projects

                for _id in projects[p]:       # remove any other references
                    if _id != id:
                        index[_id].remove(p)
                        if len(index[_id]) == 0:
                            del index[_id]
                            ids.remove(_id)

                if id not in result.keys():
                    result[id] = index[id]

        # re-sort based on pruning
        ids = sorted(ids, key = lambda k: len(index[k]), reverse = True)

    return result

def solve(teams):
    """
    >>> solve([(1009, 2011), (1017, 2011)])
    [2011]
    >>> s = solve([(1009, 2011), (1017, 2011), (1009, 2012), (1017, 2012)])
    >>> s in [[1009, 1017], [2011, 2012]]
    True
    """

    index, projects = make_index(teams)
    index = prune_index(index, projects, len(teams))

    return sorted(index.keys())

def format(people):
    print len(people)
    for p in people:
        print p

if __name__ == '__main__':
    doctest.testmod()
    n, teams = 0, []
    for line in sys.stdin:
        try:
            e1, e2 = line.strip().split()
            teams.append([int(e1), int(e2)])
        except ValueError:
            n = int(line.strip())

    if n == len(teams):
        format(solve(teams))
