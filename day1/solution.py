with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

def right(size:int, pos: int, n: int):
    return (pos + n) % size, (pos + n) // size

def left(size: int, pos: int, n: int):
    # I calculate the number of clicks by imagining I'm going right...
    # so the start position is ((size - pos) % size) + n
    return (pos + (size - n)) % size, (((size - pos) % size) + n) // size

commands = map(lambda l : ((right if l[0] == 'R' else left), int(l[1:])), lines)
size = 100
pos = 50
res1 = 0
res2 = 0

for c in commands:
    rotation_func, rotation_amount = c
    pos, rotations_count = rotation_func(size, pos, rotation_amount)

    if pos == 0:
        res1 += 1
    
    res2 += rotations_count

print('part 1:', res1)
print('part 2:', res2)
