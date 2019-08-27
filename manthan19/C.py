n = int(input())

assert n % 4 == 0

nh = n // 2

for U in [0, 1]:
    for i in range(nh):
        for V in [0, 1]:
            for j in range(nh):
                print(((i*nh + j) << 2) + U + 2*V, end=" ")
        print()

exit(0)