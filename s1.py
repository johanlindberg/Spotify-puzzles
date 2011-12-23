## Spotify Software Puzzles - Best Before
##
## Given a possibly ambiguous date "A/B/C", where A,B,C are integers between
## 0 and 2999, output the earliest possible legal date between Jan 1, 2000
## and Dec 31, 2999 (inclusive) using them as day, month and year (but not
## necessarily in that order).

import datetime
import doctest
import itertools
import sys

EARLIEST = datetime.date(2000, 01, 01)
LATEST = datetime.date(2999, 12, 31)

def solve(s):
  """
  >>> solve("02/4/67")
  2067-02-04
  >>> solve("12/11/10")
  2010-11-12
  >>> solve("31/5/2012")
  2012-05-31
  >>> solve("31/9/73")
  31/9/73 is illegal
  >>> solve("1999/01/01")
  1999/01/01 is illegal
  """
  d = None
  for p in itertools.permutations(s.split("/"), 3):
    try:
      # Years may be truncated to two digits and may
      # in that case also omit the leading 0 (if there
      # is one), so 2000 could be given as "2000", "00"
      # or "0" (but not as an empty string).
      if len(p[0]) < 4:
        p = (str(2000 + int(p[0])), p[1], p[2])

      # generate a date based on this tuple. If it's
      # earlier than d we keep it.
      _d = datetime.date(*[int(x) for x in p])
      if d is None or _d < d:
        d = _d

    except ValueError:
      pass

  # If we can't create a date from any of the tuples
  # d will still be None and we should let the user
  # know that the input was invalid.
  # Also, if the date falls outside the span of
  # 2000-01-01 and 2099-12-31 we need to output that
  # it's illegal.
  if d is None or \
     d < EARLIEST or \
     d > LATEST:
    print s, "is illegal"
  else:
    print d

if __name__ == '__main__':
  doctest.testmod()
  for i in sys.argv[1:]:
    solve(i)
