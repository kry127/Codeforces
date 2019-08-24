from collections import deque

def substr_idx(s, t, reverse=False):
    idx = deque()
    i = 0
    rng = range(len(s))
    if reverse:
        rng = reversed(rng)
    for k in rng:
        if i >= len(t):
            break

        if reverse and s[k] == t[-i-1]:
            idx.appendleft(k)
            i += 1
        elif not reverse and s[k] == t[i]:
            idx.append(k)
            i += 1

    return idx

s = input()
t = input()

idleft = substr_idx(s, t)
idright = substr_idx(s, t, reverse=True)

m = max(idright[0], len(s) - idleft[-1] - 1)

for i in range(1, len(idleft)):
    m = max(m, idright[i]-idleft[i-1]-1)

print(m)