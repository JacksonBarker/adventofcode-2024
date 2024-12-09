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

    def antinode(self, antenna, harmonic=1):
        return self.x+(self.x-antenna.x)*harmonic, self.y+(self.y-antenna.y)*harmonic


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
        harmonic = 0
        while True:
            antinode = antennas[i].antinode(antennas[j], harmonic)
            harmonic += 1
            if antinode[0] >= 0 and antinode[0] < width and antinode[1] >= 0 and antinode[1] < height:
                try:
                    antinodes.index(antinode)
                except:
                    antinodes.append(antinode)
            else:
                break

print(len(antinodes))
