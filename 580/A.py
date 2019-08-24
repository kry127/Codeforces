def main():
    # insert your code here
    na = int(input())
    A = set(map(int, input().split()))
    nb = int(input())
    B = set(map(int, input().split()))

    for a in A:
        for b in B:
            s = a + b
            if s not in A and s not in B:
                print("{} {}".format(a, b))
                return


    pass


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    main()