import re
text = open("3.input").read()
def part1(text):
    t = re.finditer(r"mul\([0-9]+,[0-9]+\)", text)
    return sum(int(a[4:])*int(b[:-1]) for a,b in (_[0].split(",") for _ in t))

def part2(text):
    t = list(re.finditer(r"(mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\))", text))
    acc = 0
    do = True
    for m in t:
        if m[0] == "don't()":
            do = False
        elif m[0] == "do()":
            do = True
        elif do:
            a,b = m[0].split(",")
            acc += int(a[4:])*int(b[:-1])
    return acc

print(part1(text))
print(part2(text))
