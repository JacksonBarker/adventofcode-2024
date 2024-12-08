grid = []

with open("4/input.txt") as inpt:
    for line in inpt:
        grid.append(line.strip())

width = len(grid[0])
height = len(grid)

count = 0
for y in range(0, height):
    for x in range(0, width):
        if x <= width-4 and grid[y][x] == "X" and grid[y][x+1] == "M" and grid[y][x+2] == "A" and grid[y][x+3] == "S":
            count += 1
        if x >= 3 and grid[y][x] == "X" and grid[y][x-1] == "M" and grid[y][x-2] == "A" and grid[y][x-3] == "S":
            count += 1
        if y <= height-4 and grid[y][x] == "X" and grid[y+1][x] == "M" and grid[y+2][x] == "A" and grid[y+3][x] == "S":
            count += 1
        if y >= 3 and grid[y][x] == "X" and grid[y-1][x] == "M" and grid[y-2][x] == "A" and grid[y-3][x] == "S":
            count += 1
        if x <= width-4 and y <= height-4 and grid[y][x] == "X" and grid[y+1][x+1] == "M" and grid[y+2][x+2] == "A" and grid[y+3][x+3] == "S":
            count += 1
        if x >= 3 and y >= 3 and grid[y][x] == "X" and grid[y-1][x-1] == "M" and grid[y-2][x-2] == "A" and grid[y-3][x-3] == "S":
            count += 1
        if x <= width-4 and y >= 3 and grid[y][x] == "X" and grid[y-1][x+1] == "M" and grid[y-2][x+2] == "A" and grid[y-3][x+3] == "S":
            count += 1
        if x >= 3 and y <= height-4 and grid[y][x] == "X" and grid[y+1][x-1] == "M" and grid[y+2][x-2] == "A" and grid[y+3][x-3] == "S":
            count += 1

print(count)
