def solution(operations):
    import heapq
    lst = []
    
    T = len(operations)
    for t in range(T):
        if operations[t][0] == "I":
            heapq.heapify(lst)
            heapq.heappush(lst, int(operations[t][2:]) )
        elif operations[t][0] == "D":
            if (operations[t][2] == "-") & (len(lst) > 0):
                heapq.heapify(lst)
                heapq.heappop(lst)
            elif (operations[t][2] != "-") & (len(lst) > 0):
                heapq._heapify_max(lst)
                heapq._heappop_max(lst)
    
    if len(lst) == 0: lst = [0, 0]
    heapq.heapify(lst)
    m = heapq.heappop(lst)

    heapq._heapify_max(lst)
    M = heapq._heappop_max(lst)

    answer = [M, m]

    return answer

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))
