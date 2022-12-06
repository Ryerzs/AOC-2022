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
            # print(len(row))
            # print(row)
            data.append(row)
    return data

def priority_for_character(character):
    upper_priority =  26*character.isupper()
    return ord(character.lower()) - ord('a') + 1 + upper_priority
    
def star1(data):
    compartments = [(row[0:len(row)//2], row[len(row)//2:len(row)]) for row in data]
    intersect_characters = [set(compartment[0]).intersection(compartment[1]).pop() for compartment in compartments]
    priority = sum([priority_for_character(character) for character in intersect_characters])
    return priority

def star2(data):
    badge_priority = 0
    for i in range(0, len(data), 3):
        badge = set(data[i]).intersection(data[i+1]).intersection(data[i+2]).pop()
        badge_priority += priority_for_character(badge)
    return badge_priority

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