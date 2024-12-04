count_1 = 0
count_2 = 0
data = []
starting_points = []
with open('data/day_4_data.txt') as f:
    for row, line in enumerate(f):
        data.append(line.strip())

target = ['XMAS', 'SAMX']
for r in range(len(data)):
    for c in range(len(data[r])):
        # horizontal
        s = data[r][c:c+4]
        if c+3 < len(data[r]) and s in target:
            count_1 += 1
        # vertical
        if r+3 < len(data):
            s = data[r][c] + data[r+1][c] + data[r+2][c] + data[r+3][c]
            if s in target:
                count_1 += 1
        # diagonal
        if r+3 < len(data):
            if c+3 < len(data[r]):
                s = data[r][c] + data[r+1][c+1] + data[r+2][c+2] + data[r+3][c+3]
                if s in target:
                    count_1 += 1
            if c-3 >= 0:
                s = data[r][c] + data[r+1][c-1] + data[r+2][c-2] + data[r+3][c-3]
                if s in target:
                    count_1 += 1

        if data[r][c] == 'A' and r-1 >= 0 and c-1 >= 0 and r+1 < len(data) and c+1 < len(data[r]):
            s = data[r-1][c-1] + data[r-1][c+1] + data[r+1][c-1] + data[r+1][c+1]
            if s in ['MSMS', 'SMSM', 'MMSS', 'SSMM']:
                count_2 += 1


print(count_1)
print(count_2)
