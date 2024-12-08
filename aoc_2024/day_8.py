antennas = {}
map = []
with open('data/day_8_data.txt') as f:
    for i, line in enumerate(f):
        map.append([])
        for j, c in enumerate(line.strip()):
            map[-1].append(c)
            if c != '.':
                antennas.setdefault(c, []).append((i,j))

R = len(map)
C = len(map[0])

def get_antinodes_1(x1, y1, x2, y2):
    antinodes = []
    if within_bounds(2*x1-x2, 2*y1-y2):
        antinodes.append((2*x1-x2, 2*y1-y2))
    if within_bounds(2*x2-x1, 2*y2-y1):
        antinodes.append((2*x2-x1, 2*y2-y1))

    return antinodes

def get_antinodes_2(x1, y1, x2, y2):
    a = x1 - x2
    b = y1 - y2

    antinodes = []
    x = x1
    y = y1
    while True:
        x -= a
        y -= b

        if not within_bounds(x, y):
            break
        
        antinodes.append((x, y))
        

    while True:
        x += a
        y += b

        if not within_bounds(x, y):
            break
        
        antinodes.append((x, y))

    return antinodes

def within_bounds(x, y):
    return (0 <= x < R and 0 <= y < C)

ans1 = set()
ans2 = set()
for k, v in antennas.items():
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            antinodes = get_antinodes_1(*v[i], *v[j])
            for antinode in antinodes:
                ans1.add(antinode)

            antinodes = get_antinodes_2(*v[i], *v[j])
            for antinode in antinodes:
                ans2.add(antinode)

print(len(ans1))
print(len(ans1.union(ans2)))