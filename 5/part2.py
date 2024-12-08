rules = []
updates = []

with open("5/input.txt") as inpt:
    sections = inpt.read().split("\n\n")
    for line in sections[0].split("\n"):
        rule = []
        for page in line.split("|"):
            rule.append(int(page))
        rules.append(rule)
    for line in sections[1].split("\n"):
        update = []
        for page in line.split(","):
            update.append(int(page))
        updates.append(update)

unordered = []
update: list[int]
for update in updates:
    order = True
    for rule in rules:
        try:
            if update.index(rule[1]) < update.index(rule[0]):
                order = False
        except:
            pass
    if not order:
        unordered.append(update)

for update in unordered:
    while True:
        order = True
        for rule in rules:
            try:
                if update.index(rule[1]) < update.index(rule[0]):
                    order = False
                    update.remove(rule[1])
                    update.insert(update.index(rule[0])+1, rule[1])
            except:
                pass
        if order:
            break

total = 0
for update in unordered:
    total += update[int(len(update)/2)]

print(total)
