order = {}
updates = []

with open('data/day_5_data.txt') as f:
    for line in f:
        if line == '\n':
            break

        nums = line.strip().split('|')
        order.setdefault(int(nums[0]), []).append(int(nums[1]))

    for line in f:
        updates.append(list(map(int, line.strip().split(','))))

ans1 = 0
incorrect_updates = []
for update in updates:
    already_printed = []
    correct = True
    for page in update:
        if page in order:
            for printed in already_printed:
                if printed in order[page]:
                    correct = False
                    break

        if not correct:
            incorrect_updates.append(update)
            break

        already_printed.append(page)
    else:
        ans1 += update[len(update)//2]

ans2 = 0
for update in incorrect_updates:
    for i, page in enumerate(update):
        if page in order:
            for j in range(i-1, -1, -1):
                if update[j] in order[page]:
                    update[i], update[j] = update[j], update[i]
                    i = j

    ans2 += update[len(update)//2]


print(ans1)
print(ans2)