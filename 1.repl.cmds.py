>>> """62619   25903
>>> _.splitlines()
>>> [a.split() for a in _]
>>> """62619   25903
>>> left, right = [a.split()[0] for a in _], [a.split(1)[0] for a in _]
>>> left, right = [a.split()[0] for a in _], [a.split()[1] for a in _]
>>> x="""62619   25903
>>> 97595   45435
>>> [a.split() for a in x.splitlines()]
>>> left,right = [a.split()[0] for a in x.splitlines()], [a.split()[1] for a in x.splitlines()]
>>> left
>>> clear
>>> left = sorted(left)
>>> right = sorted(right)
>>> [abs(a-b) for a,b in zip(left,right)]
>>> left = sorted([int(a) for a in left])
>>> right = sorted([int(a) for a in right])
>>> sum(abs(a-b) for a,b in zip(left,right))
>>> sum(a*right.count(a) for a in left)
