left = []
right = []

with open("1/input.txt") as inpt:
    for line in inpt:
        ids = line.split()
        left.append(int(ids[0]))
        right.append(int(ids[1]))

similarity = 0

for i in left:
    multiplyer = 0
    for j in right:
        if i == j:
            multiplyer += 1
    similarity += i * multiplyer

print(similarity)
