solutions = []
terms = []

with open("7/input.txt") as inpt:
    for line in inpt:
        solutions.append(int(line.split(": ")[0]))
        terms.append([int(i) for i in line.split(": ")[1].split()])

tree = []
for i in range(0, len(terms)):
    tree.append([terms[i][0]])
    for j in range(1, len(terms[i])):
        branches = []
        for branch in tree[i]:
            branches.append(branch + terms[i][j])
            branches.append(branch * terms[i][j])
            branches.append(int(str(branch) + str(terms[i][j])))
        tree[i] = branches.copy()

total = 0
for i in range(0, len(tree)):
    for j in range(0, len(tree[i])):
        if tree[i][j] == solutions[i]:
            total += solutions[i]
            break

print(total)
