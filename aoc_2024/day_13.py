import re

def solve_linear_system(a, b, target):
    det = a[0]*b[1] - a[1]*b[0]
    if det == 0:
        return 0

    x = (target[0]*b[1] - target[1]*b[0]) // det
    y = (target[1]*a[0] - target[0]*a[1]) // det

    # verify
    if a[0]*x + b[0]*y == target[0] and a[1]*x + b[1]*y == target[1]:
        return 3*x + y

    return 0

if __name__ == '__main__':
    ans1 = 0
    ans2 = 0
    with open('data/day_13_data.txt') as f:
        while True:
            lines = [f.readline() for _ in range(4)]

            if not lines[0]:
                break

            a = tuple(map(int, re.findall(r'\d+', lines[0])))
            b = tuple(map(int, re.findall(r'\d+', lines[1])))
            target = tuple(map(int, re.findall(r'\d+', lines[2])))

            ans1 += solve_linear_system(a, b, target)
            ans2 += solve_linear_system(a, b, (target[0]+10000000000000, target[1]+10000000000000))

    print(ans1)
    print(ans2)