from queue import PriorityQueue

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
         
def solve(maze, start_point, end_point):
    priority_queue = PriorityQueue()
    priority_queue.put((0, start_point, 1, [start_point])) # (cost, position, direction, path)
    visited = {} # (position, direction): cost
    min_cost = float('inf')
    all_paths = []

    while not priority_queue.empty():
        cost, pos, dir, path = priority_queue.get() # visit tile with lowest cost

        # check if end point is reached
        if pos == end_point:
            if cost < min_cost:
                min_cost = cost
                all_paths = [path]
            elif cost == min_cost:
                all_paths.append(path)
            continue
        
        # this tile was already visited with lower cost, skip it
        if (pos, dir) in visited and visited[(pos, dir)] < cost:
            continue

        # mark as visited
        visited[(pos, dir)] = cost

        # iterate through counterclockwise, forward, clockwise
        for i in [-1, 0, 1]:
            new_dir = (dir+i)%4 # index of new direction

            # path blocked, skip
            if maze[pos[0] + directions[new_dir][0]][pos[1] + directions[new_dir][1]] == '#':
                continue

            # record new position and cost
            new_pos = (pos[0]+directions[new_dir][0], pos[1]+directions[new_dir][1])
            new_cost = cost + (1 if new_dir == dir else 1001)

            # if this position was not yet visited, or was visited with higher cost, add it to queue
            if (new_pos, new_dir) not in visited or visited[(new_pos, new_dir)] >= new_cost:
                priority_queue.put((new_cost, new_pos, new_dir, path + [new_pos]))

    return min_cost, all_paths

if __name__ == '__main__':
    maze = []
    with open('data/day_16_data.txt') as f:
        for line in f:
            maze.append([])
            for c in line.strip():
                maze[-1].append(c)

                if c == 'S':
                    start_point = (len(maze)-1, len(maze[-1])-1)

                if c == 'E':
                    end_point = (len(maze)-1, len(maze[-1])-1)

    cost, all_paths = solve(maze, start_point, end_point)
    unique_tiles = []
    for path in all_paths:
        unique_tiles.extend(path)

    unique_tiles = set(unique_tiles)
    print(cost)
    print(len(unique_tiles))