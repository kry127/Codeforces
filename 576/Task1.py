H, L = map(int, input().split())
if H <= 0.000001:
    print('0')
else:
    print((L*L - H*H)/(2*H))