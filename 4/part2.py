grid = []

with open("4/input.txt") as inpt:
    for line in inpt:
        grid.append(line.strip())

width = len(grid[0])
height = len(grid)

count = 0
for y in range(0, height):
    for x in range(0, width):
        if grid[y][x] == "A" and x >= 1 and x <= width-2 and y >= 1 and y <= height-2:
            if grid[y-1][x-1] == "M" and grid[y-1][x+1] == "M" and grid[y+1][x+1] == "S" and grid[y+1][x-1] == "S":
                count += 1
            if grid[y-1][x+1] == "M" and grid[y+1][x+1] == "M" and grid[y+1][x-1] == "S" and grid[y-1][x-1] == "S":
                count += 1
            if grid[y+1][x+1] == "M" and grid[y+1][x-1] == "M" and grid[y-1][x-1] == "S" and grid[y-1][x+1] == "S":
                count += 1
            if grid[y+1][x-1] == "M" and grid[y-1][x-1] == "M" and grid[y-1][x+1] == "S" and grid[y+1][x+1] == "S":
                count += 1

print(count)
