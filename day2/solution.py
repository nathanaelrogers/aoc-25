from itertools import batched

def parse_range(string):
    start, end = string.split('-')
    return (int(start), int(end))

with open('input.txt') as file:
    ranges = list(map(parse_range, file.read().split(',')))

# Part 1

res = []

for start, end in ranges:
    for id in map(str, range(start, end+1)):
        id_len = len(id)

        if id_len % 2 != 0:
            continue

        if id[id_len // 2:] != id[:id_len // 2]:
            continue
        
        res.append(int(id))

print('part 1:', sum(res))

#  Part 2

res = []

def check_invalid_id(id):
    win_size = len(id) // 2

    while win_size > 0:
        id_invalid = True
        pattern = id[:win_size]

        for slice in batched(id[win_size:], n=win_size):
            slice = ''.join(slice)

            if slice != pattern:
                id_invalid = False
                break

        if id_invalid:
            return True
        
        win_size -= 1
    
    return False

for start, end in ranges:
    for id in map(str, range(start, end+1)):
        if check_invalid_id(id):
            res.append(int(id))

print('part 2:', sum(res))
        