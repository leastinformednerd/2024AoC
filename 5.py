def part1(rules, updates):
    count = 0;
    for update in updates:
        illegal=set()
        for elem in update:
            if elem in illegal:
                break
            illegal=illegal | rules.get(elem, set())
        else:
            count+=int(update[int(len(update)/2)])
    return count

def part2(rules, updates):
    count = 0;
    for update in updates:
        illegal=set()
        built = []
        invalid=False
        for elem in update:
            if elem in illegal:
                invalid=True
                for index, item in enumerate(built):
                    if elem in rules[item]:
                        built.insert(index, elem)
                        break
            else:
                built.append(elem)
            illegal=illegal|rules.get(elem,set())           
        if invalid:
           count+=int(built[int(len(built)/2)])
    return count
  
with open("5.input") as f:
    rules_, updates_ = (_.splitlines() for _ in f.read().split("\n\n"))
    rules = {}
    for first, second in (_.split("|") for _ in rules_):
        if second not in rules:
            rules[second] = set()
        rules[second] = rules[second] | {first}
    updates = [_.split(",") for _ in updates_]
    print(part1(rules,updates))
    print(part2(rules,updates))
