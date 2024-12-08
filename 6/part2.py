GRID = []

with open("6/input.txt") as inpt:
    for line in inpt:
        GRID.append(list(line.strip()))

width = len(GRID[0])
height = len(GRID)


class Guard():
    def __init__(self, x: int, y: int, direction: chr):
        self.x = x
        self.y = y
        self.direction = direction

    def rotate(self):
        if self.direction == '^':
            self.direction = '>'
        elif self.direction == '>':
            self.direction = 'v'
        elif self.direction == 'v':
            self.direction = '<'
        else:
            self.direction = '^'


for row in GRID:
    if '^' in row:
        start = [row.index('^'), GRID.index(row), '^']
        break
    elif 'v' in row:
        start = [row.index('v'), GRID.index(row), 'v']
        break
    elif '<' in row:
        start = [row.index('<'), GRID.index(row), '<']
        break
    elif '>' in row:
        start = [row.index('>'), GRID.index(row), '>']
        break

GRID[start[1]][start[0]] = '.'

count = 0
for y in range(0, height):
    for x in range(0, width):
        if GRID[y][x] == '#' or y == start[1] and x == start[0]:
            continue

        grid = []
        for i in range(0, height):
            grid.append(GRID[i].copy())
        guard = Guard(start[0], start[1], start[2])

        grid[y][x] = '#'

        stuck = False
        while True:
            if guard.direction in grid[guard.y][guard.x]:
                stuck = True
                break
            if guard.direction == '^':
                if guard.y == 0:
                    grid[guard.y][guard.x] += guard.direction
                    break
                if grid[guard.y-1][guard.x] == '#':
                    grid[guard.y][guard.x] += guard.direction
                    guard.rotate()
                else:
                    grid[guard.y][guard.x] += guard.direction
                    guard.y = guard.y-1
            elif guard.direction == 'v':
                if guard.y == height-1:
                    grid[guard.y][guard.x] += guard.direction
                    break
                if grid[guard.y+1][guard.x] == '#':
                    grid[guard.y][guard.x] += guard.direction
                    guard.rotate()
                else:
                    grid[guard.y][guard.x] += guard.direction
                    guard.y = guard.y+1
            elif guard.direction == '<':
                if guard.x == 0:
                    grid[guard.y][guard.x] += guard.direction
                    break
                if grid[guard.y][guard.x-1] == '#':
                    grid[guard.y][guard.x] += guard.direction
                    guard.rotate()
                else:
                    grid[guard.y][guard.x] += guard.direction
                    guard.x = guard.x-1
            elif guard.direction == '>':
                if guard.x == width-1:
                    grid[guard.y][guard.x] += guard.direction
                    break
                if grid[guard.y][guard.x+1] == '#':
                    grid[guard.y][guard.x] += guard.direction
                    guard.rotate()
                else:
                    grid[guard.y][guard.x] += guard.direction
                    guard.x = guard.x+1
        if stuck:
            count += 1

print(count)
