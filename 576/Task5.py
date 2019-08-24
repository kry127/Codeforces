# Check this solutions:
# cpp: https://codeforces.com/contest/1199/submission/58046178
# py: https://codeforces.com/contest/1199/submission/58081308

from array import array
# https://pythonworld.ru/moduli/modul-array-massivy-v-python.html

def main():
    n = int(input())
    assert (1 <= n <= 50)

    symbol = [" "*(n+1)] + [" " + input() for _ in range(n)]
    field = [[0]*(n + 1) for _ in range(n + 1)]

    # 2D prefix
    for i in range(n):
        for j in range(n):
            field[i+1][j+1] = field[i][j+1] + field[i+1][j] - field[i][j]
            if symbol[i+1][j+1] == "#":
                field[i+1][j+1] += 1

    # Dynamic Programming
    #dp = [[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    #dp = np.zeros((n, n, n, n), np.int16)

    dp = array('I', [0 for _ in range(n*n*n*n)])

    # the cycle for all rectangles
    for i in range(n):
        for j in range(n):
            # i and j is the right bottom corner of rectangle
            # let's look for all subrectangles in left-upper area
            for ii in range(i, -1, -1):
                for jj in range(j, -1, -1):
                    # we've got rectangle (ii, jj) and (i, j)
                    # lets find out, how many hashes ('#') presented in the rectangle
                    hashcount = field[i+1][j+1] - field[ii][j+1] - field[i+1][jj] + field[ii][jj]
                    # this formulae gets all hashes in rectangle (0, 0) (i, j)
                    # then we subtract hashcount from rectangles (0, 0) (ii-1, j) and (0, 0) (i, jj - 1)
                    # then we add (0, 0) (ii-1, jj-1) rectangle hashcount -- this area subtracted twice
                    if hashcount == 0:
                        continue
                        # if no hashes in the rectangle -- nothing to calculate here

                    # let's try to separate rectangle to get smaller value
                    minimal = max(i - ii + 1, j - jj + 1)
                    #separate by rows
                    for k in range(ii, i):
                        #minimal = min(minimal, dp[i][j][k+1][jj] + dp[k][j][ii][jj])
                        minimal = min(minimal, dp[i*n*n*n + j*n*n + (k+1)*n + jj] + dp[k*n*n*n + j*n*n + ii*n + jj])
                    #separate by cols
                    for k in range(jj, j):
                        #minimal = min(minimal, dp[i][j][ii][k+1] + dp[i][k][ii][jj])
                        minimal = min(minimal, dp[i*n*n*n + j*n*n + ii*n + (k+1)] + dp[i*n*n*n + k*n*n + ii*n + jj])
                    # save minimal result
                    dp[i*n*n*n + j*n*n + ii*n + jj] = minimal
                    #print("dp[{}][{}][{}][{}]={}".format(i, j, ii, jj, minimal))

    #print(dp[n-1][n-1][0][0])
    print(dp[(n-1)*n*n*n + (n-1)*n*n])


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    main()