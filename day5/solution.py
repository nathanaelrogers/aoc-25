from time import perf_counter_ns
start = perf_counter_ns()

from heapq import heappop, heappush

with open('input.txt') as file:
    lines = file.readlines()
    
    ranges = []
    ids = []

    ranges_done = False
    for l in lines:
        if l == '\n':
            ranges_done = True
            continue

        if ranges_done:
            heappush(ids, int(l))
        else:
            r = tuple(map(int, l.strip().split('-')))
            heappush(ranges, r)

# Part 1

def part_1(ranges, ids):
    res = 0
    cur_start, cur_end = heappop(ranges)
    cur_id = heappop(ids)

    while cur_start:
        # if there are further ranges we need to check for overlap
        if ranges:
            next_start, next_end = heappop(ranges)

            # the next range starts inside the current one, so it overlaps
            if next_start <= cur_end:
                cur_end = max(cur_end, next_end)
                continue

        # if we're not overlapping we can run through all the ids up to the end
        while cur_id:
            # print(f'examining id {cur_id}')

            if cur_id > cur_end:
                break

            if cur_id >= cur_start:
                res += 1

            cur_id = heappop(ids) if ids else None
        
        # if there are ranges left to check we update before iterating
        if not ranges:
            break
        else:
            cur_start, cur_end = next_start, next_end

    return res

print('part 1:', part_1(ranges.copy(), ids.copy()))

# Part 2

def part_2(ranges):
    res = 0
    cur_start, cur_end = heappop(ranges)

    while cur_start:
        # if there are further ranges we need to check for overlap
        if ranges:
            next_start, next_end = heappop(ranges)

            # the next range starts inside the current one, so it overlaps
            if next_start <= cur_end:
                cur_end = max(cur_end, next_end)
                continue

        res += cur_end - cur_start + 1
        
        # if there are ranges left to check we update before iterating
        if not ranges:
            break
        else:
            cur_start, cur_end = next_start, next_end
    
    return res

print('part 2:', part_2(ranges.copy()))

end = perf_counter_ns()

print(f'time: {(end - start) / 1E6}')