import time
import sys
from collections import deque
import heapq

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
    nodes = {}
    edges = {}
    start_node = None
    end_node = None
    count = 0
    with open(path) as f:
        rows = f.read().splitlines()
        height = len(rows)
        for row_nr, row in enumerate(rows):
            width = len(row)
            for col_nr, c in enumerate(row):
                add_neighbors(edges, row_nr, col_nr, height, width)
                current = row_nr*width + col_nr
                if c == "S":
                    start_node = current
                    c = "a"
                if c == "E":
                    end_node = current
                    c = "z"
                nodes[row_nr*width + col_nr] = ord(c) - 97
                count += 1
    counter = {2:0, 3:0, 4:0}
    for node in nodes:
        counter[len(edges[node])] +=1
    print(counter)
    print(4, (height-2)*2 + (width -2)*2, (width-2)*(height-2))
    return nodes, edges, start_node, end_node

def add_neighbors(edges, row_nr, col_nr, height, width):
    neighbors = get_possible_neighbors(row_nr, col_nr, height, width)
    current = row_nr*width + col_nr
    if current not in edges:
        edges[current] = []
    for n in neighbors:
        if n not in edges:
            edges[n] = []
        if n in edges[current]:
            continue
        edges[current].append(n)
        edges[n].append(current)

def get_possible_neighbors(row_nr, col_nr, height, width):
    neighbors = []
    if col_nr > 0:
        neighbors.append(row_nr*width + col_nr-1)
    if col_nr < width - 1:
        neighbors.append(row_nr*width + col_nr+1)
    if row_nr > 0:
        neighbors.append((row_nr-1)*width + col_nr)
    if row_nr < height - 1:
        neighbors.append((row_nr+1)*width + col_nr)
    return neighbors
    
def star1(data):
    nodes, edges, start_node, end_node = data
    edges = remove_too_big_jumps(nodes, edges)
    print("Beginning Dijkstras...")
    val = dijkstras(nodes, edges, start_node, end_node)
    return val

def remove_too_big_jumps(nodes, edges):
    new_edges = {}
    for node in nodes.keys():
        new_edges[node] = []
    for node, val in nodes.items():
        for neighbor in edges[node]:
            if val >= nodes[neighbor] - 1:
                new_edges[node].append(neighbor)
    return new_edges

def dijkstras(nodes, edges, start_node, end_node, find_a = False):
    value_of_nodes = {}
    for node in nodes.keys():
        value_of_nodes[node] = sys.maxsize

    value_of_nodes[start_node] = 0
    visited = []
    unvisited = [(0,start_node)]
    heapq.heapify(unvisited)
    current_node = start_node
    print(unvisited)

    while len(unvisited) > 0:
        (_, current_node) = heapq.heappop(unvisited)
        # print(_*-1)
        #print(current_node, end_node)
        if current_node in visited:
            # print("skip")
            continue
        if find_a and nodes[current_node] == 25:
            print(value_of_nodes[current_node])
            return value_of_nodes[current_node]
        elif current_node == end_node:
            # print(visited)
            print(value_of_nodes[end_node])
            return value_of_nodes[end_node]
        visited.append(current_node)
        for neighbor in edges[current_node]:
            value_of_nodes[neighbor] = min(value_of_nodes[neighbor], value_of_nodes[current_node] + 1)
            # diff = nodes[neighbor] - nodes[current_node]
            # if diff > 0:
            #     print(diff)
            if neighbor not in visited:
                heapq.heappush(unvisited, (value_of_nodes[neighbor], neighbor))
                # unvisited.append(neighbor)
    return sys.maxsize

def star2(data):
    nodes, edges, start_node, end_node = data
    for node, val in nodes.items():
        nodes[node] = 25 - val
    edges = remove_too_big_jumps(nodes, edges)
    print("Beginning Dijkstras...")
    return dijkstras(nodes, edges, end_node, 0, find_a = True)

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