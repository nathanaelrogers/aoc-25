from itertools import accumulate
from operator import mul, add

OPS_MAP = {'*' : mul, '+' : add}

with open('sample.txt') as file:
    lines = [l.strip() for l in file.readlines()]
    num_grid = [list(map(int, l.split())) for l in lines[:-1]]
    operations = list(map(lambda op_str: OPS_MAP[op_str], lines[-1].split()))

ROWS, COLS = len(num_grid), len(num_grid[0])

# Part 1 

results = []
for c in range(COLS):
    operands = [num_grid[r][c] for r in range(ROWS)]
    results.append(list(accumulate(operands, operations[c]))[-1])

print(f'part 1: {sum(results)}')