ROWS = 71
COLS = 71
MOVES = [(1,0), (-1,0), (0,1), (0,-1)]

def findShortestPath(map):
    start = (0, 0)
    exit = (ROWS-1, COLS-1)
    visited = set()
    q = [(start, 0)] # position, cost
    visited.add(start) # mark as visited

    while len(q):
        current, cost = q.pop(0) # get next tile

        # found exit
        if current == exit:
            return cost

        # add neighbors to queue
        for move in MOVES:
            next = (current[0]+move[0], current[1]+move[1])
            if 0 <= next[0] < ROWS and 0 <= next[1] < COLS:
                if map[next[0]][next[1]] != '#' and next not in visited:
                    visited.add(next)
                    q.append((next, cost+1))

    return -1

def findBlockingByte(map, bytes):
    # binary search
    low = 0
    high = len(bytes)-1
    lowestBlocking = -1

    while low <= high:
        map = [['.' for _ in range(COLS)] for _ in range(ROWS)]
        mid = (high-low)//2 + low

        for byte in bytes[:mid]:
            map[byte[0]][byte[1]] = '#'

        cost = findShortestPath(map)

        if cost == -1:
            lowestBlocking = mid
            high = mid-1
        else:
            low = mid+1

    return lowestBlocking

map = [['.' for _ in range(COLS)] for _ in range(ROWS)]
bytes = []
with open('data/day_18_data.txt') as f:
    for line in f:
        x, y = line.strip().split(',')
        bytes.append((int(x), int(y)))

# part 1
for i in range(1024):
    map[bytes[i][0]][bytes[i][1]] = '#'
print(findShortestPath(map))

# part 2
print(bytes[findBlockingByte(map, bytes)-1])

