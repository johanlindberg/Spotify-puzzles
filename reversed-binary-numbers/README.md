This repository is mainly to hold some summer vacation python hacking
on a Spotify puzzle.

Nothing to see here... Move along.

At the time of writing this puzzle can be found at [Spotify's jobs page](http://www.spotify.com/se/jobs/tech/reversed-binary/)

Reversed Binary Numbers
-----------------------

Yi has moved to Sweden and now goes to school here. The first years of schooling she got in China, and the curricula do not match completely in the two countries. Yi likes mathematics, but now... The teacher explains the algorithm for subtraction on the board, and Yi is bored. Maybe it is possible to perform the same calculations on the numbers corresponding to the reversed binary representations of the numbers on the board? Yi dreams away and starts constructing a program that reverses the binary representation, in her mind. As soon as the lecture ends, she will go home and write it on her computer.

*Task*

Your task will be to write a program for reversing numbers in binary. For instance, the binary representation of 13 is 1101, and reversing it gives 1011, which corresponds to number 11.

*Input*

The input contains a single line with an integer N, 1 ≤ N ≤ 1000000000.

*Output*

Output one line with one integer, the number we get by reversing the binary representation of N.

    Sample input 1     Sample output 1
    13                 11
    
    Sample input 2     Sample output 2
    47                 61

Results
-------

    > python2.6 s1.py
    13^D
    11

Spotify Judge
-------------

My first attempt at a solution, that I sent in to be judged, passed a `str`to the solve function which raised a `TypeError` but once I corrected that I got this reply.

    From: Honorable Judge Kattis <puzzle@spotify.se>
    To: johan.h.lindberg@gmail.com
    Subject: Result for "reversebinary": Accepted
    Date: Thu, 13 Jun 2013 12:55:18 +0200 (CEST)

    Hello Johan Lindberg,

    Thank you for submitting a solution to our problem "reversebinary"!

    We have tested your solution, and we are happy to report that it
    solved the problem!  We hope you had as fun with it as we did.

    Yours truly,
    Spotify
