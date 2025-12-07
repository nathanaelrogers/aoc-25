from time import perf_counter_ns
start = perf_counter_ns()

from collections import defaultdict

with open('input.txt') as file:
    grid = [l.strip() for l in file.readlines()]

ROWS, COLS = len(grid), len(grid[0])

s_pos = 0
for i in range(COLS):
    if grid[0][i] == 'S':
        s_pos = i
        break

#  Part 1

beam_pos = {s_pos}
split_count = 0

for r in range(1, ROWS):
    for pos in beam_pos.copy():
        if grid[r][pos] == '^':
            split_count += 1
            beam_pos.remove(pos)
            if pos - 1 >= 0:
                beam_pos.add(pos - 1)
            if pos + 1 < COLS:
                beam_pos.add(pos + 1)

print(f'part 1: {split_count}')

# Part 2
    
beam_pos = defaultdict(int)
beam_pos[s_pos] += 1

for r in range(1, ROWS):
    for pos in beam_pos.copy():
        if grid[r][pos] == '^':
            if pos - 1 >= 0:
                beam_pos[pos - 1] += beam_pos[pos]
            if pos + 1 < COLS:
                beam_pos[pos + 1] += beam_pos[pos]
            beam_pos[pos] = 0

print(f'part 2: {sum(beam_pos.values())}')

end = perf_counter_ns()
print(f'time: {(end - start) / 1E6}')