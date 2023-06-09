import time

from collections import deque

def day_():
    path = "data.txt"
    #path = "test-data.txt"

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
    with open(path) as f:
        rows = f.read().splitlines()
        monkeys = []
        for i, row in enumerate(rows):
            if i%7 == 1:
                starting = deque([int(s) for s in row.replace("  Starting items: ", "").split(", ")])
            if i%7 == 2:
                op = row.replace("  Operation: new = old ", "").split(" ")
                if op[1] == "old":
                    op[0] = "^"
                    op[1] = 2
                else:
                    op[1] = int(op[1])
            if i%7 == 3:
                div = int(row.replace("  Test: divisible by ", ""))
            if i%7 == 4:
                case_true = int(row.replace("    If true: throw to monkey ", ""))
            if i%7 == 5:
                case_false = int(row.replace("    If false: throw to monkey ", ""))
            if i%7 == 6:
                monkeys.append({"id": i//7, "starting": starting, "op": op, "div":div, "case_true": case_true, "case_false":case_false})
        # for m in monkeys:
        #     print(m)
    return monkeys
    
def star1(data):
    data = make_modulo_list(data)
    counter = {}
    for m in range(len(data)):
        counter[m] = 0
    for _ in range(20):
        for m in data:
            counter[m["id"]] += len(m["starting"])
            while len(m["starting"])>0:
                item = m["starting"].popleft()
                item = get_new_worry(item, m)
                throw_to = get_next_monkey(item[m["div"]], m)
                data[throw_to]["starting"].append(item)
        # for m in data:
        #     l = []
        #     for s in m["starting"]:
        #         l.append(s[m["div"]])
        #     print(_, ":", m["id"], l)
            
    counter_sort = list(sorted(counter.items(), key=lambda item: -item[1]))
    print(counter)
    return counter_sort[0][1] * counter_sort[1][1]

def make_modulo_list(data):
    divisors = set()
    for m in data:
        divisors.add(m["div"])
    divisors.add(3)
    print(divisors)
    for m in data:
        starting = deque([])
        for item in m["starting"]:
            starting.append({d:item%d for d in divisors})
        m["starting"] = starting
    return data

def get_new_worry(item, m, div_by_three = True):
    new_item = {}
    three_mod = item[3]
    for div, i in item.items():
        if m["op"][0] == "+":
            i += m["op"][1]
        if m["op"][0] == "*":
            i *= m["op"][1]
        if m["op"][0] == "^":
            i = i ** m["op"][1]
        if div_by_three:

            i -= three_mod
        new_item[div] = i % div
    return new_item

def get_next_monkey(item, m):
    if item == 0:
        return m["case_true"]
    else:
        return m["case_false"]

def star2(data):
    counter = {}
    for m in range(len(data)):
        counter[m] = 0
    for _ in range(10000):
        for m in data:
            counter[m["id"]] += len(m["starting"])
            while len(m["starting"])>0:
                item = m["starting"].popleft()
                item = get_new_worry(item, m, False)
                throw_to = get_next_monkey(item[m["div"]], m)
                data[throw_to]["starting"].append(item)
        # if _ % 100 == 0:
        #     print(counter)
    counter_sort = list(sorted(counter.items(), key=lambda item: -item[1]))
    print(counter)
    return counter_sort[0][1] * counter_sort[1][1]

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