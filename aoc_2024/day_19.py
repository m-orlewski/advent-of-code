class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isLast = True

    def match_prefixes(self, s):
        node = self.root
        matched = [] # list of indices up to which the prefix was matched
        for i in range(len(s)):
            c = s[i]
            if c in node.children:
                node = node.children[c]
                if node.isLast:
                    matched.append(i+1)
            else:
                break

        return matched

mem = {}
def count_designs(trie, s):
    if s in mem:
        return mem[s]

    if not len(s):
        return 1
    
    count = 0
    matched = trie.match_prefixes(s)
    for prefix_end in matched:
        count += count_designs(trie, s[prefix_end:])
    
    mem[s] = count
    return mem[s]

def count_combinations(s):
    return 0

if __name__ == '__main__':
    ans1, ans2 = 0, 0
    with open('data/day_19_data.txt') as f:
        patterns = f.readline().strip().split(', ')

        trie = Trie()
        for pattern in patterns:
            trie.insert(pattern)

        f.readline()
        for line in f:
            s = line.strip()
            count = count_designs(trie, s)
            if count:
                ans1 += 1
                ans2 += count

    print(ans1)
    print(ans2)