def calculate_pins(schematic):
    pins = [0] * 5
    for row in schematic:
        for i, c in enumerate(row):
            if c == '#':
                pins[i] += 1

    return pins


if __name__ == '__main__':
    locks = []
    keys = []
    schematic = []
    with open('data/day_25_data.txt') as f:
        for line in f:
            line = line.strip()
            if line != '':
                schematic.append(line)
            else:
                if schematic[0] == '#####':
                    locks.append(calculate_pins(schematic[1:-1]))
                else:
                    keys.append(calculate_pins(schematic[1:-1]))
                schematic = []
    
    # last lock/key
    if schematic[0] == '#####':
        locks.append(calculate_pins(schematic[1:-1]))
    else:
        keys.append(calculate_pins(schematic[1:-1]))

    ans1 = len(locks)*len(keys)
    for lock in locks:
        for key in keys:
            for i in range(5):
                if lock[i] + key[i] > 5:
                    ans1 -= 1
                    break

    print(ans1)
            


    
                
                