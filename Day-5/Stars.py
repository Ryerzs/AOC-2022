import time
from collections import deque
import copy

def day_():
    path = "data.txt"
    # path = "test-data.txt"

    start_time = time.perf_counter()
    piles, instructions = get_data(path)

    time1 = time.perf_counter()
    piles2 = copy.deepcopy(piles)
    ans1 = star1(piles, instructions)
    time2 = time.perf_counter()

    ans2 = star2(piles2, instructions)
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
    test_crate_pile_row = 3
    test_last_row = 3
    data_crate_pile_row = 9
    data_last_row = 8
    # number_of_crate_piles = test_crate_pile_row
    number_of_crate_piles = data_crate_pile_row
    # last_line = test_last_row
    last_line = data_last_row
    instructions = []
    piles = {}
    for i in range(number_of_crate_piles):
        piles[i] = deque()
    with open(path) as f:
        rows = f.read().splitlines()
        for i, row in enumerate(rows):
            if(0 <= i < last_line):
                for j in range(1, number_of_crate_piles*4-1, 4):
                    if row[j] == ' ':
                        continue
                    piles[(j-1)/4].appendleft(row[j])
            # if(i <= data_crate_pile_row+1):
            if(i <= last_line+1):
                continue
            info = row.split(' ')
            info = [info[1], info[3], info[5]]
            info = [int(number) for number in info]
            instructions.append(info)
    
    return piles, instructions
                
    
def star1(piles, instructions):
    for instruction in instructions:
        number_of_crates = instruction[0]
        from_pile = instruction[1]-1
        to_pile = instruction[2]-1
        for i in range(number_of_crates):
            crate = piles[from_pile].pop()
            piles[to_pile].append(crate)
    output = ''
    for crates in piles.values():
        output = output + crates.pop()
    return output

def star2(piles, instructions):
    for instruction in instructions:
        number_of_crates = instruction[0]
        from_pile = instruction[1]-1
        to_pile = instruction[2]-1
        crate_pile_moving = deque()
        for i in range(number_of_crates):
            crate_pile_moving.append(piles[from_pile].pop())
        for i in range(number_of_crates):
            piles[to_pile].append(crate_pile_moving.pop())
    output = ''
    for crates in piles.values():
        output = output + crates.pop()
    return output

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