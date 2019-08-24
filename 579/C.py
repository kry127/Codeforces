import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

primecount = 1
def factorize(a):
    global primecount
    primecount = 1

    def _factorize(a):
        global primecount
        till = int(math.sqrt(a)) + 1

        for i in range(2, till+1):
            cnt = 1
            while a % i == 0:
                a = a // i
                cnt += 1
            primecount *= cnt
            if cnt > 1:
                return a
        primecount *= 2
        return 1

    while (a > 1):
        a = _factorize(a)

    return primecount


n = int(input())
arr = list(map(int, input().split()))

assert n == len(arr)

g = arr[0]
for i in range(1, n):
    g = gcd(g, arr[i])

print(factorize(g))