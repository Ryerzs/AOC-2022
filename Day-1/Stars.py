import time

def day_1():
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
    calories_elves = []
    with open(path) as f:
        calories_current_elf = []
        rows = f.read().splitlines()
        for row in rows:
            if row == '':
                calories_elves.append(calories_current_elf)
                calories_current_elf = []
                continue
            calories_current_elf.append(int(row))
    calories_elves.append(calories_current_elf)
    return calories_elves
    
def star1(calories_elves):
    calorie_sum_elves = [sum(calorie for calorie in elf_inventory) for elf_inventory in calories_elves]
    return max(calorie_sum_elves)

def star2(calories_elves):
    calorie_sum_elves = [sum(calorie for calorie in elf_inventory) for elf_inventory in calories_elves]
    calorie_sum_elves.sort(key=lambda x: -x)
    sum_top_three = sum(calorie_sum_elves[0:3])
    return sum_top_three

def main():
    import cProfile
    import pstats
    with cProfile.Profile() as pr:
        day_1()
    
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename = 'profiling.prof')

if __name__ == '__main__':
    main()