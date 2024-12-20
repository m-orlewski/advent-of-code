from collections import deque

map = []
ROWS = -1
ROWS = -1

def get_next_nodes(node):
    nextNodes = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x = node[0] + dx
        y = node[1] + dy

        if 0 <= x < ROWS and 0 <= y < COLS and map[x][y] != '#':
            nextNodes.append((x, y))

    return nextNodes

def bfs(start):
    q = deque()
    q.append(start)
    costs = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
    costs[start[0]][start[1]] = 0

    while len(q):
        node = q.pop()

        nextNodes = get_next_nodes(node)
        for nextNode in nextNodes:
            if costs[nextNode[0]][nextNode[1]] == -1: # not visited
                costs[nextNode[0]][nextNode[1]] = costs[node[0]][node[1]] + 1
                q.append(nextNode)

    return costs

def find_best_cheats(costs, cheatTime):
    count = 0
    for i in range(len(costs)):
        for j in range(len(costs[i])):
            if costs[i][j] == -1:
                continue
            
            for dx in range(-cheatTime, cheatTime+1):
                r = cheatTime - abs(dx)
                for dy in range(-r, r+1):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < ROWS and 0 <= y < COLS and costs[x][y] != -1:
                        timeSaved = costs[x][y] - costs[i][j] - (abs(dx) + abs(dy))
                        if timeSaved >= 100:
                            count += 1

    return count

if __name__ == '__main__':
    map = []
    with open('data/day_20_data.txt') as f:
        for i, line in enumerate(f):
            map.append([])
            for j, c in enumerate(line.strip()):
                if c == 'S':
                    start = (i, j)
                
                map[-1].append(c if c not in 'SE' else '.')

    ROWS = len(map)
    COLS = len(map[0])

    costs = bfs(start)
    ans1 = find_best_cheats(costs, 2)
    print(ans1)

    ans2 = find_best_cheats(costs, 20)
    print(ans2)