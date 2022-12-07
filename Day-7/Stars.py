import time

def day_():
    path = "Day-7/data.txt"
    # path = "Day-7/test-data.txt"

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
        instruction = []
        output = []

        for r in rows:
            if r[0] == '$':
                if instruction != []:
                    instruction.append(output)
                    data.append(instruction)
                    instruction = []
                    output = []
                instruction.append(r[2:])
            else:
                output.append(r)
        instruction.append(output)
        data.append(instruction)
        instruction = []
        output = []
    return data

    
def star1(data):
    #cd ..
    #cd /
    #cd x
    #ls
    #dir
    # print(data)
    directories = {}
    current_directory = []
    for iteration, instruction in enumerate(data):
        # print(current_directory)
        operation = instruction[0]
        output = instruction[1]
        if operation[0:2] == 'cd':
            if operation[3:] == '..':
                current_directory = current_directory[0:-1]
            else:
                current_directory.append(operation[3:])
                directory_name = '-'.join(current_directory)
                if directory_name not in directories:
                    directories[directory_name] = Directory(directory_name, [])
        if operation == 'ls':
            directory_name = '-'.join(current_directory)
            directory = directories[directory_name]
            for out in output:
                if out[0:3] == 'dir':
                    child_name = directory_name + '-' + out[4:]
                    if child_name not in directories:
                        new_child = Directory(child_name, [])
                        directories[child_name] = new_child
                    else:
                        new_child = directories[child_name]
                else:
                    info = out.split(' ')
                    child_name = directory_name + '-' + info[1]
                    new_child = File(child_name, info[0])
                    # print(info)
                directory.children.append(new_child)
    sizes = []
    for direc in directories.values():
        # print(direc.name)
        # print(direc.get_size())
        sizes.append(direc.get_size())
    total_size = max(sizes)
    # print(total_size)
    space_needed = 30000000 + total_size - 70000000
    print(space_needed)
    sizes_viable = [size for size in sizes if size >= space_needed]
    print(min(sizes_viable))


    sizes.append(sum(sizes))
    sizes_under_1000 = [size for size in sizes if size <=100000]
    return sum(sizes_under_1000)

class File():
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
    
    def get_size(self):
        return int(self.size)

    def __str__(self):
        return str(self.name) + ' ' + str(self.size)

class Directory():
    def __init__(self, name, children=[]):
        self.finished = False
        self.name = name
        self.children = list(children)
        self.size = 0

    def __str__(self):
        out = self.name + '-['
        for child in self.children:
            out = out + child.name + ', '
        out = out + ']'
        return out
    
    def get_size(self):
        size = 0
        for child in self.children:
            size += child.get_size()
        return size


def get_dir_size(dir, instruction, iteration):
    pass

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