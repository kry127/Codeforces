s = input()
t = input()
s_inv = s[::-1]

low_id = s.find(t)

low = max(low_id, len(s) - low_id - len(t))

high_id = s_inv.find(t[::-1])

high = max(high_id, len(s) - high_id - len(t))

# split t and search substring parts
cycle = max(low, high)
for k in range(1, len(t) - 1):
    tl = t[:k]
    tr = t[:k-1:-1]
    id1 = s.find(tl)
    if id1 == -1:
        continue
    id2 = s_inv.find(tr)
    if id2 == -1:
        continue
    cycle = max(cycle, (len(s) - id2 - len(tr)) - id1 - len(tl))

print(cycle)