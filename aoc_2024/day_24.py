known_wires = {}
gates = {}

def solve(gate, wire1, op, wire2):
    if wire1 not in known_wires:
        solve(wire1, *gates[wire1])

    if wire2 not in known_wires:
        solve(wire2, *gates[wire2])

    if wire1 in known_wires and wire2 in known_wires:
        if op == 'OR':
            known_wires[gate] = known_wires[wire1] | known_wires[wire2]
        elif op == 'AND':
            known_wires[gate] = known_wires[wire1] & known_wires[wire2]
        else:
            known_wires[gate] = known_wires[wire1] ^ known_wires[wire2]

if __name__ == '__main__':
    
    with open('data/day_24_data.txt') as f:
        for line in f:
            if line.strip() == '':
                break
            wire, bit = line.strip().split(':')
            known_wires[wire] = int(bit)

        for line in f:
            line = line.strip().split(' ')
            gates[line[4]] = line[:3]

    for gate, [wire1, op, wire2] in gates.items():
        solve(gate, wire1, op, wire2)

    ans1 = ''
    for k, v in sorted(known_wires.items(), reverse=True):
        if k[0] == 'z':
            ans1 += str(v)
    print(int(ans1, 2))