grid = []

with open("8/input.txt") as inpt:
    for line in inpt:
        grid.append(list(line.strip()))

width = len(grid[0])
height = len(grid)


class Antenna():
    def __init__(self, x, y, frequency):
        self.x = x
        self.y = y
        self.frequency = frequency

    def antinode(self, antenna):
        return self.x+self.x-antenna.x, self.y+self.y-antenna.y


antennas = []

for y in range(0, height):
    for x in range(0, width):
        if grid[y][x] != ".":
            antennas.append(Antenna(x, y, grid[y][x]))

antinodes = []

for i in range(0, len(antennas)):
    for j in range(0, len(antennas)):
        if j == i or antennas[i].frequency != antennas[j].frequency:
            continue
        antinode = antennas[i].antinode(antennas[j])
        if antinode[0] >= 0 and antinode[0] < width and antinode[1] >= 0 and antinode[1] < height:
            try:
                antinodes.index(antinode)
            except:
                antinodes.append(antinode)

print(len(antinodes))
