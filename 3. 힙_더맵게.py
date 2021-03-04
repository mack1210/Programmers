import heapq

def solution(scoville, K):
    i = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
            i += 1
        else:
            return -1
    return i

scoville = [1, 2, 3, 9, 10, 12]	
K = 7

print(solution(scoville, K))
