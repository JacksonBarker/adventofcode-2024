grid = []

with open("6/input.txt") as inpt:
    for line in inpt:
        grid.append(list(line.strip()))

width = len(grid[0])
height = len(grid)


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


for row in grid:
    if '^' in row:
        guard = Guard(row.index('^'), grid.index(row), '^')
        break
    elif 'v' in row:
        guard = Guard(row.index('v'), grid.index(row), 'v')
        break
    elif '<' in row:
        guard = Guard(row.index('<'), grid.index(row), '<')
        break
    elif '>' in row:
        guard = Guard(row.index('>'), grid.index(row), '>')
        break

while True:
    if guard.direction == '^':
        if guard.y == 0:
            grid[guard.y][guard.x] = 'X'
            break
        if grid[guard.y-1][guard.x] == '#':
            guard.rotate()
        else:
            grid[guard.y][guard.x] = 'X'
            guard.y = guard.y-1
    elif guard.direction == 'v':
        if guard.y == height-1:
            grid[guard.y][guard.x] = 'X'
            break
        if grid[guard.y+1][guard.x] == '#':
            guard.rotate()
        else:
            grid[guard.y][guard.x] = 'X'
            guard.y = guard.y+1
    elif guard.direction == '<':
        if guard.x == 0:
            grid[guard.y][guard.x] = 'X'
            break
        if grid[guard.y][guard.x-1] == '#':
            guard.rotate()
        else:
            grid[guard.y][guard.x] = 'X'
            guard.x = guard.x-1
    elif guard.direction == '>':
        if guard.x == width-1:
            grid[guard.y][guard.x] = 'X'
            break
        if grid[guard.y][guard.x+1] == '#':
            guard.rotate()
        else:
            grid[guard.y][guard.x] = 'X'
            guard.x = guard.x+1

count = 0
for y in range(0, height):
    for x in range(0, width):
        if grid[y][x] == 'X':
            count += 1
print(count)
