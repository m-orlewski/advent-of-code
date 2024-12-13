from collections import Counter
 
def transform_stone(old_stone):
    if old_stone == 0:
        return [1]
 
    s = str(old_stone)
    l = len(s)
    if l % 2 == 0:
        return [int(s[:l//2]), int(s[l//2:])]
    else:
        return [old_stone*2024]
 
def blink(counter):
    new_counter = Counter()
    for old_stone, old_count in counter.items():
        new_stones = transform_stone(old_stone)
        for new_stone in new_stones:
            new_counter[new_stone] += old_count
 
    return new_counter
 
if __name__ == '__main__':
    with open('data/day_11_data.txt') as f:
        for line in f:
            counter = Counter(list(map(int, line.strip().split(' '))))
 
    for _ in range(25):
        counter = blink(counter)
    print(sum(counter.values()))
 
    for _ in range(50):
        counter = blink(counter)
    print(sum(counter.values()))
