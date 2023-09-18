import time

def day_():
    path = "data.txt"
    path = "test-data.txt"

    start_time = time.perf_counter()
    instructions = get_data(path)

    time1 = time.perf_counter()

    ans1 = star1(instructions)
    time2 = time.perf_counter()

    ans2 = star2(instructions)
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
    instructions = []
    with open(path) as f:
        rows = f.read().splitlines()
        for row in rows:
            new_instruction = [tuple([int(coord) for coord in position.split(",")]) for position in row.split(" -> ")]
            instructions.append(new_instruction)
            print(instructions[-1])
    return instructions
    
def star1(instructions):
    grid = set()
    for instruction in instructions:
        add_line_segment(instruction, grid)
    print(grid)
    max_x = max(grid, key=lambda item: item[0])[0]
    min_x = min(grid, key=lambda item: item[0])[0]
    max_y = max(grid, key=lambda item: item[1])[1]
    min_y = min(grid, key=lambda item: item[1]>3)[1]
    print(min_x, max_x)
    print(min_y, max_y)

    return 0

def add_line_segment(instruction, grid):
    for c1, c2 in zip(instruction[:-1], instruction[1:]):
        add_points_between(c1, c2, grid)

def add_points_between(c1, c2, grid):
    diff_x = c2[0] - c1[0]
    diff_y = c2[1] - c1[1]
    if diff_y == 0:
        sign = int(abs(diff_x)/diff_x)
        for i in range(abs(diff_x)+1):
            grid.add((c1[0]+i*sign, c1[1]))
    elif diff_x == 0:
        sign = int(abs(diff_y)/diff_y)
        for j in range(abs(diff_y)+1):
            grid.add((c1[0], c1[1]+j*sign))

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