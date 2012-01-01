This repository is mainly to hold some christmas vacation python hacking on the Spotify puzzle: Ticket Lottery.

Nothing to see here... Move along.

At the time of writing this puzzle can be found at [Spotify's jobs page](http://www.spotify.com/se/jobs/tech/ticket-lottery/)

Ticket Lottery
--------------

You and your friends are in New York and are planning to go see a Broadway musical. Unfortunately, New York being New York, the tickets are just a tiny bit expensive. But one of the shows has a ticket lottery each night where impecunious people such as you have a chance to win the right to buy slightly less expensive tickets to good seats. The lottery operates as follows. First, everyone interested enters the lottery. Then, n lucky winners are drawn, and each of these is offered to buy up to t tickets.
Given the number of people p in your group (all of which entered the lottery) and the total number of people m that entered the lottery, what is the probability that you will be able to get tickets for your entire group? Assume that the n lucky winners are chosen uniformly at random from the m people that entered the lottery, and that each person can win at most once.

*Input*

The input consists of a single line containing four integers:

- 1 ≤ m ≤ 1000: the total number of people who entered the lottery.
- 1 ≤ n ≤ m: the total number of winners drawn.
- 1 ≤ t ≤ 100: the number of tickets each winner is allowed to buy.
- 1 ≤ p ≤ m: the number of people in your group.

*Output*

Output a single line containing the probability that your entire group can get tickets to the show. This probability should be given with an absolute error of at most 10^−9.

    Sample input 1     Sample output 1
    100 10 2 1         0.1
    
    Sample input 2     Sample output 2
    100 10 2 2         0.1909090909
    
    Sample input 3     Sample output 3
    10 10 5 1          1.0000000000

Result
------

    > python2.6 s1.py
    100 10 2 2^D
    0.1909090909

Spotify Judge
-------------

Hmmm, the judge says `Run Time Error` and that my program exited with status 1. I *do* return `False` if the input parameters are out of bounds but could that really be the problem? This might take some meditating to get right.