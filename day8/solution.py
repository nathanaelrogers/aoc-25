from time import perf_counter_ns
start = perf_counter_ns()

from itertools import combinations
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
    return total

distances = []
for a, b in combinations(boxes, 2):
    a_id, a_val = a
    b_id, b_val = b
    heappush(distances, (dist(a_val, b_val), a_id, b_id))

connected = dict()
for id, val in boxes:
    #               (owner, elements)
    connected[id] = (id, (id,))

def part1(d):
    sizes = []
    for eid, es in d.values():
        heappush(sizes, -len(es))

    print(f'part 1: {reduce(mul, [-heappop(sizes) for _ in range(3)])}')
    return

def part2(a, b):
    print(f'part 2: {boxes[a][1][0] * boxes[b][1][0]}')
    return

count = 0
while distances:
    count += 1
    if count == 1000:
        part1(connected.copy())

    d, a, b = heappop(distances)

    a_owner, a_es = connected[a]
    b_owner, b_es = connected[b]

    if a_owner == b_owner:
        continue

    id1, es1 = connected[a_owner]
    id2, es2 = connected[b_owner]

    for e in es1:
        connected[e] = (id2, ())

    new_es = es2 + es1
    if len(new_es) == BOX_COUNT:
        part2(a, b)
    else:
        connected[b_owner] = (id2, new_es)

end = perf_counter_ns()
print(f'time: {(end - start) / 1E6}')