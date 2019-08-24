from collections import Counter, deque
from math import log2

n, I = map(int, input().split())
debug = False

mp3 = list(map(int, input().split()))
assert n == len(mp3)
if n == 0:
    print(0)
    exit(0)

mp3 = sorted(mp3)


bts_avail = I*8 // n

if debug:
    diff = mp3[-1] - mp3[0]
    bits = 0
    pwr2 = 1
    while pwr2 < diff:
        bits += 1
        pwr2 <<= 1


    print('diff: {}'.format(diff))
    print('pwr2: {}'.format(pwr2))
    print('bits: {}'.format(bits))
    print('bts_avail: {}'.format(bts_avail))
    print('rng: {}'.format(rng))


max_range = 0
# your implementation here
window = deque()
wrng = 0
for Ampl, freq in Counter(mp3).items():
    window.append(freq)
    wrng += freq
    if wrng > max_range:
        max_range = wrng
    if (log2(len(window)) == bts_avail):
        wrng -= window.popleft()



print(n - max_range)

