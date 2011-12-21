## Spotify Software Puzzles - Best Before
##
## Given a possibly ambiguous date "A/B/C", where A,B,C are integers between
## 0 and 2999, output the earliest possible legal date between Jan 1, 2000
## and Dec 31, 2999 (inclusive) using them as day, month and year (but not
## necessarily in that order).

import doctest

def solve(s):
  """
  >>> solve("02/4/67")
  2067-04-02
  """

if __name__ == '__main__':
  doctest.testmod()
