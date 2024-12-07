class Lab:
    GUARD_MOVES = [(-1,0), (0,1), (1,0), (0,-1)]
 
    def __init__(self, map, guard_pos):
        self.map = map
        self.guard_x = guard_pos[0]
        self.guard_y = guard_pos[1]
        self.guard_direction = 0 # 0: UP, 1: RIGHT, 2: DOWN, 3: LEFT
        self.start_pos_x = guard_pos[0]
        self.start_pos_y = guard_pos[1]
 
    def print_map(self):
        for row in self.map:
            for c in row:
                print(c, end='')
            print()
 
    def update_direction(self):
        self.guard_direction = (self.guard_direction + 1) % 4
 
    def guard_out_of_bounds(self):
        if self.guard_x < 0 or self.guard_y < 0 or \
            self.guard_x >= len(self.map) or self.guard_y >= len(self.map[self.guard_x]):
            return True
 
        return False
 
    def move_guard_forward(self):
        self.guard_x += self.GUARD_MOVES[self.guard_direction][0]
        self.guard_y += self.GUARD_MOVES[self.guard_direction][1]
 
    def move_guard_back(self):
        self.guard_x -= self.GUARD_MOVES[self.guard_direction][0]
        self.guard_y -= self.GUARD_MOVES[self.guard_direction][1]
 
    def count_visited_tiles(self):
        visited_tiles = 1
 
        while not self.guard_out_of_bounds():
            if map[self.guard_x][self.guard_y] == '.':
                map[self.guard_x][self.guard_y] = 'X'
                visited_tiles += 1
            elif map[self.guard_x][self.guard_y] == '#':
                self.move_guard_back()
                self.update_direction()
 
            self.move_guard_forward()
 
        return visited_tiles
 
    def is_guard_in_loop(self):
        # guard to starting position
        self.guard_x = self.start_pos_x
        self.guard_y = self.start_pos_y
        self.guard_direction = 0
 
        encountered_obstacles_with_direction = {}
        while not self.guard_out_of_bounds():
 
            if map[self.guard_x][self.guard_y] == '#':
                if (self.guard_x, self.guard_y) in encountered_obstacles_with_direction:
                    if self.guard_direction ==  encountered_obstacles_with_direction[(self.guard_x, self.guard_y)]:
                        return True
                else:
                    encountered_obstacles_with_direction[(self.guard_x, self.guard_y)] = self.guard_direction
                self.move_guard_back()
                self.update_direction()
 
            self.move_guard_forward()
 
        return False
 
    def count_loops(self):
        loops = 0
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if map[x][y] == 'X':
                    map[x][y] = '#' 
                    if self.is_guard_in_loop():
                        loops += 1
                    map[x][y] = 'X'
        return loops
 
if __name__ == '__main__':
    map = []
    with open('data/day_6_data.txt') as file:
        for x, line in enumerate(file):
            map.append([])
            for y, c in enumerate(line.strip()):
                map[-1].append(c)
                if c == '^':
                    guard_pos = (x, y)
 
    lab = Lab(map, guard_pos)
    print(f'Visited tiles {lab.count_visited_tiles()}')
    print(f'Possible loops {lab.count_loops()}')