def rotate(dir):
    if dir == (-1, 0): return (0,1)
    if dir == (0,1): return (1, 0)
    if dir == (1,0): return (0,-1)
    return (-1,0)

def part1(obstacles, start_pos, bound_x, bound_y):
    x,y = start_pos
    dir = (-1, 0)
    count = 0
    visited = set()
    while (x:=x+dir[0], y:=y+dir[1], 0 <= x <= bound_x and 0 <= y <= bound_y)[2]:
        if (x,y) not in visited:
            count += 1
            visited = visited | {(x,y)}
        while (x+dir[0], y+dir[1]) in obstacles:
            dir = rotate(dir)
    return count-1

def part2(obstacles, start_pos, bound_x, bound_y):
    return sum(
        part2_better_shim(obstacles|{(i,j)}, start_pos, bound_x, bound_y)
        for i in range(bound_x) for j in range(bound_y)
    )

def part2_shim(obstacles, start_pos, bound_x, bound_y):
    x,y = start_pos
    dir = (-1, 0)
    visited = {}
    while (x:=x+dir[0], y:=y+dir[1], 0 <= x <= bound_x and 0 <= y <= bound_y)[2]:
            if (x,y) not in visited:
                visited[(x,y)] = [dir]
            else:
                if dir in visited[(x,y)]:
                    return True
                visited[(x,y)].append(dir)
            while (x+dir[0], y+dir[1]) in obstacles:
                dir = rotate(dir)
    return False

text = open("6.input").read().splitlines()
obstacles = set()
start_pos = (-1,-1)
for i,l in enumerate(text):
    for j, c in enumerate(l):
        if c == "#":
            obstacles = obstacles | {(i,j)}
        elif c == "^":
            start_pos = (i,j)
print(part1(obstacles, start_pos, len(text), len(text[0])))
print(part2(obstacles, start_pos, len(text), len(text[0])))
