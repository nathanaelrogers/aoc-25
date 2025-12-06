import time
start = time.perf_counter_ns()

from functools import reduce
from operator import mul, add

OPS_MAP = {'*' : mul, '+' : add}

with open('input.txt') as file:
    lines = [l for l in file.readlines()]
    ch_grid  = [[ch for ch in l[:-1]] for l in lines[:-1]]
    operations = list(map(lambda op_str: OPS_MAP[op_str], lines[-1].split()))

ROWS, COLS = len(ch_grid), len(ch_grid[0])

# Part 2

cols = []
for c in range(COLS):
    cols.append(''.join([ch_grid[r][c] for r in range(ROWS)]).strip())

results = []
pos = 0
for op in operations:
    operands = []
    while pos < len(cols) and cols[pos] != '':
        operands.append(cols[pos])
        pos += 1
    pos += 1

    if operands:
        results.append(reduce(op, map(int, operands)))

print(f'part 2: {sum(results)}')

end = time.perf_counter_ns()
print(f'time: {(end - start) / 1E6}')