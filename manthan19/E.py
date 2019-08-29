from collections import deque

class MaxQueue:
    def __init__(self):
        self.p = list()
        self.q = list()
        pass

    def __len__(self):
        return len(self.p) + len(self.q)

    def __add__(self, other):
        return self.enqueue(other)

    def enqueue(self, other):
        min_val = other if len(self.p) == 0 else max(other, self.p[-1][1])
        self.p.append((other, min_val))

    def dequeue(self):
        if len(self.q) == 0:
            while len(self.p) > 0:
                item = self.p.pop()[0]
                min_val = item if len(self.q) == 0 else max(item, self.q[-1][1])
                self.q.append((item, min_val))

        if len(self.q) > 0:
            return self.q.pop()[0]

    def max(self):
        if len(self) == 0:
            return None
        if len(self.p) == 0:
            return self.q[-1][1]
        elif len(self.q) == 0:
            return self.p[-1][1]
        else:
            return max(self.p[-1][1], self.q[-1][1])

class MaxWindowedQueue(MaxQueue):
    def __init__(self, wnd_size):
        super().__init__()
        self.wnd_size = wnd_size

    def enqueue(self, other):
        super().enqueue(other)
        if len(self) > self.wnd_size:
            return super().dequeue()

def max_of_window(A, wnd):
    mwq = MaxWindowedQueue(wnd)
    ret = list()
    mwq.enqueue(0)

    for elm in A:
        mwq.enqueue(elm)
        ret.append(mwq.max())
    last_max = mwq.max()
    for _ in range(wnd - 1):
        mwq.enqueue(0)
        if len(mwq) > 1:
            last_max = mwq.max()
        ret.append(last_max)
    return ret


def main():
    n, w = map(int, input().split())
    A = [0] * w
    for _ in range(n):
        arr = deque(map(int, input().split()))
        wnd = w - arr.popleft() + 1
        if wnd > 1:
            # lr
            max_suffix = max_of_window(arr, wnd)

            for i in range(w):
                A[i] += max_suffix[i]
        else:
            for i in range(w):
                A[i] += arr[i]

    print(*A)


import sys

input = sys.stdin.readline
if __name__ == "__main__":
    main()