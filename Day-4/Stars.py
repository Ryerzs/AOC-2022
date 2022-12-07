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
        for r in rows:
            ranges = r.split(',')
            range_1 = [int(string_number) for string_number in ranges[0].split('-')]
            range_2 = [int(string_number) for string_number in ranges[1].split('-')]
            data.append((range_1, range_2))
    return data
    
def star1(data):
    contains_range = []
    for intervall in data:
        if contains_other(intervall[0], intervall[1]):
            contains_range.append(1)
            continue
        contains_range.append(0)

    return sum(contains_range)

def contains_other(range_1, range_2):
    if(range_1[0] <= range_2[0] and range_1[1]>= range_2[1]):
        return True
    if(range_2[0] <= range_1[0] and range_2[1]>= range_1[1]):
        return True
    return False

def star2(data):
    overlaps_range = []
    for intervall in data:
        if overlaps(intervall[0], intervall[1]):
            overlaps_range.append(1)
            continue
        overlaps_range.append(0)

    return sum(overlaps_range)

def overlaps(range_1, range_2):
    if(range_1[0] <= range_2[0] <= range_1[1]):
        return True
    if(range_1[0] <= range_2[1] <= range_1[1]):
        return True
    if(range_2[0] <= range_1[0] <= range_2[1]):
        return True
    if(range_2[0] <= range_1[1] <= range_2[1]):
        return True
    return False

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