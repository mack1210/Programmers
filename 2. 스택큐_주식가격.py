def solution(prices):
    lst = []
    n = len(prices)
    for i in range(n-1):
        cnt = 0
        for j in range(i+1, n):
            if prices[i] > prices[j]:
                cnt += 1
                break
            else:
                cnt += 1
        lst.extend([cnt])
    lst.extend([0])
    return lst


prices = [1,2,3,3,2]
print(solution(prices))



