n, m = map(int, input().split())

answ = [input() for _ in range(n)]

weights = list(map(int, input().split()))

total = 0
for task in range(m):
    task_score = {}
    for student in range(n):
        answer = answ[student][task]
        if answer not in task_score:
            task_score[answer] = 0
        task_score[answer] += 1

    total += max(task_score.values())*weights[task]

print(total)
