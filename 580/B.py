def main():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    coins = 0
    sign = 1 # 1 -- plus, 0 -- minus
    sign_defined = False
    for elm in A:
        if elm > 1:
            coins += elm - 1
        elif elm <= -1:
            coins += -1 - elm
            sign = 1 - sign
        elif elm == 0:
            coins += 1
            sign_defined = True

    if sign_defined == False and sign == 0:
        coins += 2

    print(coins)

    pass


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    main()