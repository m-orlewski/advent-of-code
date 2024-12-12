def get_next_nodes(m, i, j, plot_type):
    surrounding_plots = []
    if i-1 >= 0 and m[i-1][j] == plot_type:
        surrounding_plots.append((i-1, j)) # left
    if i+1 < len(m) and m[i+1][j] == plot_type:
        surrounding_plots.append((i+1, j)) # right
    if j-1 >= 0 and m[i][j-1] == plot_type:
        surrounding_plots.append((i, j-1)) # up
    if j+1 < len(m[i]) and m[i][j+1] == plot_type:
        surrounding_plots.append((i, j+1)) # down
    return surrounding_plots

def count_corners(m, i, j):
    plot_type = m[i][j]
    sides = 0

    # upper left
    if m[i][j-1] != plot_type and m[i-1][j] != plot_type:
        sides += 1
    elif m[i][j-1] == plot_type and m[i-1][j-1] != plot_type and m[i-1][j] == plot_type:
        sides += 1

    # upper right
    if m[i][j+1] != plot_type and m[i-1][j] != plot_type:
        sides += 1
    elif m[i][j+1] == plot_type and m[i-1][j+1] != plot_type and m[i-1][j] == plot_type:
        sides += 1

    # lower left
    if m[i][j-1] != plot_type and m[i+1][j] != plot_type:
        sides += 1
    elif m[i][j-1] == plot_type and m[i+1][j-1] != plot_type and m[i+1][j] == plot_type:
        sides += 1

    # lower right
    if m[i][j+1] != plot_type and m[i+1][j] != plot_type:
        sides += 1
    elif m[i][j+1] == plot_type and m[i+1][j+1] != plot_type and m[i+1][j] == plot_type:
        sides += 1

    return sides


def bfs(m, i, j, visited):
    q = [(i, j)]
    plot_type = m[i][j]
    area = 0
    sides = 0
    total_neighbors = 0
    visited.add((i, j))
    while len(q):
        v = q.pop(0)
        sides += count_corners(m, *v)
        area += 1
        next_nodes = get_next_nodes(m, *v, plot_type)
        total_neighbors += len(next_nodes)
        for next in next_nodes:
            if next not in visited:
                q.append(next)
                visited.add(next)
            
    return area, 4*area - total_neighbors, sides

if __name__ == '__main__':
    m = []
    with open('data/day_12_data.txt') as f:
        for line in f:
            m.append([])
            m[-1].append('_')
            for c in line.strip():
                m[-1].append(c)
            m[-1].append('_')

    C = len(m[0])
    m.append(['_']*C)
    m.insert(0, ['_']*C)

    ans1 = 0
    ans2 = 0
    visited = set()
    for i in range(1, len(m)-1):
        for j in range(1, len(m[i])-1):
            if (i, j) in visited:
                continue
                       
            area, perimeter, sides = bfs(m, i, j, visited)
            print(m[i][j], area, perimeter, sides)
            ans1 += area*perimeter
            ans2 += area*sides
    
    print(ans1)
    print(ans2)