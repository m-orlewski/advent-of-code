from collections import Counter
 
def disk_map_to_file_blocks(disk_map):
    file_blocks = ['.' for _ in range(sum(disk_map))]
    current_id = 0
    file_block = True
 
    i = 0
    for d in disk_map:
        if file_block:
            for _ in range(d):
                file_blocks[i] = current_id
                i += 1
            current_id += 1
        else:
            i += d
        file_block = not file_block
 
    return file_blocks
 
def optimize_file_blocks(file_blocks):
    r = len(file_blocks)-1
 
    for i in range(len(file_blocks)):
        if r < i:
            break
 
        if file_blocks[i] != '.':
            continue
 
        file_blocks[i] = file_blocks[r]
        r -= 1
        while file_blocks[r] == '.':
            r -= 1
 
    return file_blocks[:i]
 
def get_empty_segments(file_blocks):
    empty_segments = [] # not dict because keys and values will change and we want to preserve the order
    i = 0
    while i < len(file_blocks):
        if file_blocks[i] == '.':
            count = 1
            while i+count < len(file_blocks) and file_blocks[i+count] == '.':
                count += 1
            empty_segments.append([i, count])
            i += count
        else:
            i += 1
    return empty_segments
 
 
def optimize_file_blocks_2(file_blocks, counter, empty_segments):
    for id, count in counter.items():
        start = file_blocks.index(id)
        for i in range(len(empty_segments)):
            segment_start, segment_len = empty_segments[i]
            if count <= segment_len and segment_start < start:
                file_blocks[start:start+count] = ['.']*count
                file_blocks[segment_start:segment_start+count] = [id]*count
                if count == segment_len:
                    del empty_segments[i]
                else:
                    empty_segments[i] = [segment_start+count, segment_len-count]
                break
 
    return file_blocks
 
 
if __name__ == '__main__':
    with open('data.txt') as file:
        data = file.read().strip()
        disk_map = [int(c) for c in data]
 
    file_blocks = disk_map_to_file_blocks(disk_map)
    optimized_file_blocks = optimize_file_blocks(file_blocks.copy())
 
    ans1 = 0
    for i, d in enumerate(optimized_file_blocks):
        ans1 += i * d
    print(ans1)
 
    counter = Counter(file_blocks)
    counter.pop('.')
    counter = dict(sorted(counter.items(), key=lambda x: x[0], reverse=True))
    empty_segments = get_empty_segments(file_blocks)
    optimized_file_blocks_2 = optimize_file_blocks_2(file_blocks, counter, empty_segments)
    ans2 = 0
    for i, d in enumerate(optimized_file_blocks_2):
        if d != '.':
            ans2 += i * d
    print(ans2)
