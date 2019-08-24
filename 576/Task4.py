# inspired by https://codeforces.com/contest/1198/submission/58086142
# Use PyPy 3.6! It has JIT compiler!

def main():
    T = int(input())
    
    v_cover = set()
    for _ in range(T):
        n, m = map(int, input().split())
        v_count = 3*n
        v_cover.clear()
        i_cover = []
        for k in range(m):
            edge = list(map(int, input().split()))
            if edge[0] not in v_cover and edge[1] not in v_cover:
                v_cover.add(edge[0])
                v_cover.add(edge[1])
                i_cover.append(k+1)
                if len(i_cover) == n:
                    print('Matching')
                    print(*i_cover[:n])
                    for _ in range(k+1, m):
                        input()
                    break
    
        if len(i_cover) < n:
            #v_independent = set(range(1, v_count+1)) - v_cover
            v_independent = []
            for vert in range(1, 3*n+1):
                if vert not in v_cover:
                    v_independent.append(vert)
                if len(v_independent) == n:
                    print('IndSet')
                    #print(*random.sample(v_independent, n))
                    print(*v_independent)
                    break
    
            if len(v_independent) < n:
                print('Impossible')

# preamble
import sys
input=sys.stdin.readline #crucial for speedup

# main call
if __name__== "__main__":
    main()