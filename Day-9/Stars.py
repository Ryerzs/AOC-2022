import time
import math

def day_():
    path = "data.txt"
    path = "Day-9/test-data.txt"

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
        count += 1
        if count >= 20:
            break
    positions = head.get_positions()
    print(positions)
    print(str(head))
    return len(positions)


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
        if not self.tail_connected(position, self.tail.pos):
            self.tail.set_head(self.pos)
        self.pos = position
    def move_head(self, direction):
        new_head_pos = (self.pos[0] + direction[0], self.pos[1] + direction[1])
        if not self.tail_connected(new_head_pos, self.tail.pos):
            self.tail.set_head(self.pos)
        self.pos = new_head_pos

    def tail_connected(self, head_pos, tail_pos):
        distance = math.sqrt((head_pos[0]-tail_pos[0])**2 + (head_pos[1]-tail_pos[1])**2)
        return distance <= 1.9
    
    def get_positions(self):
        if self.tail == None:
            return self.positions 
        return self.tail.get_positions()

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