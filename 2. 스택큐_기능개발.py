import math

def solution(progresses, speeds):
    day_remained = []
    day_remained = [math.ceil((100-a) / b) for a, b in zip(progresses,speeds)]

    lst = []
    front = 0
    n = len(progresses)
    for idx in range(n):
        if day_remained[front] < day_remained[idx]:
            lst.append(idx - front)
            front = idx
    lst.append(len(day_remained) - front)
    return lst

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))