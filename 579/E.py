n = int(input())
A = list(map(int, input().split()))

A.sort()

MAX_WEIGHT = 150001

k = 0
count = 0
for i in range(1, MAX_WEIGHT+1):
    if k >= len(A):
        break
    boxer = A[k]
    if i < boxer - 1:
        i += boxer - 2
        continue

    while i > boxer + 1 and k < len(A) - 1:
        k += 1
        boxer = A[k]

    if i == boxer or i == boxer - 1 or i == boxer + 1:
        count += 1
        k += 1

print(count)