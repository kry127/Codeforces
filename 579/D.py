s = input()
t = input()

low_id = s.find(t)

low = max(low_id, len(s) - low_id - len(t))

high_id = s[::-1].find(t[::-1])

high = max(high_id, len(s) - high_id - len(t))

print(max(low, high))