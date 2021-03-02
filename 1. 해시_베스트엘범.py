def solution(genres, plays):
    answer = []
    hash_map = {}
    hash_map_plays = {}
    for i, j in zip(genres, plays):
        if i in list(hash_map.keys()):
            hash_map[i].append(j)
            hash_map_plays[i] = sum(hash_map[i])
        else:
            hash_map[i] = [j]

    # 정렬 후 큰 순서대로 배치
    sorted_hash_map_plays = sorted(hash_map_plays.items(), key = lambda x: x[1], reverse= True)

    for key in sorted_hash_map_plays:
        play_list = hash_map[key[0]]
        play_list = sorted(play_list, key = lambda x : (-x[0], x[1]))
        
        for i in range(len(play_list)):
            if i == 2:
                break
            answer.append(play_list[i][1])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
