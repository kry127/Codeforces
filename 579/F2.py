n, r = map(int, (input().split()))

proj_list = []
for _ in range(n):
    a, b = map(int, input().split())
    proj_list.append([b, a, True])

def check(proj_list):
    global r

    proj_count = 0
    while len(proj_list) > 0:
        i = 0
        while True:
            if i == len(proj_list):
                return proj_count

            proj = proj_list[i]
            if r >= proj[1] and proj[2]:
                proj[2] = False
                r += proj[0]
                if r < 0:
                    return proj_count
                proj_count += 1
                break
            i += 1


#proj_list.sort(reverse=True)
raise_mmr = filter(lambda x: x[0] >= 0, proj_list)
hard_work = filter(lambda x: x[0] < 0, proj_list)
proj_list = sorted(raise_mmr, key=lambda x: x[0], reverse=True) + sorted(hard_work, key=lambda x: x[1] + x[0], reverse=True)

print(check(proj_list))
