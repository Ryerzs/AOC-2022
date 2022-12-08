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
    grid = []
    with open(path) as f:
        rows = f.read().splitlines()
        for row in rows:
            horizontal = []
            for char in row:
                horizontal.append(int(char))
            grid.append(horizontal)
    return grid
    
def star1(grid):
    viable_trees = []
    for i in range(1, len(grid[0])-1):
        for j in range(1, len(grid)-1):
            # print(grid[j][i], j, i)
            if has_viable_direction(grid[j][i], grid, j, i):
                viable_trees.append(grid[j][i])
    viable_trees
    output = len(grid[0]) * len(grid) - len(viable_trees)
    return output

def has_viable_direction(number, grid, j, i):
    found_viable = True
    column = get_column(grid, i)
    # print(column)
    row = get_row(grid, j)
    found_viable = found_viable and check_up(number,    j, column)
    # print(check_up(number,  j, column))
    found_viable = found_viable and check_right(number, i, row)
    # print(check_right(number,  i, column))
    found_viable = found_viable and check_left(number,  i, row)
    # print(check_left(number,  i, column))
    found_viable = found_viable and check_down(number,  j, column)
    # print(check_down(number,  j, column))
    return found_viable

def get_column(grid, i):
    column = []
    for iterator in range(len(grid)):
        column.append(grid[iterator][i])
    return column

def get_row(grid, j):
    row = grid[j]
    return row

def check_up(number: int, i, column):
    out = ''
    for iterator in range(0, i):
        out = out + str(column[iterator])
        if column[iterator] >= number:
            # print(out)
            return True
    # print(out)
    return False
def check_left(number: int, j, row):
    for iterator in range(j+1, len(row)):
        if row[iterator] >= number:
            return True
    return False
def check_right(number: int, j, row):
    for iterator in range(0, j):
        if row[iterator] >= number:
            return True
    return False
def check_down(number: int, i, column):
    for iterator in range(i+1, len(column)):
        if column[iterator] >= number:
            return True
    return False

def star2(grid):
    scenic_scores = []
    for i in range(1, len(grid[0])-1):
        for j in range(1, len(grid)-1):
            # print(grid[j][i], j, i)
            scenic_scores.append(get_scenic_score(grid[j][i], grid, j, i))
    print(scenic_scores)
    return max(scenic_scores)

def get_scenic_score(number, grid, j, i):
    scenic_score = 1
    column = get_column(grid, i)
    # print(column)
    row = get_row(grid, j)
    scenic_score *= scenic_up(number,    j, column)
    # print(scenic_up(number,  j, column))
    scenic_score *= scenic_right(number, i, row)
    # print(scenic_right(number,  i, row))
    scenic_score *= scenic_left(number, i, row)
    # print(scenic_left(number,  i, row))
    scenic_score *= scenic_down(number,    j, column)
    # print(scenic_down(number,  j, column))
    return scenic_score

def get_column(grid, i):
    column = []
    for iterator in range(len(grid)):
        column.append(grid[iterator][i])
    return column

def get_row(grid, j):
    row = grid[j]
    return row

def scenic_up(number: int, i, column):
    scenic_score = 0
    for iterator in range(0, i):
        if column[iterator] >= number:
            scenic_score = 0
        scenic_score += 1
    # print(out)
    return scenic_score
def scenic_left(number: int, j, row):
    scenic_score = 0
    for iterator in range(j+1, len(row)):
        if row[iterator] >= number:
            scenic_score += 1
            return scenic_score
        scenic_score += 1
    return scenic_score
def scenic_right(number: int, j, row):
    scenic_score = 0
    for iterator in range(0, j):
        if row[iterator] >= number:
            scenic_score = 0
        scenic_score += 1
    # print(out)
    return scenic_score
def scenic_down(number: int, i, column):
    scenic_score = 0
    for iterator in range(i+1, len(column)):
        if column[iterator] >= number:
            scenic_score += 1
            return scenic_score
        scenic_score += 1
    return scenic_score

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