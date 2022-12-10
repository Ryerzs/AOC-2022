import time

def day_():
    path = "data.txt"
    # path = "test-data.txt"

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
            # print(row)
            instruction = []
            info = row.split(' ')
            if info[0] == 'noop':
                instruction.append(0)
            else:
                instruction.append(1)
                instruction.append(int(info[1]))
            data.append(instruction)
    return data
    
def star1(data):
    cycle = 0
    x = 1
    interesting_cycle_indices = [20+40*i for i in range(6)]
    interesting_cycles = []
    for instruction in data:
        if instruction[0] == 0:
            cycle += 1
            if cycle in interesting_cycle_indices:
                interesting_cycles.append(x*cycle)
            continue
        for operation in range(2):
            cycle += 1
            if cycle in interesting_cycle_indices:
                interesting_cycles.append(x*cycle)
            if operation == 1:
                x += instruction[1]
    return sum(interesting_cycles)

def star2(data):
    out = []
    cycle = 0
    x = 1
    interesting_cycle_indices = [20+40*i for i in range(6)]
    for instruction in data:
        if instruction[0] == 0:
            cycle += 1
            out.append(get_char_for_cycle(x,cycle))
            continue
        for operation in range(2):
            cycle += 1
            out.append(get_char_for_cycle(x,cycle))
            if operation == 1:
                x += instruction[1]
    
    # print(out)
    # out = ['#' for i in range(240)]
    out = ''.join(out)
    for i in interesting_cycle_indices:
        start = i -20
        end = i +20
        print(out[start:end])
        
    return 0

def get_char_for_cycle(x, cycle):
    cycle = (cycle-1) %40
    range_for_sprite = range(x-1, x+2)
    print(cycle, x)
    if (cycle) in range_for_sprite:
        return '#'
    return '.'

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