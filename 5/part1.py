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

ordered = []
update: list[int]
for update in updates:
    order = True
    for rule in rules:
        try:
            if update.index(rule[1]) < update.index(rule[0]):
                order = False
        except:
            pass
    if order:
        ordered.append(update[int(len(update)/2)])

print(sum(ordered))
