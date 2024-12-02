from collections import Counter

left = []
right = []

with open('data/day_1_data.txt') as f:
    for line in f:
        row = line.strip().split()
        left.append(int(row[0]))
        right.append(int(row[1]))

left.sort()
right.sort()

distance = 0
for l, r in zip(left, right):
    distance += abs(l - r)

print(distance)

counter = Counter(right)

similarity_score = 0
for l in left:
    similarity_score += l * counter[l]

print(similarity_score)