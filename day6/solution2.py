import time
start = time.perf_counter_ns()

from functools import reduce
from operator import mul, add

OPS_MAP = {'*' : mul, '+' : add}

with open('input.txt') as file:
    lines = [l for l in file.readlines()]
    num_grid = [list(map(int, l.strip().split())) for l in lines[:-1]]
    ch_grid  = [[ch for ch in l[:-1]] for l in lines[:-1]]
    operations = list(map(lambda op_str: OPS_MAP[op_str], lines[-1].split()))

ROWS, COLS = len(num_grid), len(num_grid[0])

# Part 2
def process_operands(depth, raw_operands):
    width = len(str(max(raw_operands)))

    new_operands = []
    for c in range(depth[0], depth[0] + width):
        new_operands.append(int(''.join(ch_grid[r][c] for r in range(ROWS)).strip()))

    depth[0] += width + 1
    return new_operands

results = []
depth = [0]
for c in range(COLS):
    operands = process_operands(depth, [num_grid[r][c] for r in range(ROWS)])
    results.append(reduce(operations[c], operands))

print(f'part 2: {sum(results)}')

end = time.perf_counter_ns()
print(f'time: {(end - start) / 1E6}')