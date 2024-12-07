from operator import *

def part1(equations):
    count = 0
    for total, individual in equations:
        count+=int(total)*part1_inner(total, individual[1:], individual[0])
            
    return count

def part1_inner(total, individuals, current):
    for op in [add, mul]:
        new = op(current,individuals[0])
        if len(individuals) == 1:
            if new  == int(total):
                return True
        elif part1_inner(total, individuals[1:], new):
            return True
    return False

 
def part2(equations):
    count = 0
    for total, individual in equations:
        count+=int(total)*part2_inner(total, individual[1:], individual[0])
            
    return count

def part2_inner(total, individuals, current):
    for op in [add, mul, lambda a,b: int(f"{a}{b}")]:
        new = op(current,individuals[0])
        if len(individuals) == 1:
            if new  == total:
                return True
        else:
            if total == 7290:
                print(individuals[1:], current, op, new)
            if part2_inner(total, individuals[1:], new):
                return True
    return False

cases = [(int(b[0]),[int(_) for _ in b[1].split()]) for b in (a.split(":") for a in open("7.input").read().splitlines())]
print(part1(cases))
print(part2(cases))
