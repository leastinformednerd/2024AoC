import re

def mul(a,b):
    return a*b

text = open("3.input").read()

def part1(text):
    return sum(eval(_[0]) for _ in re.finditer(r"mul\([0-9]+,[0-9]+\)", text))

def part2(text):
    do = True
    return sum(
        (do:=False,0)[1] if e[0] == "don't()" else
            ((do:=True,0)[1] if e[0] == "do()" else eval(e[0]) if do else 0)
        for e
        in list(re.finditer(r"(mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\))", text))
    )
    
print(part1(text))
print(part2(text))
