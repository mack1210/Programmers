def dfs(computer, computers, n, visited):
    visited[computer] = True

    for i in range(n):
        if (computers[computer][i] == 1) and (not visited[i]):
            computers[computer][i], computers[i][computer] = 0, 0
            dfs(i, computers, n, visited)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, n, visited)
            answer += 1
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))

