import re

with open("data/day_3_data.txt") as f:
    data = f.read()

mul_sum_1 = 0
mul_sum_2 = 0
enabled = True
for s in re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', data):
    if s == 'do()':
        enabled = True
    elif s == 'don\'t()':
        enabled = False
    else:
        x, y = re.findall(r'\d+', s)
        mul_sum_1 += int(x)*int(y)
        if enabled:
            mul_sum_2 += int(x)*int(y)

print(mul_sum_1)
print(mul_sum_2)
