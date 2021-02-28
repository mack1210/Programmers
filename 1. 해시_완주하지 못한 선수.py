def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

part = ["marina", "josipa", "nikola", "vinko", "filipa"]
comp = ["josipa", "filipa", "marina", "nikola"]

print(solution(part, comp))
