import itertools
import math

def solution(numbers):

    numbers = list(map(str, [i for i in numbers]))
    lst = []
    for i in range(len(numbers)):
        lst.extend(list(map(''.join, itertools.permutations(numbers, i+1))))
    lst = list(set(map(int, lst)))

    answer = 0
    n = len(lst)
    for i in range(n):
        cnt = 0
        m = int(lst[i])
        if m == 1 or m == 0:
            cnt += 1
        else:
            for j in range(2, math.floor(m**0.5)+1):
                if m % j == 0:
                    cnt += 1
                    break
        if cnt == 0:
            answer += 1
    return answer

numbers	= "011"

print(solution(numbers))