
def canBuildRectangles(A):
    A.sort()

    # check pairs
    B = []
    for i in range(0, len(A), 2):
        if A[i] == A[i+1]:
            B.append(A[i])
            i += 1
        else:
            return False

    # check for equal area
    area = B[0]*B[-1]
    for i in range(1, len(B) // 2):
        if B[i] * B[-i-1] != area:
            return False
    
    return True


q = int(input())

for _ in range(q):
    n = int(input())
    rect = list(map(int, input().split()))
    assert 4*n == len(rect)


    isch = canBuildRectangles(rect)
    print("YES" if isch else "NO")