import re
from math import floor
import sys

numbers = []
with open('data/day_17_data.txt') as f:
    for line in f:
        numbers.extend(list(map(int, re.findall(r'\d+', line))))

A = numbers[0]
B = numbers[1]
C = numbers[2]
numbers = numbers[3:]

def combo_operand(operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        print('invalid literal operand')
        sys.exit(1)

i = 0
output = []
while i+1 < len(numbers):
    opcode = numbers[i]
    operand = numbers[i+1]

    if opcode == 0:
        A = floor(A / (2**combo_operand(operand)))
    elif opcode == 1:
        B = B ^ operand
    elif opcode == 2:
        B = combo_operand(operand) % 8
    elif opcode == 3 and A != 0:
        i = operand
        continue
    elif opcode == 4:
        B = B ^ C
    elif opcode == 5:
        output.append(str(combo_operand(operand)%8))
    elif opcode == 6:
        B = floor(A / (2**combo_operand(operand)))
    elif opcode == 7:
        C = floor(A / (2**combo_operand(operand)))
    i += 2

print(','.join(output))

# Register A: 46187030
# Register B: 0
# Register C: 0

# Program: 2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0

# 2,4 # B = A % 8
# 1,5 # B = B ^ 5
# 7,5 # C = A >> B
# 0,3 # A = A >> 3
# 4,0 # B = B ^ C
# 1,6 # B = B ^ 6
# 5,5 # out(B % 8)
# 3,0 # if A != 0: back to start

def solve(numbers, target):
    if not len(numbers):
        return target
    for i in range(8):
        A = target << 3 | i
        B = A % 8
        B = B ^ 5
        C = A >> B
        B = B ^ C
        B = B ^ 6
        if B % 8 == numbers[-1]:
            sub = solve(numbers[:-1], A)
            if sub is not None:
                return sub

print(solve(numbers, 0))