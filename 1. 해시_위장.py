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

print(no_clothes)