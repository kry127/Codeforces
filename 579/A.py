
def isChorovod(lst):
    if len(lst) <= 2:
        return True
    direction = lst[1] - lst[0]
    if direction == len(lst) - 1:
        direction = -1
    elif direction == 1 - len(lst):
        direction = 1

    if direction != 1 and direction != -1:
        return False

    for k in range(2, len(lst)):
        if lst[k] != (lst[k-1] + direction - 1) % len(lst) + 1:
            return False

    return True

q = int(input())

for _ in range(q):
    c = int(input())
    arr = list(map(int, input().split()))
    assert c == len(arr)


    isch = isChorovod(arr)
    print("YES" if isch else "NO")
