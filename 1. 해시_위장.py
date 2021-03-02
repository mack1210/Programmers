from collections import Counter

def solution(clothes):
    answer = 0
    hash_map = {}

    # 키 초기화
    for clothe in clothes: hash_map[clothe[1]] = []
    for clothe in clothes: hash_map[clothe[1]].append(clothe[0])
    keys = list(hash_map.keys())

    result = 1
    for i in range(len(keys)):
        n = len(hash_map[keys[i]])+1
        result *= n

    answer =  result-1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(clothes)


# counter와 reduce를 활용한 풀이
# from collections import Counter
# from functools import reduce

# def solution(clothes):
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer

# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

# print(solution(clothes))