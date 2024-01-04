# [Advent of Code 2023](https://adventofcode.com/2023)
This is a repository of personal notes and solutions to this coding tournament / challenge.

For a first participation, I was not at all in the competitive mindset, but aimed at being a "finisher" of the 50 puzzles (I'm still working on it, starting day 20 soon, then I'll go back to the ones I left behind).

## Building my own toolkit
I saw that a library to ease the processing of input data and automate entry submission could be useful.
For example, the first player in the leaderboard used one for Kotlin.

So I started my own in the [aoc_lib.py](https://github.com/HubTou/AoC-2023/blob/main/src/aoc_lib.py) file, with a blank template to use it in the [TEMPLATE.py](https://github.com/HubTou/AoC-2023/blob/main/src/TEMPLATE.py) file.

I'll publish my solutions for days 1 - 9, 11 - 13 once they're retrofitted to this new toolkit and template...

## Why not publishing puzzle texts and user inputs?
As mentioned on [Advent of Code website](https://adventofcode.com/2023/about): 
> Can I copy/redistribute part of Advent of Code? Please don't. Advent of Code is free to use, not free to copy.
> If you're posting a code repository somewhere, please don't include parts of Advent of Code like the puzzle text or your inputs.

## Competitive programming and leaderboard
The competition is now over. The [top players](https://adventofcode.com/2023/leaderboard) were all incredible!

Check the time it took them to get the first and both stars:

day|\*\*/1st|\*\*/100th|\*/1st|\*/100th|Comments and hints
---|---|---|---|---|---
25|00:02:53|00:14:01|00:02:43|00:13:07|TODO...
24|00:12:42|01:02:10|00:04:17|00:15:56|TODO...
23|00:07:09|00:38:20|00:02:08|00:09:02|TODO...
22|00:12:50|00:29:48|00:10:04|00:21:00|TODO...
21|00:14:35|01:19:03|00:01:24|00:04:44|TODO...
20|00:15:52|00:48:46|00:10:26|00:23:11|TODO...
19|00:12:56|00:29:12|00:02:01|00:10:23|OK. Very pleasant one. Using some regular expressions and recursivity. I provided a [file](https://github.com/HubTou/AoC-2023/blob/main/src/19-p2-probabilities.png) explaining how the probabilities are computed as an hint.
18|00:05:31|00:20:55|00:02:35|00:08:21|HALF WAY. The first part was quite fun and I found a flood filling algorithm that could also be useful in the future. However it appears I'll have to rewrite my code completely to tackle part 2!
17|00:05:03|00:20:00|00:02:25|00:14:05|TODO. Skipping that one until I can review [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). Then I'll need to adapt it
16|00:04:33|00:15:30|00:02:03|00:11:36|OK. That one was also easy, though I needed to take care of never ending beams in first part that blown up the Python recursion limit!
15|00:01:26|00:11:04|00:00:51|00:02:10|OK. That one was surprisingly easy :-)
14|00:05:46|00:17:15|00:01:28|00:04:10|OK. With 1 billion cycles, the second part cannot be brute forced, but after a while a cycle appears that avoids computing all of it
13|00:06:06|00:13:46|00:03:51|00:08:58|The specification for this one doesn't cover all the cases that can be encountered
12|00:05:58|00:05:58|00:02:02|00:08:12|HALF WAY. I need to work on an optimized algorithm for the second part
11|00:03:37|00:09:18|00:02:00|00:06:07|OK
10|00:10:04|00:36:31|00:01:05|00:11:33|OK. I was stuck for a long time (about 3 weeks!) on the second part until I realised that FJ or L7 count as a single wall. I provided a [file](https://github.com/HubTou/AoC-2023/blob/main/src/10-p2-example-data-3-results.txt) explaining why with better looking characters. I really needed to experience algorithmic warmup :-) 
9|00:01:48|00:05:36|00:01:16|00:04:02|OK
8|00:04:24|00:10:16|00:00:38|00:03:30|HALF WAY. I need to work on an optimized algorithm for the second part
7|00:08:45|00:16:00|00:04:52|00:09:57|HALF WAY. The second part works with the example data, but not the validation data. I need to cross check my results with the solution of someone else to find my mistake(s)
6|00:02:05|00:05:02|00:01:15|00:03:11|OK
5|00:08:38|00:26:37|00:01:35|00:08:15|OK. I got the result for the second part but it took a day to compute, with multiprocessing on a multi-cores machine. There must be a better way to do it! 
4|00:01:22|00:07:08|00:00:43|00:02:51|OK
3|00:05:09|00:11:37|00:03:11|00:07:09|OK
2|00:01:34|00:06:15|00:00:37|00:04:10|OK
1|00:02:24|00:07:03|00:00:12|00:01:39|OK. Looking at the best competitor: 12 seconds to read the spec, code and submit the result for the first star, how can this even be possible?!

## Interesting notes and solutions elsewhere
Half of the top 100 leaders have a GitHub account, and one third of them have published their AoC 2023 code.

Among them, I noticed [Jonathan Paulson (#5) Python solutions](https://github.com/jonathanpaulson/AdventOfCode/tree/master/2023), and [mrphlip (#27) commented Python solutions](https://github.com/mrphlip/aoc/tree/master/2023). 

There are some other interesting resources on GitHub, such as a [collection of awesome resources related to the yearly Advent of Code challenge](https://github.com/Bogdanp/awesome-advent-of-code), or on the Web, such as an article about [Solving Your Puzzles With Python](https://realpython.com/python-advent-of-code/).
