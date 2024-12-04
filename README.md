# 2024 Advent of Code
My solutions for 2024's Advent of Code

### Day 1
> Part 1 time = 14:55, Rank 5629

> Part 2 time = 15:55, Rank 4413

>(Probably worse than it needs to be I spent maybe 12ish minutes on a compiled Haskell solution but I am not good enough for it rn)

1.repl.py is just the entirety of my repl for day 1
1.repl.cmd.py was generated by grep ">>>" 1.repl.py >> 1.repl.cmd.py and contains just the code I ran

A better python solution is probably (given that itertools has been unqualified imported and that input is in `text`):
\>\>\> t=list(batched(map(int,text.split()),2))

\>\>\> l,r=[q[0] for q in t],[q[1] for q in t]

\>\>\> sum(abs(a-b) for a,b in zip(sorted(l), sorted(r)))

And for part two we can repeat

\>\>\> sum(a*count(a,r) for a in l)

### Day 2
> Part 1 time = 9:34, Rank 2436

> Part 2 time = 1:17:46, Rank 10155

> Needless to say I'm going to end it. It should have taken 5 minutes to do part 2 after part 1, but I have the brain of a mewling infant

I can't provide REPL logs since they exceeded the bounds of the terminal and were lost

An actually servicable Haskell solution is provided (in 2.good.hs)

It took a while because I made some bad assumptions :)

Additionally I began part 1 with a clone of my bad Python part 1 solution

Both parts were improved (and part 2 was solved in Haskell originally) by performing the checks in
parallel rather than doing them in series

### Day 3
> Part 1 time = 8:23, Rank 3314

> Part 2 time = 20:36, Rank 3745

> Better than yesterday. Part 2 had a natural continuation from part 2 that I knew how to do
> but tested it incorrectly so didn't pursue and wasted ~5 minutes handwriting a specialist parser

Lost the repl logs :( - Provided is a file (3.py) containing a solution that mirrored my REPL solution
There is also a horrid cursed solution, plus an attempted golf of that solution that  I got distracted from

### Day 4
> Part 1 time = 49:44, Rank 9280

> Part 2 time =  1:51:05, Rank 12415

> :( Needless to say I'm not happy with this. Part one is whatever I got it easily when I switched to Haskell
> Part 2 is a repeat of day 2
