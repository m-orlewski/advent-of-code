from copy import deepcopy

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def printMap(map):
    print()
    for i, row in enumerate(map):
        if i < 10:
            print(f'0{i}', end=' ')
        else:
            print(i, end=' ')
        for c in row:
            print(c, end='')
        print()
    print()

def processMoves1(map, moves, robot_x, robot_y):
    for i in range(len(moves)):
        dx, dy = directions[moves[i]]
        new_robot_x, new_robot_y = robot_x + dx, robot_y + dy
        
        if map[new_robot_x][new_robot_y] == '.':
            map[new_robot_x][new_robot_y] = '@'
            map[robot_x][robot_y] = '.'
            robot_x, robot_y = new_robot_x, new_robot_y
        elif map[new_robot_x][new_robot_y] == '#':
            continue
        elif map[new_robot_x][new_robot_y] == 'O':
            x, y = new_robot_x, new_robot_y
            iter = 1
            while True:
                x += dx
                y += dy
                if map[x][y] == '.':
                    for i in range(iter+1):
                        map[x-dx*i][y-dy*i], map[x-dx*(i+1)][y-dy*(i+1)] = map[x-dx*(i+1)][y-dy*(i+1)], map[x-dx*i][y-dy*i] 
                    robot_x, robot_y = new_robot_x, new_robot_y
                    break
                elif map[x][y] == '#':
                    break
                else:
                    iter += 1
        
def processMoves2(map, moves, robot_x, robot_y):
    for i in range(len(moves)):
        dx, dy = directions[moves[i]]

        new_robot_x, new_robot_y = robot_x + dx, robot_y + dy
        
        if map[new_robot_x][new_robot_y] == '.':
            map[new_robot_x][new_robot_y] = '@'
            map[robot_x][robot_y] = '.'
            robot_x, robot_y = new_robot_x, new_robot_y
        elif map[new_robot_x][new_robot_y] == '#':
            continue
        elif map[new_robot_x][new_robot_y] in '[]' and moves[i] in '<>':
            x, y = new_robot_x, new_robot_y
            iter = 1
            while True:
                x += dx
                y += dy
                if map[x][y] == '.':
                    for j in range(iter+1):
                        map[x-dx*j][y-dy*j], map[x-dx*(j+1)][y-dy*(j+1)] = map[x-dx*(j+1)][y-dy*(j+1)], map[x-dx*j][y-dy*j] 
                    robot_x, robot_y = new_robot_x, new_robot_y
                    break
                elif map[x][y] == '#':
                    break
                else:
                    iter += 1
        else:
            x, y = new_robot_x, new_robot_y
            boxes_to_push = {}
            if map[x][y] == '[':
                boxes_to_push[x] = [y, y+1]
            else:
                boxes_to_push[x] = [y-1, y]

            row = x
            while len(boxes_to_push[row]):
                previous_row = row
                row += dx
                boxes_to_push[row] = []

                if map[row][boxes_to_push[previous_row][0]-1] == '[':
                    boxes_to_push[row].append(boxes_to_push[previous_row][0]-1)
                else:
                    for j in range(boxes_to_push[previous_row][0], boxes_to_push[previous_row][1]+1):
                        if map[row][j] == '[':
                            boxes_to_push[row].append(j)
                            break

                if map[row][boxes_to_push[previous_row][1]+1] == ']':
                    boxes_to_push[row].append(boxes_to_push[previous_row][1]+1)
                else:
                    for j in range(boxes_to_push[previous_row][1], boxes_to_push[previous_row][0]-1, -1):
                        if map[row][j] == ']':
                            boxes_to_push[row].append(j)
                            break

            

            del boxes_to_push[row]
            
            if dx == -1:
                boxes_to_push = dict(sorted(boxes_to_push.items())) # direction is up
            else:
                boxes_to_push = dict(sorted(boxes_to_push.items(), reverse=True))# direction is down

            
            # check if there are no obstacles for boxes
            obstacle = False
            for k, v in boxes_to_push.items():
                for c in range(v[0], v[1]+1):
                    if map[k][c] in '[]' and map[k+dx][c] == '#':
                        obstacle = True
                        break

                if obstacle:
                    break

            if not obstacle:
                for k, v in boxes_to_push.items():
                    for c in range(v[0], v[1]+1):
                        if map[k][c] in '[]':
                            map[k+dx][c] = map[k][c]
                            map[k][c] = '.'

                map[new_robot_x][new_robot_y] = '@'
                map[robot_x][robot_y] = '.'
                robot_x, robot_y = new_robot_x, new_robot_y



def transformMap(map):
    newMap = []

    for row in map:
        newMap.append([])
        for c in row:
            if c == 'O':
                newMap[-1].extend(['[', ']'])
            elif c == '@':
                newMap[-1].extend(['@', '.'])
                robot_x = len(newMap)-1
                robot_y = len(newMap[-1])-2
            else:
                newMap[-1].extend([c, c])

    return newMap, robot_x, robot_y


original = []
moves = []

with open('data/day_15_data.txt') as f:
    for x, line in enumerate(f):
        if line == '\n':
             break
        original.append([])
        for y, c in enumerate(line.strip()):
                if c == '@':
                     robot_x, robot_y = x, y
                original[-1].append(c)
            
    for line in f:
        for c in line.strip():
            moves.append(c)

map = deepcopy(original)
processMoves1(map, moves, robot_x, robot_y)

ans1 = 0
for x in range(len(map)):
    for y in range(len(map[x])):
        if map[x][y] == 'O':
            ans1 += 100*x + y

print(ans1)


map, robot_x, robot_y = transformMap(original)

processMoves2(map, moves, robot_x, robot_y)
ans2 = 0
for x in range(len(map)):
    for y in range(len(map[x])):
        if map[x][y] == '[':
            ans2 += 100*x + y

print(ans2)

