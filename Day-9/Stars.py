import time
import math

def day_():
    path = "Day-9/data.txt"
    # path = "Day-9/test-data2.txt"
    # path = "Day-9/test-data3.txt"

    start_time = time.perf_counter()
    data = get_data(path)

    time1 = time.perf_counter()

    ans1 = star1(data)
    time2 = time.perf_counter()

    ans2 = star2(data)
    time3 = time.perf_counter()

    load_time = time1 - start_time
    star1_time = time2 - time1
    star2_time = time3 - time2
    if 1:
        print(f'Load time: {load_time}')
        print(f'Star 1 time: {star1_time}')
        print(f'Star 2 time: {star2_time}')
        print(f'Star 1 answer: {ans1}')
        print(f'Star 2 answer: {ans2}')

def get_data(path):
    data = []
    with open(path) as f:
        rows = f.read().splitlines()
        for row in rows:
            data.append(row.split(' '))
    return data
    
def star1(data):
    direction_map = {'U':(0,1), 'R':(1,0), 'D':(0,-1), 'L':(-1,0)}
    head = Head((0,0), None)
    for i in range(9):
        head.set_tail((0,0))
    count = 0
    for instruction in data:
        times = int(instruction[1])
        direction = instruction[0]
        direction = direction_map[direction]
        for i in range(times):
            head.move_head(direction)
        # count += 1
        # if count >= 20:
        #     break
        # draw_rope(head, 15)
    positions = head.get_positions()
    print(positions)
    print(str(head))
    return len(positions)

def draw_rope(head, size):
    positions = []
    current = head
    positions.append(current.pos) 
    while current.tail is not None:
        current = current.tail
        positions.append(current.pos) 
    # print(positions)
    out = [['.' for i in range(size*2+1)] for i in range(size*2+1)]
    table = ['9', '8', '7', '6', '5', '4', '3', '2', '1', 'H']
    positions.reverse()
    # print(out)
    out[size][size] = 's'
    for i, pos in enumerate(positions):
        x = pos[0] + size
        y = pos[1] + size
        out[y][x] = table[i]
    
    out.reverse()

    for i, row in enumerate(out, start = 0):
        print(''.join(row) + str(size-i))
    print(head.get_positions())


def star2(data):
    return 0


class Head():
    def __init__(self, head_pos, tail=None):
        self.pos = head_pos
        self.tail = tail
        self.positions = set()
        self.positions.add(head_pos)
    
    def __str__(self):
        out = str(self.pos) + ', '
        if self.tail != None:
            out = out + str(self.tail)
        return out
    
    def set_tail(self, position):
        if self.tail is None:
            self.tail = Head(position, None)
            return
        self.tail.set_tail(position)
    def set_head(self, position):
        if self.tail is None:
            self.pos = position
            self.positions.add(self.pos)
            return
        # Figure out if self is going to make diagonal move
        distance = self.get_distance(self.pos, position)
        distance_from_tail = self.get_distance(self.tail.pos, position)
        is_diagonal_move = distance >= 1.1
        is_in_line = 1.9 <= distance_from_tail <= 2.1
        # If diagonal move and tail not connected after new position
        # then tail will move same relative amount as self
        if not self.tail_connected(position, self.tail.pos):
            if is_diagonal_move and is_in_line:
                offset = (round((position[0] - self.tail.pos[0])/2), round((position[1] - self.tail.pos[1])/2))
                new_tail_pos = self.get_relative_position(self.tail.pos, offset)
                pass
            elif is_diagonal_move:
                offset = (position[0] - self.pos[0], position[1] - self.pos[1])
                new_tail_pos = self.get_relative_position(self.tail.pos, offset)
            else:
                new_tail_pos = self.pos
            self.tail.set_head(new_tail_pos)
        self.pos = position

    def move_head(self, direction):
        new_head_pos = self.get_relative_position(self.pos, direction)
        if not self.tail_connected(new_head_pos, self.tail.pos):
            self.tail.set_head(self.pos)
        self.pos = new_head_pos

    def tail_connected(self, head_pos, tail_pos):
        return self.get_distance(head_pos, tail_pos) <= 1.9
    
    def get_distance(self, position1, position2):
        return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)
    
    def get_relative_position(self, position, offset):
        return (position[0] + offset[0], position[1] + offset[1])
    
    def get_positions(self):
        if self.tail == None:
            return self.positions 
        return self.tail.get_positions()
    
    ## if not connected and keep relative,
    ## move relative
    ## if moved horizontal, Keep relative
    ## Check if not connected

def main():
    import cProfile
    import pstats
    with cProfile.Profile() as pr:
        day_()
    
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename = 'profiling.prof')

if __name__ == '__main__':
    main()