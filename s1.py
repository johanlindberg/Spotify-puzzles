## Spotify Software Puzzles - Best Before
##
## Given a possibly ambiguous date "A/B/C", where A,B,C are integers between
## 0 and 2999, output the earliest possible legal date between Jan 1, 2000
## and Dec 31, 2999 (inclusive) using them as day, month and year (but not
## necessarily in that order).

import datetime
import doctest
import itertools

def solve(s):
  """
  >>> solve("02/4/67")
  ('02', '4', '67')
  ('02', '67', '4')
  ('4', '02', '67')
  ('4', '67', '02')
  ('67', '02', '4')
  ('67', '4', '02')
  """
  parts = s.split("/")
  for p in itertools.permutations(parts, 3):
    print p


if __name__ == '__main__':
  doctest.testmod()
