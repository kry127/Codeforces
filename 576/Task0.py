n, x, y = map(int, input().split())
a = list(map(int, input().split()))

m = -1
m_id = None
y_count = 0
for k in range(n):
    if a[k] < m or m_id is None:
        m = a[k]
        m_id = k
        y_count = 0
        if y == 0:
            break
    else:
        y_count += 1
        if y_count == y:
            break

print(m_id + 1)

