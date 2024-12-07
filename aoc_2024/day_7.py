def is_equation_possible(test_value, operands):
    if len(operands) == 1:
        return operands[0] == test_value
    else:
        if operands[0] > test_value:
            return False
        
        return is_equation_possible(test_value, [operands[0]+operands[1]] + operands[2:]) or \
        is_equation_possible(test_value, [operands[0]*operands[1]] + operands[2:])

def is_equation_possible_with_concat(test_value, operands):
    if len(operands) == 1:
        return operands[0] == test_value
    else:
        if operands[0] > test_value:
            return False
        
        return is_equation_possible_with_concat(test_value, [operands[0]+operands[1]] + operands[2:]) or \
        is_equation_possible_with_concat(test_value, [operands[0]*operands[1]] + operands[2:]) or \
        is_equation_possible_with_concat(test_value, [operands[0] * (10 ** len(str(operands[1]))) + operands[1]] + operands[2:])

ans1 = 0
ans2 = 0
with open("data/day_7_data.txt") as f:
    for line in f:
        numbers = line.strip().split(' ')
        test_value = int(numbers[0].rstrip(':'))
        operands = list(map(int, numbers[1:]))

        if is_equation_possible(test_value, operands):
            ans1 += test_value

        if is_equation_possible_with_concat(test_value, operands):
            ans2 += test_value

print(ans1)
print(ans2)