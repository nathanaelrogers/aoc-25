from time import perf_counter_ns
start = perf_counter_ns()

from itertools import combinations
from math import sqrt
from heapq import heappush, heappop
from operator import mul
from functools import reduce

with open('input.txt') as file:
    boxes = list(enumerate([tuple(map(int, l.strip().split(','))) for l in file.readlines()]))

BOX_COUNT = len(boxes)

def dist(a_val, b_val):
    total = 0
    for i in range(len(a_val)):
        total += (a_val[i] - b_val[i]) ** 2
    return sqrt(total)

distances = []
for a, b in combinations(boxes, 2):
    a_id, a_val = a
    b_id, b_val = b
    heappush(distances, (dist(a_val, b_val), a_id, b_id))

connected = dict()
for id, val in boxes:
    #               (owner, size)
    connected[id] = (id, 1)

def chase(start_id):
    owner_id, size = connected[start_id]

    while size == 0:
        owner_id, size = connected[owner_id]

    return owner_id

def part1(d):
    sizes = []
    for eid, size in d.values():
        heappush(sizes, -size)

    print(f'part 1: {reduce(mul, [-heappop(sizes) for _ in range(3)])}')
    return

def part2(a, b):
    a_id, (a_x, a_y, a_z) = boxes[a]
    b_id, (b_x, b_y, b_z) = boxes[b]

    print(f'part 2: {a_x * b_x}')
    return

count = 0
while distances:
    count += 1
    if count == 1000:
        part1(connected.copy())

    d, a, b = heappop(distances)
    a_eid, b_eid = chase(a), chase(b)

    if a_eid == b_eid:
        continue

    upper = max(a_eid, b_eid)
    lower = min(a_eid, b_eid)

    u_id, u_size = connected[upper]
    connected[upper] = (lower, 0)

    l_id, l_size = connected[lower]
    new_size = l_size + u_size
    if new_size == BOX_COUNT:
        part2(a, b)
    else:
        connected[lower] = (l_id, new_size)

end = perf_counter_ns()
print(f'time: {(end - start) / 1E6}')