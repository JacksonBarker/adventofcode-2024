left = []
right = []

with open("1/input.txt") as inpt:
    for line in inpt:
        ids = line.split()
        left.append(int(ids[0]))
        right.append(int(ids[1]))

left.sort()
right.sort()
distances = []

for i in range(0, len(left)):
    distances.append(abs(left[i] - right[i]))

print(sum(distances))
