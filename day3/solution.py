with open('input.txt') as file:
    banks = [x.strip() for x in file.readlines()]

# Part 1

def joltage_1(bank: str):
    l, r = 0, 1
    max = int(bank[l] + bank[r])

    while r < len(bank):
        l_char = bank[l]
        r_char = bank[r]

        if int(r_char) > int(l_char):
            l = r

        if int(l_char + r_char) > max:
            max = int(l_char + r_char)

        r += 1

    return max

res = 0
for bank in banks:
    res += joltage_1(bank)

print('part 1:', res)

# Part 2

def drop_one(num_str):
    for i in range(12):
        yield num_str[:i] + num_str[i+1:]

def joltage_2(bank):
    max_str = bank[:12]

    for ch in bank[12:]:
        for alt_str in drop_one(max_str):
            if int(alt_str + ch) > int(max_str):
                max_str = alt_str + ch

    return int(max_str)

res = 0
for bank in banks:
    res += joltage_2(bank)

print('part 2:', res)