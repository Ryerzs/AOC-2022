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
    rounds = []
    with open(path) as f:
        rows = f.read().splitlines()
        for r in rows:
            moves = r.split(sep=' ')
            moves = (ord(moves[0]) - ord('A'), ord(moves[1]) - ord('X'))
            rounds.append(moves)
    return rounds
    
"""
rounds = [(0,1), (1,0), (2, 2)] <=> [(A,Y), (B,X), (C,Z)]
Outcome of match for a set of moves is
(my_move - opponents_move + 1) mod 3
where 0 is a loss, 1 is a draw, 2 is a win
"""
def star1(rounds):
    score = sum([1 + moves[1] + 3*((moves[1]-moves[0]+1)%3) for moves in rounds])
    return score

"""
rounds = [(0,1), (1,0), (2, 2)] <=> [(A,Y), (B,X), (C,Z)]
Solve for my move in the equation
  (my_move - opponents_move + 1) = outcome (mod 3)
=>my_move = opponents_move + outcome - 1 (mod 3)
where 0 is rock, 1 is paper, 2 is scissors
"""
def star2(rounds):
    score = sum([1 + 3*moves[1] + ((moves[1]+moves[0]-1)%3) for moves in rounds])
    return score

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