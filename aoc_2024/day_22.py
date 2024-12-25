from collections import Counter

def mix_and_prune(currentSecretNumber, previousSecretNumber):
    currentSecretNumber = currentSecretNumber ^ previousSecretNumber
    currentSecretNumber %= 16777216
    return currentSecretNumber

def calculateSecretNumber(secretNumber, N):
    prev = secretNumber
    changes = []
    sequences = {}
    for _ in range(N):
        secretNumber = mix_and_prune(secretNumber*64, secretNumber)
        secretNumber = mix_and_prune(secretNumber//32, secretNumber)
        secretNumber = mix_and_prune(secretNumber*2048, secretNumber)
        changes.append(secretNumber%10 - prev%10)
        prev = secretNumber
        if len(changes) > 3:
            sequence = tuple(changes[-4:])
            if sequence not in sequences:
                sequences[sequence] = secretNumber%10

    return secretNumber, sequences

if __name__ == '__main__':
    ans1 = 0
    all_sequences = []
    with open('data/day_22_data.txt') as f:
        for i, line in enumerate(f):
            secretNumber = int(line.strip())
            price, sequences = calculateSecretNumber(secretNumber, 2000)
            all_sequences.append(sequences)
            ans1 += price
    print(ans1)
    
    combined_sequences = Counter()
    for sequences in all_sequences:
        combined_sequences += Counter(sequences)

    print(combined_sequences.most_common(1)[0][1])