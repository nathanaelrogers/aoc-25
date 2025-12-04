with open('input.txt') as file:
    grid = [[ch for ch in line.strip()] for line in file.readlines()]

ROWS, COLS = len(grid), len(grid[0])
DIRECTIONS = ((1, 0), (0, -1), (-1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1))

def contains_roll(r, c):
    if (r >= ROWS or r < 0 or c >= COLS or c < 0):
        return False

    return grid[r][c] == '@'

prox = dict()
for i in range(4, 9):
    prox[i] = set()

accessible = set()

res = 0
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == '@':
            num_adjacent = sum([1 if contains_roll(i + dx, j + dy) else 0 for dx, dy in DIRECTIONS])
            if num_adjacent < 4:
                accessible.add((i, j))
            else:
                prox[num_adjacent].add((i, j))

print('part 1:', len(accessible))

# Part 2

res = 0
while accessible:
    x, y = accessible.pop()
    res += 1

    for dx, dy in DIRECTIONS:
        r, c = x + dx, y + dy

        if (r < 0 or r >= ROWS or c < 0 or c >= COLS):
            continue

        if (r, c) in prox[4]:
            prox[4].remove((r, c))
            accessible.add((r, c))
            continue

        for i in range(5, 9):
            if (r, c) in prox[i]:
                prox[i].remove((r, c))
                prox[i - 1].add((r, c))


print('part 2:', res)