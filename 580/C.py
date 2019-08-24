def main():
    n = int(input())
    if n % 2 == 0:
        print("NO")
        return

    A = [0]*(2*n)
    i = 0
    k = 1
    while k < 2*n:
        A[i] = k
        k += 1
        i = (i + n) % (2*n)
        A[i] = k
        k += 1
        i -= 1

    print("YES")
    print(*A)
    pass


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    main()