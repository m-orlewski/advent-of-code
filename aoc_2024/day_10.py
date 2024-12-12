tiles = []
trailheads = []
 
def getNodesToVisit(x, y):
    nextNodeVal = tiles[x][y] + 1
    nodesToVisit = []
    if x-1 >= 0 and tiles[x-1][y] == nextNodeVal:
        nodesToVisit.append((x-1, y)) # left
    if x+1 < len(tiles) and tiles[x+1][y] == nextNodeVal:
        nodesToVisit.append((x+1, y)) # right
    if y-1 >= 0 and tiles[x][y-1] == nextNodeVal:
        nodesToVisit.append((x, y-1)) # up
    if y+1 < len(tiles[x]) and tiles[x][y+1] == nextNodeVal:
        nodesToVisit.append((x, y+1)) # down
 
    return nodesToVisit
 
def dfs(x, y, found):
    if tiles[x][y] == 9:
        found.append((x, y))
        return
 
    nodesToVisit = getNodesToVisit(x, y)
    for node in nodesToVisit:
        dfs(*node,found)
 
def count_trails(x, y, found):
    dfs(x, y, found)
    return len(set(found)), len(found)
 
if __name__ == '__main__':
    with open('data.txt') as f:
        for i, line in enumerate(f):
            tiles.append([])
            for j, c in enumerate(line.strip()):
                tiles[-1].append(int(c))
                if c == '0':
                    trailheads.append((i, j))
 
    ans1 = 0
    ans2 = 0
    for trailhead in trailheads:
        found = []
        found_unique, found_total = count_trails(*trailhead, found)
        ans1 += found_unique
        ans2 += found_total
    print(ans1)
    print(ans2)