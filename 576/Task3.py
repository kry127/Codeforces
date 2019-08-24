from collections import deque

n = int(input())
money = list(map(int, input().split()))
money_t = [0]*len(money) # moments of last money change
x_list = [] # subsidion of government

# processing queries
q = int(input())
for q_ind in range(q):
    line = list(map(int, input().split()))
    if line[0] == 2:
        x = line[1]
        x_list.append(x)
    if line[0] == 1:
        _, p, mon = line
        money[p-1] = mon
        money_t[p-1] = len(x_list)

# calculating max suffixes of x_list subsidion
x_list_suffix = deque()
max_suff = 0
x_list_suffix.appendleft(max_suff) # zero at the beginning
for k in reversed(range(len(x_list))):
    max_suff = max(max_suff, x_list[k])
    x_list_suffix.appendleft(max_suff)

# last loop
for k in range(len(money)):
    money[k] = max(money[k], x_list_suffix[money_t[k]])


print(*money)
