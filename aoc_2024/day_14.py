import re
from functools import reduce
from copy import deepcopy

WIDTH = 101
HEIGHT = 103

class Robot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def __str__(self):
        return f'Robot at p=({self.px}, {self.py}) with velocity=({self.vx}, {self.vy})'
    
    def simulate_move(self, t):
        self.px += self.vx * t
        self.py += self.vy * t

        self.px %= WIDTH
        self.py %= HEIGHT

def printMap(m):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(m[i][j][0], end='')
        print()

if __name__ == '__main__':
    ans1 = 0
    robots = []
    with open('data/day_14_data.txt') as f:
        for line in f:
            robots.append(Robot(*list(map(int, re.findall('-?\d+', line.strip())))))

    quadrants = [0, 0, 0, 0]
    for robot in deepcopy(robots):
        robot.simulate_move(100)

        if robot.px < (WIDTH-1) // 2 and robot.py < (HEIGHT-1) // 2:
            quadrants[0] += 1
        elif robot.px > (WIDTH-1) // 2 and robot.py < (HEIGHT-1) // 2:
            quadrants[1] += 1
        elif robot.px < (WIDTH-1) // 2 and robot.py > (HEIGHT-1) // 2:
            quadrants[2] += 1
        elif robot.px > (WIDTH-1) // 2 and robot.py > (HEIGHT-1) // 2:
            quadrants[3] += 1

    ans1 = reduce(lambda x, y: x*y, quadrants, 1)
    print(ans1)

    m = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    counts = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for robot in robots:
            m[robot.py][robot.px] = '#'
            counts[robot.py][robot.px] += 1
    
    iter = 1
    found = False
    while not found:
        for robot in robots:
            counts[robot.py][robot.px] -= 1
            if counts[robot.py][robot.px] == 0:
                m[robot.py][robot.px] = '.'

            robot.simulate_move(1)
            m[robot.py][robot.px] = '#'
            counts[robot.py][robot.px] += 1


        # search for box - naive solution to not well described task
        for i in range(HEIGHT):
            for j in range(WIDTH-10):
                if m[i][j:j+10] == ['#']*10:
                    print(iter)
                    found = True
                    break

            if found:
                break
                    

        iter += 1
        