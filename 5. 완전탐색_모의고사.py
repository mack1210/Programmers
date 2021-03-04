def solution(answers):
    import math

    n = len(answers)
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    lst = []
    T = len(patterns)
    for t in range(T):
        pattern = patterns[t]
        p = len(answers) / len(pattern)
        if p > 1:
            ex = lambda x: x*(math.ceil(p))
            pattern = ex(pattern)[:n]
        elif p < 1:
            pattern = pattern[:n]
        
        cnt = 0
        for x, y in zip(pattern, answers):
            if x == y:
                cnt += 1
        
        lst.append(cnt)

    answers = []
    for i in range(T):
        if lst[i] == max(lst):
            answers.append(i+1)

    return answers

answers = [1,3,2,4,2]

print(solution(answers))


