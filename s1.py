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
  2067-02-04
  """
  parts = s.split("/")
  d = None
  for p in itertools.permutations(parts, 3):
    try:
      # Years may be truncated to two digits and may
      # in that case also omit the leading 0 (if there
      # is one), so 2000 could be given as "2000", "00"
      # or "0" (but not as an empty string).
      if len(p[0]) < 4:
        p = (str(2000 + int(p[0])), p[1], p[2])
      _d = datetime.date(*[int(x) for x in p])
      if d is None or _d < d: d = _d
    except ValueError:
      pass

  print d


if __name__ == '__main__':
  doctest.testmod()
