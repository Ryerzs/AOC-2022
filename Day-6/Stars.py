import time
from collections import defaultdict

def day_():
    path = "data.txt"
    # path = "test-data.txt"

    start_time = time.perf_counter()
    data = get_data(path)

    time1 = time.perf_counter()

    ans1 = star1(data, 4)
    time2 = time.perf_counter()

    ans2 = star1(data, 14)
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
            data.append(r)
    return data
    
def star1(data, number_search):
    number_search -= 1
    characters = 0
    for row in data:
        stack = {}
        for i in range(number_search):
            if row[i] in stack:
                stack[row[i]] += 1
            else:
                stack[row[i]] = 1
        for i, (char_start, char_end) in enumerate(zip(row[0:-number_search], row[number_search:])):
            if char_end in stack:
                stack[char_end] += 1
            else:
                stack[char_end] = 1

            if len(stack.keys()) == sum([occurrences for occurrences in stack.values()]):
                characters += number_search + i+1
                print(number_search + i+1)
                break

            stack[char_start] -= 1
            if (stack[char_start] == 0):
                stack.pop(char_start, None)
    return characters

def default_value():
    return 0


def star2(data):
    return 0

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